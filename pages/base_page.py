from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def go_to(self, url):
        """Navigate to a specific URL"""
        self.page.goto(url)

    def click(self, selector):
        """Click on an element"""
        self.page.locator(selector).click()

    def type(self, selector, text):
        """Type text into an input field"""
        self.page.locator(selector).fill(text)

    def wait_for_element(self, selector: str):
        """Wait for an element to be visible"""
        self.page.wait_for_selector(selector)

    def get_text(self, selector: str) -> str:
        """Get text from an element"""
        return self.page.inner_text(selector)

    def is_visible(self, selector: str) -> bool:
        """Check if an element is visible"""
        return self.page.is_visible(selector)

    def url(self) -> str:
        return self.page.url

