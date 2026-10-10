"""Keeping email addresses private (Spec Section 11.1, DD-4).

- Emails are stored encrypted, and decrypted only to send an email.
- Each email also gets two scrambled (hashed) copies that can't be turned
  back into the address: one to find the account at sign-in, one for the
  block list, which survives when an account is deleted.
"""

import base64
import hashlib
import hmac

from cryptography.fernet import Fernet


def standardize(email):
    """Lowercase, and remove dots and any '+' tag before the '@' (Spec Section 6).

    j.o.h.n+beach@example.test and john@example.test are the same inbox.
    """
    email = email.strip().lower()
    local, at, domain = email.rpartition("@")
    if not at:
        return email
    local = local.split("+", 1)[0].replace(".", "")
    return f"{local}@{domain}"


class EmailVault:
    def __init__(self, key):
        self._fernet = Fernet(key)
        self._hash_key = hashlib.sha256(b"bbpv-email-hash:" + key.encode()).digest()

    @staticmethod
    def new_key():
        return Fernet.generate_key().decode()

    def encrypt(self, email):
        return self._fernet.encrypt(email.strip().encode("utf-8", "surrogatepass")).decode()

    def decrypt(self, token):
        return self._fernet.decrypt(token.encode()).decode("utf-8", "surrogatepass")

    def _hash(self, text):
        return hmac.new(self._hash_key, text.encode("utf-8", "surrogatepass"), hashlib.sha256).hexdigest()

    def lookup_key(self, email):
        return self._hash("lookup:" + email.strip().lower())

    def block_key(self, email):
        return self._hash("block:" + standardize(email))


def token_hash(token):
    return hashlib.sha256(token.encode()).hexdigest()


def looks_like_email(email):
    email = email.strip()
    if not 3 <= len(email) <= 254 or any(c.isspace() for c in email):
        return False
    local, at, domain = email.rpartition("@")
    return bool(at and local and "." in domain.strip(".") and "@" not in domain)


def valid_key(key):
    try:
        return len(base64.urlsafe_b64decode(key.encode())) == 32
    except Exception:
        return False
