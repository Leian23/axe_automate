from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from Pages.access_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

#qx7 validation
email_textbox = (By.XPATH, "//*[@type='email']")
password_textbox = (By.XPATH, "//*[@type='password']")
product_dev = (By.XPATH, "//*[@id='panel']/aside/section/ul/li[6]")
brand_style = (By.XPATH, "//*[@id='panel']/aside/section/ul/li[6]/ul/li[5]/a")
search_product = (By.XPATH, "//*[@id='brand_style_table_filter']/label/input")
filter_brand = (By.XPATH, "//*[@id='filterBrand']")
select_filter = (By.XPATH, "//*[@id='main-div']/section/div/div/div/div[2]/div[1]/div/div[8]/a")

browse_all_styles = (By.XPATH, "//*[@id='brand_style_table']/tbody/tr/td[1]")
product_name = (By.XPATH, "//*[@id='brand_style_table']/tbody/tr[1]/td[7]/table/tbody/tr[2]/td[2]")
product_sport = (By.XPATH, "//*[@id='brand_style_table']/tbody/tr[1]/td[7]/table/tbody/tr[2]/td[1]")
select_sport_and_gender = (By.XPATH, "//div/div/div/div/div/div/a")

search_product_name = (By.XPATH, "//*[@id='section-design-type']/div[2]/div/div/div[2]/div/div[3]/div[2]/input")
close_tips = (By.XPATH, "//*[@id='section-design-type']/div[2]/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div/div/p/div/div[2]/div")
select_dropdown_gender = (By.XPATH, "//*[@id='section-design-type']/div[2]/div/div/div[2]/div/div[3]/ul/li[2]/a")
male_gender = (By.XPATH, "//*[@id='section-design-type']/div[2]/div/div/div[2]/div/div[3]/ul/li[2]/div/ul/li[2]/div/label/div")
female_gender = (By.XPATH, "//*[@id='section-design-type']/div[2]/div/div/div[2]/div/div[3]/ul/li[2]/div/ul/li[3]")

#customizer
searched_style = (By.XPATH, "//*[@class='uk-width-auto uk-first-column']/div[@class='t-t-uppercase t-w-semibold']")
click_i_icon = (By.XPATH, "//*[@class='qx-btn-info uk-link-reset']")
thumbnail = (By.XPATH, "//*[@class='uk-inline-clip uk-transition-toggle']")
sublimation_image = (By.XPATH, "//*[@id='product-info-modal']/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/a/img")
close_image = (By.TAG_NAME, "body")
intended_fit = (By.XPATH, "//*[@id='product-info-modal']/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/a/img")

class SearchBrand(BasePage):

    def email_bcknd(self):
        return self.wait_driver(email_textbox)
    def password_backnd(self):
        return self.wait_driver(password_textbox)
    def click_product_dev(self):
        return self.wait_click_driver(product_dev)
    def click_brand_style_req(self):
        return self.wait_click_driver(brand_style)
    def search_product_item(self):
        return self.wait_driver(search_product)
    def filter_brand_axe(self):
        return self.wait_driver(filter_brand)
    def select_filter_brand_axe(self):
        return self.wait_driver(select_filter)
    def check_filtered_styles(self):
        return self.wait_elements(browse_all_styles)
    def check_product_name(self):
        return self.wait_driver(product_name)
    def check_product_sport(self):
        return self.wait_driver(product_sport)
    def check_matching_gender_and_sport(self):
        return self.wait_elements(select_sport_and_gender)
    def search_field(self):
        return self.wait_driver(search_product_name)
    def tips(self):
        return self.wait_click_driver(close_tips)
    def gender_dropdown(self):
        return self.wait_click_driver(select_dropdown_gender)
    def gender_male(self):
        return self.wait_click_driver(male_gender)
    def gender_female(self):
        return self.wait_click_driver(female_gender)
    def style_searched_style(self):
        return self.wait_elements(searched_style)
    def style_i_icon(self):
        return self.wait_elements(click_i_icon)
    def thumbnail_pic(self):
        return self.wait_elements(thumbnail)
    def sublimation(self):
        return self.wait_driver(sublimation_image)
    def close_images(self):
        return self.wait_driver(close_image)

    def intended_fit_img(self):
        return self.wait_driver(intended_fit)





