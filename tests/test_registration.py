import time

from playwright.sync_api import Page, sync_playwright
from playwright.sync_api import expect
from pages.registration_page import RegistrationPage

url = "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/authorization/signup/"


def test_registration(browser_context):
    page = browser_context.new_page()

    page = RegistrationPage(page)
    page.go_to(url)
    page.enter_username("testik4")
    page.enter_password("pass123456pass")
    page.password_repeat("pass123456pass")
    page.submit()
    expect(page).to_have_url("http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/listings/list/")





