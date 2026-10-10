"""Quality requirement tests (Test Plan Section 9). These drive a real browser.

They need Playwright (see tests/README.md) and are skipped without it.
"""

import threading
import time

import pytest

from conftest import TASK, TOMORROW, make_app, mails_to, run_command, sign_in_link

pytestmark = pytest.mark.browser

PHONE = {"width": 390, "height": 844}
# A slowed, phone-like connection: 150 ms each way, about 1.6 Mbit/s down
PHONE_NETWORK = {"offline": False, "latency": 150, "downloadThroughput": 200_000, "uploadThroughput": 90_000}


@pytest.fixture
def live(clock, inbox, db_url):
    """The app running on a real local web server, for the browser to visit."""
    playwright_api = pytest.importorskip("playwright.sync_api")
    from werkzeug.serving import make_server

    application = make_app(clock, inbox, db_url, FORCE_HTTPS=False)
    server = make_server("127.0.0.1", 0, application, threaded=True)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}"
    application.config["BASE_URL"] = base
    with playwright_api.sync_playwright() as pw:
        try:
            browser = pw.chromium.launch()
        except Exception as err:  # browser not installed
            pytest.skip(f"Chromium for Playwright is not installed: {err}")
        yield application, base, browser, inbox
        browser.close()
    server.shutdown()


def browser_sign_in(app, base, browser, inbox, username, role, viewport=PHONE):
    email = f"{username}@example.test"
    run_command(app, "create-account", username, email, "--role", role)
    context = browser.new_context(viewport=viewport)
    page = context.new_page()
    page.goto(f"{base}/sign-in")
    page.fill("input[name=email]", email)
    page.locator("form button, form input[type=submit]").first.click()
    page.wait_for_load_state()
    page.goto(base + sign_in_link(mails_to(inbox, email)[-1]))
    return page


