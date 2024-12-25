from playwright.sync_api import Page
from pages.base_page import BasePage


class RegistrationPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_locator = "input[id='id_username']"
        self.password_locator = "input[id='id_password1']"
        self.repeat_password_locator = "input[id='id_password2']"
        self.submit_locator = "button[type='submit']"

    def enter_username(self, username):
        self.type(self.username_locator, username)

    def enter_password(self, password):
        self.type(self.password_locator, password)

    def password_repeat(self, password):
        self.type(self.repeat_password_locator, password)

    def submit(self):
        self.click(self.submit_locator)

    # def successful_message(self, page: Page, successful_message):
    #     page.get_by_test_id()
