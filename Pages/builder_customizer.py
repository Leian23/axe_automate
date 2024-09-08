from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Pages.access_page import BasePage

select_fabric_drpdwn = (By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/ul/li")
zoom_fabric = (By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/ul/li/div/ul/li/div/div[1]/a")
close_zoom_fabric = (By.XPATH, "//*[@id='fabric-modal']/div/div/button")
fabric_image_load = (By.XPATH, "//*[@id='fabric-modal']/div/div/div/div[1]/img")
select_colors_tab = (By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/a")
click_first_image = (By.XPATH, "//*[@id='body-content']/div[1]/div[1]/div/div[3]/div[1]/div/div[1]/div[1]/a/div")
click_2nd_image = (By.XPATH, "//*[@id='body-content']/div[1]/div[1]/div/div[3]/div[1]/div/div[1]/div[2]/a/div")
click_3rd_image = (By.XPATH, "//*[@id='body-content']/div[1]/div[1]/div/div[3]/div[1]/div/div[1]/div[3]/a/div")
click_4th_image = (By.XPATH, "//*[@id='body-content']/div[1]/div[1]/div/div[3]/div[1]/div/div[1]/div[4]/a/div")
click_all_first_elements = (By.XPATH,"//*[@class='uk-grid-small uk-child-width-auto con-color-palettes uk-flex-middle uk-width-1-1 uk-grid']/div[1]")
click_wheel = (By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/div/div[4]/a/span")
click_bagby_green = (By.XPATH, "//*[@id='builder-modal-color-selection']/div/div/div[1]/div/div[45]/label")
click_infantry_blue = (By.XPATH, "//*[@id='builder-modal-color-selection']/div/div/div[1]/div/div[46]/label")
click_dessert_sand = (By.XPATH, "//*[@id='builder-modal-color-selection']/div/div/div[1]/div/div[47]/label")
save_colors_wheel = (By.XPATH, "//*[@id='builder-modal-color-selection']/div/div/div[2]/button")
body_colors = (By.XPATH, "//*[@class='uk-grid-small uk-child-width-auto con-color-palettes uk-flex-middle uk-width-1-1 uk-grid']/div")
brand_logo_dropdown = (By.XPATH, "//*[@id='brand-logo']/li/ul/li[1]")
second_brand_logo_dropdown = (By.XPATH, "//*[@id='brand-logo']/li/ul/li[2]")
brand_logo_color = (By.XPATH, "//*[@id='brand-logo']/li/ul/li[1]/div/ul/li[2]/div/div[2]/div/div/label")
second_brand_logo_color = (By.XPATH, "//*[@id='brand-logo']/li/ul/li[2]/div/ul/li[2]/div/div[2]/div/div/label")
first_brand_logo_loc = (By.XPATH, "//*[@id='brand-logo']/li/ul/li[1]/a/div/div[1]/h6")
second_brand_logo_text = (By.XPATH, "//*[@id='brand-logo']/li/ul/li[2]/a/div/div[1]/h6")
pattern_tab = (By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[3]")
click_pattern = (By.XPATH, "(//label[@class='btn-toggle'])[1]")
select_axe_dazzle = (By.XPATH, "//*[@id='qx-modal-pattern']/div[2]/button")
layer1_pattern = (By.XPATH, "//*[@id='pattern-nav']/li[1]/ul/li[2]/div/div[2]/div/div/label")
layer2_pattern = (By.XPATH, "//*[@id='pattern-nav']/li[1]/ul/li[3]/div/div[2]/div//div/label")
pattern_slider = (By.CSS_SELECTOR, ".slider-handle-lower")
text_tab = (By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[4]")
drop_downs_text_tab = (By.XPATH, "//div[@class='uk-grid-collapse uk-flex-middle uk-flex-between uk-grid']//div[@class='uk-width-expand wrapper-title uk-first-column']")
edit_team_name = (By.XPATH, "//*[@id='text-application-accordion']/li[1]/div[3]/ul[1]/li/div[1]/div[2]/div/input")
font_styles = (By.XPATH, "//*[@id='text-application-accordion']/li[1]/div[3]/ul[1]/li/div[2]/div[2]/div/a[2]")
font_layout = (By.XPATH, "//*[@id='text-application-accordion']/li[1]/div[3]/ul[1]/li/div[3]/div[2]/div/a[2]")
tail_sweep_location = (By.XPATH, "//h6[normalize-space(text())='Tail Sweep']")
tail_sweep_items = (By.XPATH, "//*[@id='team-name-1-accordion-item-91']/div[3]/ul/li[3]/div/div[2]/div/div")
click_first_dropdown = (By.XPATH, "//*[@id='text-application-accordion']/li[1]")

font_accents = (By.XPATH, "//*[@id='team-name-1-accordion-item-91']/div[3]/ul/li[4]/div[1]/div[2]/div/div")
base_color_accents = (By.XPATH, "//*[@class='uk-grid-small uk-child-width-auto con-color-palettes uk-flex-middle uk-width-1-1 uk-grid']/div/label")
team_name_body_enable_default = (By.XPATH, "//*[@class='application-item']/div/label")
player_name_body_enable_default = (By.XPATH, "//*[@id='text-application-accordion']/li[2]")

toggle_location = (By.XPATH, "//*[@class='qx-btn-toggle btn-toggle']")
player_name_text_field = (By.XPATH, "//*[@id='text-application-accordion']/li[2]/div[3]/ul/li[1]/div[1]/div[2]/div/input")
select_player_name_font = (By.XPATH, "//*[@id='text-application-accordion']/li[2]/div[3]/ul/li[1]/div[2]/div[2]/div/a[2]")
font_accent_location_player_name = (By.XPATH, "//*[@id='text-application-accordion']/li[2]/div[3]/ul/li[3]/div[1]/div[2]/div")
font_accent_player_name_items = (By.XPATH, "//*[@id='text-application-accordion']/li[2]/div[3]/ul/li[3]/div[1]/div[2]/div/div")
pl_name_base_color = (By.XPATH, "//*[@id='accent-config-92']/li[1]/ul/li/div/div[2]/div/div/label")
pattern_slider = (By.XPATH, "//*[@id='pattern-nav']/li[1]/ul/li[4]/div/div[2]/div/div/div[2]/div")
add_text = (By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/a")
all_trash_icons = (By.XPATH, "//*[@id='text-application-accordion']/li/div/a")
click_yes_delete_dropdown = (By.XPATH, "//*[@id='confirmation-modal']/div/div/div[2]/div/div[1]/button")
select_dropdown_text = (By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/select")
all_text_body_location_tn = (By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/label")
select_continue = (By.XPATH, "//*[@id='body-content']/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/button")
added_team_name_text = (By.XPATH, "//*[@id='text-application-accordion']/li/div[3]/ul[1]/li/div[1]/div[2]/div/input")
select_added_team_name_font_ = (By.XPATH, "//*[@id='text-application-accordion']/li/div[3]/ul[1]/li/div[2]/div[2]/div/a[2]")
team_name_tailsweep_location_add = (By.XPATH, "//*[@id='team-name-1-accordion-item-91']/div[3]/ul/li[3]/div/div[2]/div")
team_select_each_tailsweep_add = (By.XPATH, "//*[@id='team-name-1-accordion-item-91']/div[3]/ul/li[3]/div/div[2]/div/div")
select_font_accent_team_name_add = (By.XPATH, "//*[@class='uk-grid-small uk-child-width-1-6 con-font-accent uk-flex-middle uk-grid']/div/label")
team_name_location_add = (By.XPATH, "//*[@class='accordion accordion-size-large accordion-gap-none uk-accordion']/li[@class='application-item']/div/label")
default_toggle = (By.XPATH, "//*[@id='text-application-accordion']/li/div/label")

input_player_name_text = (By.XPATH, "//*[@placeholder='Player Name']")
font_accents_all_color = (By.XPATH, "//*[@class='uk-grid-small uk-child-width-auto con-color-palettes uk-flex-middle uk-width-1-1 uk-grid']/div/label")
previous_arrow_pl_add = (By.XPATH, "//*[@id='text-application-accordion']/li[2]/div[3]/ul/li[1]/div[2]/div[2]/div/a[2]")

class Customizer(BasePage):

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
        return self.wait_elements(click_all_first_elements)

    def click_picker(self):
        return self.wait_click_driver(click_wheel)

    def bagby_green_color(self):
        return self.wait_click_driver(click_bagby_green)

    def infantry_blue_color(self):
        return self.wait_click_driver(click_infantry_blue)

    def dessert_sand_color(self):
        return self.wait_click_driver(click_dessert_sand)

    def click_save(self):
        return self.wait_click_driver(save_colors_wheel)

    def click_body_colors(self):
        return self.wait_elements(body_colors)

    def click_brand_logo_drpdwn(self):
        return self.wait_driver(brand_logo_dropdown)

    def second_brand_logo_drpdwn(self):
        return self.wait_driver(second_brand_logo_dropdown)

    def click_brand_logo_color(self):
        return self.wait_elements(brand_logo_color)

    def click_second_brand_logo_color(self):
        return self.wait_elements(second_brand_logo_color)

    def first_brand_logo_text(self):
        return self.wait_driver(first_brand_logo_loc)

    def second_brand_logo_text(self):
        return self.wait_driver(second_brand_logo_text)

    def click_pattern_tab(self):
        return self.wait_driver(pattern_tab)

    def click_turn_on(self):
        return self.wait_driver(click_pattern)

    def click_axe_dazzle(self):
        return self.wait_click_driver(select_axe_dazzle)
    def pattern_layer1(self):
        return self.wait_elements(layer1_pattern)
    def pattern_layer2(self):
        return self.wait_elements(layer2_pattern)
    def slider(self):
        return self.wait_driver(pattern_slider)
    def click_text_tab(self):
        return self.wait_driver(text_tab)
    def dropdowns_list_text_tab(self):
        return self.wait_elements(drop_downs_text_tab)
    def team_name_dropdown(self):
        return self.wait_driver(click_first_dropdown)
    def team_name_text(self):
        return self.wait_driver(edit_team_name)
    def select_font(self):
        return self.wait_driver(font_styles)
    def select_font_layout(self):
        return self.wait_driver(font_layout)
    def tail_sweep_position(self):
        return self.wait_driver(tail_sweep_location)
    def tail_sweep_iteems(self):
        return self.wait_elements(tail_sweep_items)
    def font_accent_list(self):
        return self.wait_elements(font_accents)
    def base_colors_font_accent_team_name(self):
        return self.wait_elements(base_color_accents)
    def enable_other_body_location(self):
        return self.wait_elements(team_name_body_enable_default)
    def toggle_loc(self):
        return self.wait_elements(toggle_location)
    def enable_player_name_body(self):
        return self.wait_driver(player_name_body_enable_default)
    def edit_player_name_default(self):
        return self.wait_driver(player_name_text_field)
    def select_player_name_font(self):
        return self.wait_driver(select_player_name_font)
    def font_accent_location_player_name(self):
        return self.wait_driver(font_accent_location_player_name)
    def font_accent_list_player_name(self):
        return self.wait_elements(font_accent_player_name_items)
    def select_pl_name_base_color(self):
        return self.wait_elements(pl_name_base_color)
    def pattern_slider_body(self):
        return self.wait_driver(pattern_slider)
    def add_a_text(self):
        return self.wait_driver(add_text)
    def click_trashes(self):
        return self.wait_elements(all_trash_icons)
    def delete_all_dropdown(self):
        return self.wait_click_driver(click_yes_delete_dropdown)
    def select_text_application(self):
        return self.wait_driver(select_dropdown_text)
    def team_name_text_body_locations(self):
        return self.wait_driver(all_text_body_location_tn)
    def select_continue_btn(self):
        return self.wait_click_driver(select_continue)
    def team_name_front_body(self):
        return self.wait_driver(added_team_name_text)
    def team_name_font_add(self):
        return self.wait_driver(select_added_team_name_font_)
    def position_of_tailsweep_team_name(self):
        return self.wait_driver(team_name_tailsweep_location_add)
    def team_name_tailsweep_select(self):
        return self.wait_elements(team_select_each_tailsweep_add)
    def team_name_font_accent_add(self):
        return self.wait_elements(select_font_accent_team_name_add)
    def team_name_locations_text_add(self):
        return self.wait_elements(team_name_location_add)

    def player_name_text_body(self):
        return self.wait_driver(input_player_name_text)
    def default_toggles(self):
        return self.wait_elements(default_toggle)
    def all_color_font_accent(self):
        return self.wait_elements(font_accents_all_color)
    def previous_arrow_add_pl(self):
        return self.wait_driver(previous_arrow_pl_add)






