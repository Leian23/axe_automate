from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from Pages.access_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

wrestling = (By.XPATH, "//*[@id='qx-sports-con']/div[17]/div/div[3]/div/div[1]/a")
wrestling_text = (By.XPATH, "//*[@id='section-design-type']/div[1]/div[1]/div")
search_field = (By.XPATH, "//*[@id='section-design-type']/div[2]/div/div/div[2]/div/div[3]/div[2]/input")
close_tips = (By.XPATH, "//*[@id='section-design-type']/div[2]/div/div/div[2]/div/div[1]/div[3]/div/div/div/div/p/div/div[2]/div/button")
gender_field = (By.XPATH, "//*[@id='section-design-type']/div[2]/div/div/div[2]/div/div[3]/ul/li[2]/a")
select_male = (
By.XPATH, "//*[@id='section-design-type']/div[2]/div/div/div[2]/div/div[3]/ul/li[2]/div/ul/li[2]/div/label/div")

# Card item info
gender = (By.XPATH, "//*[@class='uk-grid uk-grid-collapse subtitle']/div[1]")
title = (By.XPATH, "//*[@class='uk-width-expand uk-first-column']/div[@class='t-t-uppercase t-w-semibold']")
style = (By.XPATH, "//*[@class='uk-width-auto uk-first-column']/div[@class='t-t-uppercase t-w-semibold']")
product_info_i = (By.XPATH, "//*[@id='qx-design-category-Quickturn']/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/a")
card_location = (By.XPATH, "//*[@id='qx-design-category-Quickturn']/div[1]/div/div")
adult_price = (By.XPATH, "//*[@class='body uk-margin-small']/div[1]")
youth_price = (By.XPATH, "//*[@class='body uk-margin-small']/div[2]")
brand_item_code = (By.XPATH, "//*[@class='uk-flex uk-flex-between uk-margin-top']/div[2]/div")

# product Info details
#product Info details
product_gender = (By.XPATH, "//*[@id='product-info-modal']/div/div/div[2]/div/div[2]/div[1]/span[1]")
product_title = (By.XPATH, "//*[@id='product-info-modal']/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/h1")
product_line = (By.XPATH, "//*[@id='product-info-modal']/div/div/div[2]/div/div[1]/h4")
product_style = (By.XPATH, "//*[@id='product-info-modal']/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/h4")
product_adult_price = (By.XPATH, "//*[@id='product-info-modal']/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/span")
product_youth_price = (By.XPATH, "//*[@id='product-info-modal']/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/span")
product_brand_item_code = (By.XPATH, "//*[@id='product-info-modal']/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]")



sizing_chart = (
By.XPATH, "//*[@id='product-info-modal']/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/a[1]")
inseam_chart = (
By.XPATH, "//*[@id='product-info-modal']/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/a[2]")
click_x_inseam = (By.XPATH, "//*[@id='inseam-guide-roster-modal']/div/div/button")
click_measure_guide = (
By.XPATH, "//*[@id='product-info-modal']/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/a[3]")
select_pl_upgrade = (By.XPATH, "//*[@id='brands-id']")
youth_price_item = (
By.XPATH, "//*[@id='index_price_item_table']/tbody/tr[1]/td[9]/table/tbody/tr[4]/td[text()='44.44']")
adult_price_item = (
By.XPATH, "//*[@id='index_price_item_table']/tbody/tr[1]/td[9]/table/tbody/tr[4]/td[text()='51.11']")
close_info_modal = (By.XPATH, "//*[@id='product-info-modal']/div/div/button")

# qx7 validation
email_textbox = (By.XPATH, "//*[@type='email']")
password_textbox = (By.XPATH, "//*[@type='password']")
hover_finance = (By.XPATH, "//*[@id='panel']/aside/section/ul/li[7]/a")
price_items = (By.XPATH, "//*[@id='panel']/aside/section/ul/li[7]/ul/li[3]/a")
select_filter = (By.XPATH, "//*[@id='main-div']/section/div/div/div/div[4]/div[1]/div/div[6]/a")
price_items_search = (By.XPATH, "//*[@id='index_price_item_table_filter']/label/input")

