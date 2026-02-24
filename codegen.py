from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False, args=["--disable-blink-features=AutomationControlled"]
    )

    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    )

    page = context.new_page()
    page.goto("https://t-j.ru/average-income-calc/")

    container_field = page.locator('div[class^="_header_"]').filter(
        has_text="у мужа или жены есть доход"
    )
    locator_month = container_field.get_by_role("button", name="open block")

    page.wait_for_timeout(3000)
    locator_month.highlight()
    page.pause()


