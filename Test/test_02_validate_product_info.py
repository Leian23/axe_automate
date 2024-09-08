import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from Pages.product_info_page import ProductInfor
from Assets.credentials import green_color, reset_color, blue_color
from Utilities.baseclass import BaseClass
from Assets.styles import indexes, test_index, block, fetch_item_code, fetched_gender, spec_sheet


class TestProductInfo(BaseClass):
    def test_compare_info(self):
        item2 = ProductInfor(self.driver)
        product_index = indexes[0]

        genders = item2.verify_gender()
        titles = item2.verify_title()
        adult_prices = item2.verify_adult_price()
        styles = item2.verify_style()
        youth_prices = item2.verify_youth_price()
        brand_item_codes = item2.verify_brand_item_code()

        gender = None
        info_title = None
        final_adult_price = None
        info_style = None
        final_youth_price = None
        final_brand_item_code = None

        time.sleep(2)

        for g in genders:
            indexss_g = genders.index(g)
            if indexss_g == product_index:
                gender_text = g.text[:3].lower()  # Extract text from WebElement and perform operations
                gender = gender_text
                test_index.append(indexss_g)
                print(green_color + f"{gender}" + reset_color)
                break

        for t in titles:
            indexss_t = titles.index(t)
            if indexss_t == product_index:
                title = t.text.lower()  # Extract text from WebElement and perform operations
                info_title = title
                break

        for ap in adult_prices:
            indexss_ap = adult_prices.index(ap)
            if indexss_ap == product_index:
                ap_price = ap.text.split()[1].lower()
                final_adult_price = ap_price
                break

        for st in styles:
            indexss_st = styles.index(st)
            if indexss_st == product_index:
                style_info = st.text.lower()
                info_style = style_info
                break

        for yp in youth_prices:
            indexss_yp = youth_prices.index(yp)
            if indexss_yp == product_index:
                youth_price_info = yp.text.split()[1].lower()
                final_youth_price = youth_price_info
                break

        for bic in brand_item_codes:
            indexss_bic = brand_item_codes.index(bic)
            if indexss_bic == product_index:
                brand_code = bic.text.lower()
                final_brand_item_code = brand_code
                break

        #fetch the gender informat


        print(f"Gender is {gender} in index, title is {info_title}, adult price is {final_adult_price}, style is {info_style}, final youth price is {final_youth_price}, final brand item code is {final_brand_item_code}index is '{test_index[0]}' ")

        #fetched gender
        fetched_gender.append(gender)

        card_info = {
            "gender": gender,
            "title": info_title,
            "adult_price": final_adult_price,
            "style": info_style,
            "youth_price": final_youth_price,
            "brand_item_code": final_brand_item_code,
        }

        time.sleep(2)

        modal_info = {
            "gender": item2.verify_product_gender().text[:3].lower(),
            "title": item2.verify_product_title().text.lower(),
            "adult_price": item2.verify_product_adult_price().text.lower(),
            "style": item2.verify_product_style().text.lower(),
            "youth_price": item2.verify_product_youth_price().text.lower(),
            "brand_item_code": item2.verify_product_brand_item_code().text.lower(),
        }

        print("Card Info:", card_info, '\n')
        print("Modal Info:", modal_info, '\n')

        assert card_info == modal_info, (
            f"Mismatch found:\n"
            f"Card Info: {card_info}\n"
            f"Modal Info: {modal_info}"
        )
        print(green_color + "Card info and Modal info are matched" + reset_color)



    def test_verify_product_line(self):
        item2 = ProductInfor(self.driver)
        product_line = item2.verify_product_line().text.lower()
        assert product_line, "product line doesn't exist"
        print(green_color + f"product line '{product_line}' existing" + reset_color)

    def test_select_sizing_chart(self):
        item2 = ProductInfor(self.driver)

        click_sizing_chart = item2.fetch_sizing_chart()
        self.driver.execute_script("arguments[0].scrollIntoView();", click_sizing_chart)

        click_sizing_chart.click()

        window_handles = self.driver.window_handles

        self.driver.switch_to.window(window_handles[-1])
        assert "https://s3.us-west-2.amazonaws.com/qx7/uploaded_files" in self.driver.current_url, "PDF URL not matched"
        print(green_color + "Passed: " + f"PDF URL matched: {self.driver.current_url}" + reset_color)
        time.sleep(3)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_access_inseam_chart(self):
        item2 = ProductInfor(self.driver)
        click_inseam_chart = item2.fetch_inseam_chart()
        self.driver.execute_script("arguments[0].scrollIntoView();", click_inseam_chart)
        click_inseam_chart.click()
        assert click_inseam_chart, "Inseam chart doesn't exist"
        time.sleep(2)
        item2.fetch_inseam_close().click()
        time.sleep(1.5)

    def test_how_to_measure(self):
        item2 = ProductInfor(self.driver)

        item2.fetch_measure_guide().click()

        window_handles = self.driver.window_handles

        self.driver.switch_to.window(window_handles[-1])

        assert "https://s3.us-west-2.amazonaws.com/qx7/uploaded_files" in self.driver.current_url, "Measure guide URL not matched"
        print(green_color + "Passed: " + f"Measure Guide URL matched: {self.driver.current_url}" + reset_color)

        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])


    def test_compare_price(self):
        time.sleep(2)
        item2 = ProductInfor(self.driver)

        brand_item_code = item2.verify_product_brand_item_code().text
        adult_price = item2.verify_product_adult_price().text.lower().replace('$', '')
        youth_price = item2.verify_product_youth_price().text.lower().replace('$', '')

        print(f"youth:{youth_price}, adult:{adult_price}")

        self.driver.execute_script("window.open('');")

        window_handles = self.driver.window_handles

        self.driver.switch_to.window(window_handles[-1])
        self.driver.get("https://qx7-axe-customizer-stg.qstrike.net/admin/price_items")

        #time.sleep(3)

        #action = ActionChains(self.driver)
        #action.move_to_element(item2.hover_finance_tab()).perform()
        #time.sleep(2)
        #action.move_to_element(item2.click_price_items()).click().perform()

        time.sleep(2)

        Select(item2.brand_select_price_items()).select_by_visible_text("AXE")
        time.sleep(2)
        item2.filter_pl_upgrade().click()
        item2.search_product().send_keys(brand_item_code)
        time.sleep(3)

        list_of_prices = item2.price_list()
        item_description_list = item2.item_description()
        price_youth = False
        price_adult = False
        loop_counter = 0

        for description in item_description_list:
            print(f"description is: {description.text}, Gender is: {fetched_gender[0]}")
            loop_counter += 1
            if fetched_gender[0] in description.text: #.text == block[0]:

                for price in list_of_prices:
                    price_value = price.text.split('.')[0]
                    print(price_value)

                    if price_value == youth_price:
                        price_youth = True
                        print(green_color + "Youth price matched" + reset_color)

                    if price_value == adult_price:
                        price_adult = True
                        print(green_color + "Adult price matched" + reset_color)

                    if price_youth and price_adult:
                        break

        item_code = item2.get_item_code_pi()
        time.sleep(1)

        print(loop_counter)
        for index, ap in enumerate(item_code, start=1):
            print(f"{index}: {ap.text}")
            if index == loop_counter:
                fetch_item_code.append(ap.text)
                print(green_color + f"Item code: {ap.text} successfully fetched" + reset_color)
                break

        assert price_youth and price_adult, "Prices matched from qx7 and front end"

        time.sleep(2)


    def test_go_to_brand_block_rules_price(self):
        item2 = ProductInfor(self.driver)
        action = ActionChains(self.driver)
        action.move_to_element(item2.product_dev()).perform()
        time.sleep(2)
        action.move_to_element(item2.click_brand_block_rules()).click().perform()
        time.sleep(2)
        Select(item2.filter_axe()).select_by_visible_text("AXE")
        time.sleep(2)
        item2.select_flter_btn().click()
        time.sleep(1)
        print(fetch_item_code[0])
        item2.brand_block().send_keys(fetch_item_code[0])
        time.sleep(3)
        #action.move_to_element(item2.select_eye_icon()).click().perform()
        icon = item2.pen_icon()
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)
        icon.click()

        #get brand info
        time.sleep(4)
        get_spec_sheet = item2.spec_sheet_details().get_attribute("value")
        spec_sheet.append(get_spec_sheet)


        print(green_color + f"Spec sheet successfully fetched: {spec_sheet[0]}" + reset_color)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])






    def test_go_to_builder(self):
        print(blue_color + "\nDirecting to builder page\n" + reset_color)
        item2 = ProductInfor(self.driver)
        item2.close_modal().click()

        time.sleep(2)

        select_items = item2.click_item()

        for idx, item in enumerate(select_items):
            if idx == indexes[0]:  # Compare the index of the item to the desired index
                self.driver.execute_script("arguments[0].scrollIntoView();", item)
                item.click()
                break

        first_item_visibility = item2.load_first_item()

        assert first_item_visibility, "First item of in the builder did not load"
        print(green_color + "Apparel has been loaded" + reset_color)

        time.sleep(2)

    def test_validate_duplicate_info(self):
        item2 = ProductInfor(self.driver)
        time.sleep(2)
        item2.select_builder_modal().click()
        time.sleep(2)
        product_details = item2.move_to_text_list()
        self.driver.execute_script("arguments[0].scrollIntoView();", product_details)

        product_info = item2.production_information()
        product_info_texts = [items.text for items in product_info]

        for items in product_info_texts:
            print(green_color + items + reset_color)

        self.check_duplicates(product_info_texts)
        time.sleep(3)



    def check_duplicates(self, items, substring_length=5):

        item2 = ProductInfor(self.driver)
        items = [item.strip().lower() for item in items if item.strip()]

        seen_substrings = set()
        duplicates = []

        for item in items:
            substring = item[:substring_length]
            if substring in seen_substrings:
                duplicates.append(item)
            else:
                seen_substrings.add(substring)

        print(items)
        assert not duplicates, f"Duplicates found: {duplicates}"
        print(green_color + "\nNo Duplicates Found in Product Info" + reset_color)
        time.sleep(2)
        item2.select_builder_modal().click()

