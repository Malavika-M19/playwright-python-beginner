from playwright.sync_api import sync_playwright

""" Verify that the title of the page is correct"""
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://automationintesting.online/")
    print(page.title())
    expected_title = "Restful-booker-platform demo"
    assert page.title() == expected_title, f"Expected title '{expected_title}', but got '{page.title()}'"
    browser.close()

