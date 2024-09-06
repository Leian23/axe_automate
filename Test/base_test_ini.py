from selenium.webdriver.common.keys import Keys
from Pages.access_page import BasePage
from Assets.credentials import email_info, password_info, user_first_name, green_color, reset_color
import time


class BaseTest:
    def test_homepage(self):
        homepage = BasePage(self.driver)
        homepage.get_icon().click()

    def test_login(self):
        homepage = BasePage(self.driver)
        time.sleep(2)
        email_textbox = homepage.email_text_box()
        password_textbox = homepage.password_text_box()

        if email_textbox.is_displayed() and password_textbox.is_displayed():
            print(green_color + "Email and password textbox displayed" + reset_color)
            email_textbox.send_keys(email_info)
            password_textbox.send_keys(password_info + Keys.RETURN)

        assert email_textbox.is_displayed() and password_textbox.is_displayed(), "Email and password texbox does not exist"
        time.sleep(5)

    def test_validate_user(self):
        homepage = BasePage(self.driver)
        user_name = homepage.validate_current_user()
        my_cart = homepage.validate_my_cart()

        print(green_color + f"Expected user first name: {user_first_name} matches to {user_name}" + reset_color)
        print(green_color + f"My Cart text on page: {my_cart}" + reset_color)
        assert user_first_name == user_name and my_cart == "My Cart", "user not logged in"

    def test_click_customizer(self):
        time.sleep(1)
        homepage = BasePage(self.driver)
        homepage.click_customizer().click()
        time.sleep(3)

