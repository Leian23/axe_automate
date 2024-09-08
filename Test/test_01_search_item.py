from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select
from Utilities.baseclass import BaseClass
from Pages.search_for_item_page import SearchBrand
from Assets.credentials import green_color, reset_color, blue_color, email_qx7, password_qx7
from Assets.styles import block, style, male, female, fetched_style, fetched_gender, fetched_product_name, fetched_product_sport, indexes
from Test.base_test_ini import BaseTest

import random
import time


class TestSearchItem(BaseClass, BaseTest):

    def test_search_brand_style(self):

        self.driver.execute_script("window.open('');")

        window_handles = self.driver.window_handles

        self.driver.switch_to.window(window_handles[-1])
        self.driver.get("https://qx7-axe-customizer-stg.qstrike.net/login")

        item2 = SearchBrand(self.driver)
        time.sleep(2)
        item2.email_bcknd().send_keys(email_qx7)
        item2.password_backnd().send_keys(password_qx7 + Keys.RETURN)
        time.sleep(3)

        action = ActionChains(self.driver)
        action.move_to_element(item2.click_product_dev()).perform()
        time.sleep(2)
        action.move_to_element(item2.click_brand_style_req()).click().perform()
        time.sleep(2)
        Select(item2.filter_brand_axe()).select_by_visible_text("AXE")
        time.sleep(2)
        item2.select_filter_brand_axe().click()
        time.sleep(1)
        item2.search_product_item().send_keys(block[0])
        time.sleep(3)

        input_style = style[0]
        found_style = item2.check_filtered_styles()
        time.sleep(3)

        style_found = False

        for items in found_style:
            if items.text == input_style:
                style_found = True
                print(green_color + f"Style '{items.text}' found" + reset_color)
                fetched_style.append(items.text)
                break

        assert style_found, "No Style Found"


    def test_validate_gender(self):
        gender_found = False

        if male in block[0]:
            gender_found = True
            print(green_color + f"Gender 'Men' found" + reset_color)
            found_gender = "Men"
        elif female in block[0]:
            gender_found = True
            print(green_color + f"Gender 'Women' found" + reset_color)
            found_gender = "Women"
        else:
            found_gender = None  # No gender found

        assert gender_found, "No Gender Found"
        fetched_gender.append(found_gender)

        time.sleep(2)

    def test_get_product_name(self):
        item2 = SearchBrand(self.driver)

        product_name_text = item2.check_product_name().text
        fetched_product_name.append(product_name_text)

        assert product_name_text, "Product name not found"
        print(green_color + f"Product name '{product_name_text}' found" + reset_color)


    def test_get_product_sport(self):
        item2 = SearchBrand(self.driver)

        product_sport =item2.check_product_sport().text
        fetched_product_sport.append(product_sport)
        assert product_sport, "Product sport not found"
        print(green_color + f"Product sport '{product_sport}' found" + reset_color)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_select_sport_gender(self):
        time.sleep(2)
        item2 = SearchBrand(self.driver)

        sport_list = item2.check_matching_gender_and_sport()

        get_gender = fetched_gender[0]
        get_sport = fetched_product_sport[0]

        print(f"get_gender: {get_gender}, get_sport: {get_sport}")

        target_link = None
        for items3 in sport_list:
            link_text = items3.get_attribute("href")
            print(link_text)
            if get_gender.lower() in link_text and get_sport in link_text:
                target_link = items3
                self.driver.execute_script("arguments[0].scrollIntoView();", items3)
                break

        assert target_link is not None, "No matching gender and sport found in the list."
        print(green_color + f"Matching gender and sport '{target_link}' found" + reset_color)

        target_link.click()

        time.sleep(2)


    def test_search_specific_item(self):
        item2 = SearchBrand(self.driver)
        time.sleep(2)
        item2.tips().click()
        time.sleep(2)
        search_text = fetched_product_name[0]
        search_for_item = item2.search_field()
        search_for_item.send_keys(search_text)
        time.sleep(1)

        select_field = item2.gender_dropdown()
        self.driver.execute_script("arguments[0].scrollIntoView();", select_field)
        select_field.click()

        time.sleep(1)

        print(fetched_gender[0])
        if fetched_gender[0] == "Men":
            male = item2.gender_male()
            self.driver.execute_script("arguments[0].scrollIntoView();", male)
            male.click()
        elif fetched_gender[0] == "Women":
            female = item2.gender_female()
            self.driver.execute_script("arguments[0].scrollIntoView();", female)
            female.click()

        styles_available = item2.style_searched_style()
        click_i_icon = item2.style_i_icon()
        thumbnails = item2.thumbnail_pic()

        click_i = False
        time.sleep(2)
        for items4 in styles_available:
            print(green_color + f"Style '{items4.text}' found, fetched style is {fetched_style[0]}" + reset_color)
            if items4.text.lower() == fetched_style[0].lower():
                time.sleep(2)
                index = styles_available.index(items4)
                click_item = click_i_icon[index]
                view_thumbnail = thumbnails[index]
                self.driver.execute_script("arguments[0].scrollIntoView();", view_thumbnail)
                click_item.click()
                click_i = True
                indexes.append(index)
                break
        assert click_i, "'i' icon cannot be found"
        time.sleep(2)
        print(green_color + f"Item 'i' has been clicked {indexes[0]}" + reset_color)

        time.sleep(3)

        print(blue_color + f"Now Validating '{block[0]}', where style is {fetched_style[0]} " + reset_color)


    def test_sublimation_image(self):
        item2 = SearchBrand(self.driver)
        item2.sublimation().click()
        time.sleep(3)
        close_button = item2.close_images()
        close_button.send_keys(Keys.ESCAPE)
        time.sleep(2)

    def test_intended_fit_image(self):
        item2 = SearchBrand(self.driver)
        item2.intended_fit_img().click()
        time.sleep(3)
        close_button1 = item2.close_images()
        close_button1.send_keys(Keys.ESCAPE)
