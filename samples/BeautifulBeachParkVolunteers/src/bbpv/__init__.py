"""BeautifulBeachPark Volunteers: the app.

create_app() builds the Flask app. Every setting comes from an environment
variable (d08-02 Section 5), so the same code runs on your own computer and
on Parks IT's servers; the tests pass their own settings in `config`.
"""

import datetime as dt
import os
import secrets

from flask import Flask, abort, g, redirect, request, session
from werkzeug.middleware.proxy_fix import ProxyFix

from . import db, wording
from .privacy import EmailVault, valid_key


def _env_bool(name, default):
    return os.environ.get(name, default).strip().lower() in ("1", "true", "yes", "on")


def _settings_from_environment():
    return {
        "DATABASE_URL": os.environ.get("DATABASE_URL", "sqlite:///bbpv-local.db"),
        "SECRET_KEY": os.environ.get("SECRET_KEY"),
        "EMAIL_ENCRYPTION_KEY": os.environ.get("EMAIL_ENCRYPTION_KEY"),
        "BASE_URL": os.environ.get("BASE_URL", "http://localhost:5000"),
        "FORCE_HTTPS": _env_bool("FORCE_HTTPS", "true"),
        "EMAIL_SERVICE": os.environ.get("EMAIL_SERVICE"),
        "EMAIL_FROM": os.environ.get("EMAIL_FROM"),
        "SMTP_HOST": os.environ.get("SMTP_HOST"),
        "SMTP_PORT": os.environ.get("SMTP_PORT", "587"),
        "SMTP_USER": os.environ.get("SMTP_USER"),
        "SMTP_PASSWORD": os.environ.get("SMTP_PASSWORD"),
        "SIGN_IN_LINK_MINUTES": int(os.environ.get("SIGN_IN_LINK_MINUTES", "15")),
        "TRUST_PROXY": _env_bool("TRUST_PROXY", "false"),
        "DB_POOL_SIZE": int(os.environ.get("DB_POOL_SIZE", "15")),
    }


def create_app(config=None):
    app = Flask(__name__)
    app.config.update(_settings_from_environment())
    app.config.update(config or {})
    cfg = app.config

    testing = cfg.get("TESTING", False)
    if not cfg.get("SECRET_KEY"):
        if not testing:
            raise RuntimeError("SECRET_KEY is not set. See d08-02 Section 5.")
        cfg["SECRET_KEY"] = secrets.token_hex(32)
    if not cfg.get("EMAIL_ENCRYPTION_KEY"):
        if not testing:
            raise RuntimeError(
                "EMAIL_ENCRYPTION_KEY is not set. Make one with "
                "'flask --app bbpv new-key' and keep it in the secret store (d08-02 Section 5)."
            )
        cfg["EMAIL_ENCRYPTION_KEY"] = EmailVault.new_key()
    if not valid_key(cfg["EMAIL_ENCRYPTION_KEY"]):
        raise RuntimeError("EMAIL_ENCRYPTION_KEY is not a valid key. Make one with 'flask --app bbpv new-key'.")
    if not testing and cfg.get("EMAIL_SERVICE") not in ("pretend", "smtp"):
        raise RuntimeError("EMAIL_SERVICE must be 'pretend' (local only) or 'smtp'. See d08-02 Section 5.")
    if cfg.get("EMAIL_SERVICE") == "pretend" and not cfg["DATABASE_URL"].startswith("sqlite"):
        # The pretend inbox shows every email on a web page: never on the live servers.
        raise RuntimeError("EMAIL_SERVICE=pretend is for the local environment only.")
    if not cfg.get("EMAIL_FROM"):
        host = cfg["BASE_URL"].split("://", 1)[-1].split("/", 1)[0].split(":", 1)[0]
        domain = host if "." in host else "localhost.test"
        cfg["EMAIL_FROM"] = f"BeautifulBeachPark Volunteers <no-reply@{domain}>"
    if not callable(cfg.get("CLOCK")):
        cfg["CLOCK"] = dt.datetime.now

    cfg["SESSION_COOKIE_HTTPONLY"] = True
    cfg["SESSION_COOKIE_SAMESITE"] = "Lax"
    cfg["SESSION_COOKIE_SECURE"] = bool(cfg["FORCE_HTTPS"])
    cfg["PERMANENT_SESSION_LIFETIME"] = dt.timedelta(days=30)
    if cfg.get("TRUST_PROXY"):
        app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

    app.extensions["engine"] = db.make_engine(cfg["DATABASE_URL"], cfg["DB_POOL_SIZE"])
    app.extensions["vault"] = EmailVault(cfg["EMAIL_ENCRYPTION_KEY"])
    app.extensions["pretend_inbox"] = []
    db.metadata.create_all(app.extensions["engine"])

    _add_request_hooks(app)

    from . import cli, views
    app.register_blueprint(views.bp)
    cli.register(app)
    return app


def _add_request_hooks(app):
    @app.before_request
    def https_only():
        """Spec 11.1: nothing is served over plain HTTP."""
        if app.config["FORCE_HTTPS"] and not request.is_secure:
            return redirect(request.url.replace("http://", "https://", 1), code=301)

    @app.before_request
    def load_user():
        g.user = None
        account_id = session.get("account_id")
        if account_id is not None:
            with app.extensions["engine"].connect() as conn:
                row = conn.execute(
                    db.accounts.select().where(db.accounts.c.id == account_id)
                ).mappings().first()
            if row is None:
                session.clear()
            else:
                g.user = dict(row)

    @app.before_request
    def check_form_token():
        """Requests that change something must come from one of our own forms."""
        if app.config.get("TESTING") or request.method != "POST":
            return
        sent = request.form.get("csrf_token", "")
        if not sent or not secrets.compare_digest(sent, session.get("csrf_token", "")):
            abort(400)

    @app.context_processor
    def page_helpers():
        if "csrf_token" not in session:
            session["csrf_token"] = secrets.token_urlsafe(32)
        return {
            "user": g.get("user"),
            "csrf_token": session["csrf_token"],
            "pretend_inbox": app.config["EMAIL_SERVICE"] == "pretend" and app.config.get("TEST_INBOX") is None,
            "w": wording,
        }

    @app.after_request
    def security_headers(resp):
        resp.headers.setdefault("X-Content-Type-Options", "nosniff")
        resp.headers.setdefault("Referrer-Policy", "no-referrer")
        resp.headers.setdefault("X-Frame-Options", "DENY")
        if app.config["FORCE_HTTPS"]:
            resp.headers.setdefault("Strict-Transport-Security", "max-age=31536000")
        return resp