# access builder page
select_item = (By.XPATH, "//*[@class='uk-inline-clip uk-transition-toggle']")
first_item_load = (By.XPATH, "//*[@id='body-content']/div[1]/div[1]/div/div[3]/div[1]/div/div[1]/div[1]")
select_i_icon = (By.XPATH, "//*[@id='body-content']/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div[2]/a")
click_sublimation = (By.XPATH,
                     "//*[@id='body-content']/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div[2]/div/div/div/ul/li/div[1]/div[1]/div/div/a/img")
sublimation_img_visibility = (By.XPATH, "/html/body/div[8]/ul/li/img")
click_x = (By.XPATH, "/html/body/div[8]/div[1]/button/svg")

# fabric tab
select_fabric_drpdwn = (By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/ul/li")
zoom_fabric = (
By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/ul/li/div/ul/li/div/div[1]/a")
close_zoom_fabric = (By.XPATH, "//*[@id='fabric-modal']/div/div/button")
fabric_image_load = (By.XPATH, "//*[@id='fabric-modal']/div/div/div/div[1]/img")

# colors tab
select_colors_tab = (By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/a")
click_first_image = (By.XPATH, "//*[@id='body-content']/div[1]/div[1]/div/div[3]/div[1]/div/div[1]/div[1]/a/div")
click_2nd_image = (By.XPATH, "//*[@id='body-content']/div[1]/div[1]/div/div[3]/div[1]/div/div[1]/div[2]/a/div")
click_3rd_image = (By.XPATH, "//*[@id='body-content']/div[1]/div[1]/div/div[3]/div[1]/div/div[1]/div[3]/a/div")
click_4th_image = (By.XPATH, "//*[@id='body-content']/div[1]/div[1]/div/div[3]/div[1]/div/div[1]/div[4]/a/div")

product_details_info = (By.XPATH, "//*[@id='body-content']/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div[2]/div/div/div/ul/li/div[2]/ul/li")
scroll_through = (By.XPATH, "//*[@id='body-content']/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div[2]/div/div/div/ul/li/div[2]/ul")
click_all_gray_elements = (
By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/ul//*[@uk-tooltip='title:(GR) Gray']")
click_wheel = (By.XPATH,
               "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/div/div[4]/a/span/img")
click_kelly_green = (By.XPATH, "//*[@id='builder-modal-color-selection']/div/div/div[1]/div/div[19]/label")
click_black = (By.XPATH, "//*[@id='builder-modal-color-selection']/div/div/div[1]/div/div[1]/label")
click_yellow = (By.XPATH, "//*[@id='builder-modal-color-selection']/div/div/div[1]/div/div[13]/label")
save_colors_wheel = (By.XPATH, "//*[@id='builder-modal-color-selection']/div/div/div[2]/button")

body_colors = (
By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/ul/li[1]/div/div[2]/div/div")
sleeves_colors = (
By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/ul/li[2]/div/div[2]/div/div")
collar_colors = (
By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/ul/li[3]/div/div[2]/div/div")
front_graphic_color = (
By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/ul/li[4]/div/div[2]/div/div")
sleeve_stripe1_color = (
By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/ul/li[5]/div/div[2]/div/div")
sleeve_stripe2_color = (
By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/ul/li[6]/div/div[2]/div/div")
sleeve_end = (
By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/ul/li[7]/div/div[2]/div/div")
brand_logo_dropdown = (By.XPATH, "//*[@id='brand-logo']")
brand_logo_loc_drpdown = (By.XPATH, "//*[@id='brand-logo']/div[2]/ul/li[2]/div/div[2]/div/select")
brand_logo_color = (
By.XPATH, "//*[@id='brand-logo']/div[2]/ul/li[3]/div/div[2]/div/div/label[@class='wrapper-color-palette']")

pattern_tab = (By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[3]")
click_pattern = (By.XPATH, "//*[@id='pattern-nav']/li[1]/div/label")
select_arrow_camo = (By.XPATH, "//*[@id='qx-modal-pattern']/div[4]/button")

item_description = (By.XPATH, "//*[@id='index_price_item_table']/tbody/tr/td[7]")
all_price_list = (By.XPATH, "//*[@id='index_price_item_table']/tbody/tr/td[9]/table/tbody/tr//td[text()='MSRP']/following-sibling::td")
product_dev_tab = (By.XPATH, "//*[@id='panel']/aside/section/ul/li[6]")
brand_block_rules = (By.XPATH, "//*[@id='panel']/aside/section/ul/li[6]/ul/li[4]/a")
get_item_code = (By.XPATH, "//*[@id='index_price_item_table']/tbody/tr/td[5]")
filter_brand = (By.XPATH, "//*[@id='filterBrand']")

select_filter_brand_block_rules = (By.XPATH, "//*[@id='main-div']/section/div/div/div/div[2]/div[1]/div/div[8]/a")
filter_axe_brand = (By.XPATH, "//*[@id='factory-name']")
search_brand_block = (By.XPATH, "//*[@id='bpr_table_filter']/label/input")
select_pen_icon = (By.XPATH, "//*[@id='bpr_table']/tbody/tr/td[10]/a[2]")
select_eye_icon = (By.XPATH, "//*[@id='bpr_table']/tbody/tr/td[2]/a")
spec_sheet = (By.XPATH, "//*[@id='spec_sheet_details']")







class ProductInfor(BasePage):

    def click_wrestling_item(self):
        return self.wait_driver(wrestling)

    def check_wrestling_text(self):
        return self.wait_driver(wrestling_text)

    def text_search(self):
        return self.wait_driver(search_field)

    def close_tips(self):
        return self.wait_click_driver(close_tips)

    def select_gender_field(self):
        return self.wait_driver(gender_field)

    def select_male_gender(self):
        return self.wait_driver(select_male)

    # card item details
    def verify_gender(self):
        return self.wait_elements(gender)

    def verify_title(self):
        return self.wait_elements(title)

    def verify_style(self):
        return self.wait_elements(style)

    def verify_adult_price(self):
        return self.wait_elements(adult_price)

    def verify_youth_price(self):
        return self.wait_elements(youth_price)

    def verify_brand_item_code(self):
        return self.wait_elements(brand_item_code)

    def card_loc(self):
        return self.wait_driver(card_location)

    # click product info
    def click_i_btn(self):
        return self.wait_driver(product_info_i)

    # product info details
    def verify_product_gender(self):
        return self.wait_driver(product_gender)

    def verify_product_title(self):
        return self.wait_driver(product_title)

    def verify_product_line(self):
        return self.wait_driver(product_line)

    def verify_product_adult_price(self):
        return self.wait_driver(product_adult_price)

    def verify_product_youth_price(self):
        return self.wait_driver(product_youth_price)

    def verify_product_brand_item_code(self):
        return self.wait_driver(product_brand_item_code)

    def verify_product_style(self):
        return self.wait_driver(product_style)

    # further_infos
    def fetch_sizing_chart(self):
        return self.wait_driver(sizing_chart)

    def fetch_inseam_chart(self):
        return self.wait_driver(inseam_chart)

    def fetch_inseam_close(self):
        return self.wait_driver(click_x_inseam)

    def fetch_measure_guide(self):
        return self.wait_driver(click_measure_guide)

    # access qx7
    def email_bcknd(self):
        return self.wait_driver(email_textbox)

    def password_backnd(self):
        return self.wait_driver(password_textbox)

    def hover_finance_tab(self):
        return self.wait_driver(hover_finance)

    def click_price_items(self):
        return self.wait_driver(price_items)

    def brand_select_price_items(self):
        return self.wait_driver(select_pl_upgrade)

    def filter_pl_upgrade(self):
        return self.wait_driver(select_filter)

    def search_product(self):
        return self.wait_driver(price_items_search)

    def youth_prices(self):
        return self.wait_elements(youth_price_item)

    def adult_prices(self):
        return self.wait_elements(adult_price_item)

    def close_modal(self):
        return self.wait_click_driver(close_info_modal)

    def click_item(self):
        return self.wait_elements(select_item)

    def load_first_item(self):
        return self.wait_driver(first_item_load)

    def select_builder_modal(self):
        return self.wait_click_driver(select_i_icon)

    def select_sublimation(self):
        return self.wait_click_driver(click_sublimation)

    def sublimation_visibility(self):
        return self.wait_driver(sublimation_img_visibility)

    def close_sublimation_image(self):
        return self.wait_driver(click_x)

    def production_information(self):
        return self.wait_elements(product_details_info)

    def move_to_text_list(self):
        return self.wait_driver(scroll_through)

    def fabric_dropdown(self):
        return self.wait_driver(select_fabric_drpdwn)

    def zoom_fabric(self):
        return self.wait_click_driver(zoom_fabric)

    def close_modal_fabric(self):
        return self.wait_click_driver(close_zoom_fabric)

    def load_fabric_image(self):
        return self.wait_click_driver(fabric_image_load)

    def colors_tab(self):
        return self.wait_click_driver(select_colors_tab)

    def second_image(self):
        return self.wait_driver(click_2nd_image)

    def third_image(self):
        return self.wait_driver(click_3rd_image)

    def fourth_image(self):
        return self.wait_driver(click_4th_image)

    def first_image(self):
        return self.wait_driver(click_first_image)

    def click_first_color(self):
        return self.wait_elements(click_all_gray_elements)

    def click_picker(self):
        return self.wait_click_driver(click_wheel)

    def kelly_green(self):
        return self.wait_click_driver(click_kelly_green)

    def black(self):
        return self.wait_click_driver(click_black)

    def yellow(self):
        return self.wait_click_driver(click_yellow)

    def click_save(self):
        return self.wait_click_driver(save_colors_wheel)

    def click_body_colors(self):
        return self.wait_elements(body_colors)

    def click_sleeves_colors(self):
        return self.wait_elements(sleeves_colors)

    def click_collar_colors(self):
        return self.wait_elements(collar_colors)

    def click_front_graphic_color(self):
        return self.wait_elements(front_graphic_color)

    def click_sleeve_stripe_1_color(self):
        return self.wait_elements(sleeve_stripe1_color)

    def click_sleeve_stripe_2_color(self):
        return self.wait_elements(sleeve_stripe2_color)

    def click_sleeve_end(self):
        return self.wait_elements(sleeve_end)

    def click_brand_logo_drpdwn(self):
        return self.wait_driver(brand_logo_dropdown)

    def click_brand_logo_loc(self):
        return Select(self.wait_driver(brand_logo_loc_drpdown))

    def click_brand_logo_color(self):
        return self.wait_elements(brand_logo_color)

    def click_pattern_tab(self):
        return self.wait_driver(pattern_tab)

    def click_turn_on(self):
        return self.wait_driver(click_pattern)

    def select_arrow_camo(self):
        return self.wait_click_driver(select_arrow_camo)

    def item_description(self):
        return self.wait_elements(item_description)

    def price_list(self):
        return self.wait_elements(all_price_list)
    def product_dev(self):
        return self.wait_driver(product_dev_tab)
    def click_brand_block_rules(self):
        return self.wait_driver(brand_block_rules)
    def get_item_code_pi(self):
        return self.wait_elements(get_item_code)



    def filter_axe(self):
        return self.wait_driver(filter_axe_brand)
    def select_flter_btn(self):
        return self.wait_driver(select_filter_brand_block_rules)

    def brand_block(self):
        return self.wait_driver(search_brand_block)

    def pen_icon(self):
        return self.wait_driver(select_pen_icon)
    def spec_sheet_details(self):
        return self.wait_driver(spec_sheet)






