def post_tasks(app, coord_client_page, base, count_slots):
    """Posts tasks through the coordinator's browser session cookie, two slots per task."""
    request = coord_client_page.context.request
    for i in range(count_slots // 2):
        request.post(
            f"{base}/tasks/new",
            form={
                "title": f"Test Task {i:02d}",
                "description": "Made-up test task",
                "date": TOMORROW.isoformat(),
                "slot_start": "09:00",
                "slot_end": "10:00",
                "places": "4",
            },
        )
        request.post(
            f"{base}/tasks/new",
            form={
                "title": f"Test Task {i:02d} later",
                "description": "Made-up test task",
                "date": TOMORROW.isoformat(),
                "slot_start": "10:00",
                "slot_end": "11:00",
                "places": "4",
            },
        )


def test_t_qr_01_open_slots_loads_fast_on_a_phone(live):
    """Speed · PRD 6"""
    app, base, browser, inbox = live
    coord = browser_sign_in(app, base, browser, inbox, "test_coord_01", "coordinator")
    post_tasks(app, coord, base, 50)

    page = browser_sign_in(app, base, browser, inbox, "test_vol_01", "volunteer")
    cdp = page.context.new_cdp_session(page)
    cdp.send("Network.enable")
    cdp.send("Network.emulateNetworkConditions", PHONE_NETWORK)

    def load_seconds():
        start = time.perf_counter()
        page.goto(f"{base}/slots", wait_until="load")
        return time.perf_counter() - start

    seconds = load_seconds()
    if seconds >= 2:  # Test Plan Section 13: rerun once before reporting
        seconds = load_seconds()
    assert page.locator("text=places left").count() >= 50, "fewer than 50 open slots shown"
    assert seconds < 2, f"S-3 took {seconds:.2f} seconds"


# Runs in the page: contrast ratio, accessible names, and button sizes.
CHECKS_JS = r"""
() => {
  const problems = [];
  const lum = (rgb) => {
    const c = rgb.match(/[\d.]+/g).slice(0, 3).map(Number).map(v => {
      v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
  };
  const background = (el) => {
    for (let e = el; e; e = e.parentElement) {
      const bg = getComputedStyle(e).backgroundColor;
      const alpha = (bg.match(/[\d.]+/g) || [])[3];
      if (bg && bg !== 'transparent' && alpha !== '0') return bg;
    }
    return 'rgb(255, 255, 255)';
  };
  const visible = (el) => {
    const r = el.getBoundingClientRect(); const s = getComputedStyle(el);
    return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none';
  };
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (walker.nextNode()) {
    const node = walker.currentNode; const el = node.parentElement;
    if (!node.textContent.trim() || !el || !visible(el)) continue;
    const fg = getComputedStyle(el).color; const bg = background(el);
    const [a, b] = [lum(fg), lum(bg)].sort((x, y) => y - x);
    const ratio = (a + 0.05) / (b + 0.05);
    if (ratio < 4.5) problems.push(`contrast ${ratio.toFixed(2)}:1 for "${node.textContent.trim().slice(0, 30)}"`);
  }
  const named = (el) => {
    if ((el.getAttribute('aria-label') || '').trim()) return true;
    if (el.labels && [...el.labels].some(l => l.textContent.trim())) return true;
    if (['BUTTON', 'A'].includes(el.tagName) && el.textContent.trim()) return true;
    if (el.tagName === 'INPUT' && ['submit', 'button'].includes(el.type) && el.value.trim()) return true;
    return false;
  };
  for (const el of document.querySelectorAll('button, input:not([type=hidden]), select, textarea, a[href]')) {
    if (!visible(el)) continue;
    if (!named(el)) problems.push(`no text label: <${el.tagName.toLowerCase()} name="${el.name || ''}">`);
  }
  for (const el of document.querySelectorAll('button, input[type=submit], a.btn, [role=button]')) {
    if (!visible(el)) continue;
    const r = el.getBoundingClientRect();
    if (r.width < 44 || r.height < 44) problems.push(`button "${el.textContent.trim() || el.value}" is ${Math.round(r.width)}x${Math.round(r.height)} px`);
  }
  if (!document.documentElement.lang) problems.push('page has no language set');
  return problems;
}
"""


def test_t_qr_02_accessibility_checks_on_every_screen(live):
    """Accessibility · PRD 6; d05-01 Section 10"""
    app, base, browser, inbox = live
    coord = browser_sign_in(app, base, browser, inbox, "test_coord_01", "coordinator")
    coord.context.request.post(
        f"{base}/tasks/new",
        form={"title": TASK, "description": "Made-up test task", "date": TOMORROW.isoformat(),
              "slot_start": "09:00", "slot_end": "10:00", "places": "2"},
    )
    vol = browser_sign_in(app, base, browser, inbox, "test_vol_01", "volunteer")
    admin = browser_sign_in(app, base, browser, inbox, "test_admin_01", "admin", {"width": 1280, "height": 800})
    anon = browser.new_context(viewport=PHONE).new_page()

    vol.goto(f"{base}/slots")
    confirm_href = vol.locator(f"[aria-label='Sign up for {TASK}, 9 to 10']").get_attribute("href")
    vol.request.post(base + confirm_href.replace("/confirm", "/sign-up"))
    coord.goto(f"{base}/my-tasks")
    roster_href = coord.locator(f"[aria-label='Roster for {TASK}, 9 to 10']").get_attribute("href")

    screens = [
        ("S-1", anon, "/sign-in"),
        ("S-2", anon, "/create-account"),
        ("S-3", vol, "/slots"),
        ("S-4", vol, confirm_href),
        ("S-5", vol, "/my-sign-ups"),
        ("S-6", coord, "/my-tasks"),
        ("S-7", coord, "/tasks/new"),
        ("S-8", coord, roster_href),
        ("S-9", coord, "/volunteers/test_vol_01/message"),
        ("S-10", admin, "/blocked"),
    ]
    all_problems = []
    for screen, page, path in screens:
        page.goto(base + path)
        all_problems += [f"{screen}: {p}" for p in page.evaluate(CHECKS_JS)]
    assert not all_problems, "\n".join(all_problems)
