from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    person_icon = (By.XPATH, "//*[@class='qx-login']")
    email = (By.XPATH, "//*[@id='login-dropdown']/form/div[1]/div/input")
    password = (By.XPATH, "//*[@id='login-dropdown']/form/div[2]/div/div/input")
    validate_logged_acc = (By.XPATH, "//a[@class='qx-user-account']/span[@class='t-t-capitalize uk-visible@m']")
    custom = (By.XPATH, "//*[@id='menu-customizer']")
    my_cart = (By.XPATH, "//*[@id='qx-header']/div[3]/ul/li[2]/a/span")

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def wait_driver(self, locator):
        wait = WebDriverWait(self.driver, 40)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_click_driver(self, locator):
        wait = WebDriverWait(self.driver, 40)
        return wait.until(EC.element_to_be_clickable(locator))

    def wait_invisibility(self, locator):
        wait = WebDriverWait(self.driver, 40)
        return wait.until(EC.invisibility_of_element_located(locator))

    def wait_visibility(self, locator):
        wait = WebDriverWait(self.driver, 40)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_elements(self, locator):
        wait = WebDriverWait(self.driver, 40)
        return wait.until(EC.presence_of_all_elements_located(locator))

    def get_icon(self):
        return self.driver.find_element(*BasePage.person_icon)

    def email_text_box(self):
        return self.driver.find_element(*BasePage.email)

    def password_text_box(self):
        return self.driver.find_element(*BasePage.password)

    def click_customizer(self):
        return self.driver.find_element(*BasePage.custom)

    def validate_current_user(self):
        return self.wait_driver(BasePage.validate_logged_acc).text

    def validate_my_cart(self):
        return self.wait_driver(BasePage.my_cart).text
















