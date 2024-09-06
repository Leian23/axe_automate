from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.builder_customizer import Customizer
from Utilities.baseclass import BaseClass
from Assets.credentials import green_color, reset_color, blue_color, email_qx7, password_qx7
import random
import time


class TestBuilder(BaseClass):

    def test_select_fabric_drpdwn(self):
        item2 = Customizer(self.driver)
        item2.fabric_dropdown().click()
        time.sleep(2)
        item2.zoom_fabric().click()
        print(green_color + "Zoom fabric dropdown has been selected" + reset_color)
        time.sleep(2)
        item2.close_modal_fabric().click()
        print(green_color + "Close fabric dropdown has been selected" + reset_color)
        assert item2.load_fabric_image(), "Fabric image not loaded"
        print(green_color + "Fabric image loaded" + reset_color)

    def test_colors_tab(self):
        item2 = Customizer(self.driver)
        time.sleep(1)
        self.bottom_thumbnails()

        self.scroll_into_view(item2.colors_tab())
        item2.colors_tab().click()

        time.sleep(2)
        select_first_color = item2.click_first_color()

        for items in select_first_color:
            items.click()
            time.sleep(0.3)

        time.sleep(1)
        self.bottom_thumbnails()
        time.sleep(2)
        color_picker = item2.click_picker()
        self.driver.execute_script("arguments[0].scrollIntoView();", color_picker)
        color_picker.click()

        time.sleep(1)
        item2.bagby_green_color().click()
        item2.infantry_blue_color().click()
        item2.dessert_sand_color().click()
        item2.click_save().click()

        time.sleep(2)

        select_body_color = item2.click_body_colors()

        interval = 6

        for i, item in enumerate(select_body_color):
            item.click()
            time.sleep(0.2)

            if (i + 1) % interval == 0:
                random_choice = random.choice(select_body_color[i - interval + 1:i + 1])
                random_choice.click()
                time.sleep(0.2)

        time.sleep(1)
        self.bottom_thumbnails()

        time.sleep(2)
        brand_logo_drpdwn = item2.click_brand_logo_drpdwn()
        self.driver.execute_script("arguments[0].scrollIntoView();", brand_logo_drpdwn)
        brand_logo_drpdwn.click()

        time.sleep(2)

        print(
            green_color + f"You have acccessed the first brand logo location {item2.first_brand_logo_text().text}" + blue_color)

        brand_logo_col = item2.click_brand_logo_color()

        time.sleep(2)

        # brand logo color
        for items9 in brand_logo_col:
            items9.click()
            time.sleep(0.2)

        if brand_logo_col:
            random_choice = random.choice(brand_logo_col)
            random_choice.click()
        time.sleep(2)
        brand_logo_drpdwn.click()

        time.sleep(2)

        #click the second dropdown logo

        second_dropdown = item2.second_brand_logo_drpdwn()
        self.driver.execute_script("arguments[0].scrollIntoView();", second_dropdown)
        second_dropdown.click()

        print(
            green_color + f"You have acccessed the second brand logo location {item2.second_brand_logo_text().text}" + blue_color)

        brand2_logo_col = item2.click_second_brand_logo_color()

        time.sleep(2)

        # brand logo color
        for items10 in brand2_logo_col:
            items10.click()
            time.sleep(0.2)

        if brand2_logo_col:
            random_choice = random.choice(brand2_logo_col)
            random_choice.click()
        time.sleep(2)
        second_dropdown.click()

    def test_pattern_tab(self):
        item2 = Customizer(self.driver)
        item2.click_pattern_tab().click()
        time.sleep(2)
        item2.click_turn_on().click()
        time.sleep(2)
        item2.click_axe_dazzle().click()
        time.sleep(5)

        colors_layer1 = item2.pattern_layer1()
        colors_layer2 = item2.pattern_layer2()

        for items11 in colors_layer1:
            items11.click()
            time.sleep(0.2)

        if colors_layer1:
            random_choice = random.choice(colors_layer1)
            random_choice.click()

        time.sleep(2)

        for items12 in colors_layer2:
            items12.click()
            time.sleep(0.2)

        if colors_layer2:
            random_choice = random.choice(colors_layer2)
            random_choice.click()
        time.sleep(3)

        pattern_slide = item2.pattern_slider_body()
        actions = ActionChains(self.driver)
        actions.click_and_hold(pattern_slide).move_by_offset(170, 0).release().perform()
        self.bottom_thumbnails()
        time.sleep(1)

    def test_text_tab(self):
        item2 = Customizer(self.driver)
        item2.click_text_tab().click()

        default_texes = item2.dropdowns_list_text_tab()
        actions = ActionChains(self.driver)

        #dropdowns
        team_name_drpdwn = item2.team_name_dropdown()

        if default_texes:
            for item in default_texes:
                print(blue_color + "The default texes are not null, starting default text configurations")
                print(item.text)

                if item.text.lower() == "team name":
                    tn = item2.team_name_dropdown()

                    time.sleep(2)
                    tn.click()
                    item2.team_name_text().send_keys(" Sample")
                    time.sleep(2)
                    element = item2.select_font()
                    #element2 = item2.select_font_layout()
                    actions.double_click(element).perform()
                    actions.double_click(element).perform()
                    time.sleep(2)
                    #actions.double_click(element2).perform()
                    #actions.double_click(element2).perform()
                    tailsweep_position = item2.tail_sweep_position()
                    self.driver.execute_script("arguments[0].scrollIntoView();", tailsweep_position)

                    tailsweep_items_all = item2.tail_sweep_iteems()
                    select_font_accent = item2.font_accent_list()
                    team_name_enable_location = item2.enable_other_body_location()
                    time.sleep(2)

                    for tailsweeps in tailsweep_items_all:
                        tailsweeps.click()
                        time.sleep(2)

                    interval = 6

                    for i, fontaccents in enumerate(select_font_accent):
                        fontaccents.click()
                        time.sleep(0.8)

                        if (i + 1) % interval == 0:
                            random_choice = random.choice(select_font_accent[i - interval + 1:i + 1])
                            random_choice.click()
                            time.sleep(0.2)

                    base_color = item2.base_colors_font_accent_team_name()

                    for i, item in enumerate(base_color):
                        item.click()
                        time.sleep(0.2)

                        if (i + 1) % interval == 0:
                            random_choice = random.choice(base_color[i - interval + 1:i + 1])
                            random_choice.click()
                            time.sleep(0.2)

                    for enable_other_location in team_name_enable_location:
                        enable = enable_other_location
                        self.driver.execute_script("arguments[0].scrollIntoView();", enable)
                        enable.click()
                        time.sleep(1)

                    time.sleep(1)
                    self.driver.execute_script("arguments[0].scrollIntoView();", tn)

                elif item.text.lower() == "player name":

                    pn = item2.enable_player_name_body()

                    time.sleep(2)
                    pn.click()
                    item2.edit_player_name_default().send_keys(" Test")
                    time.sleep(2)
                    element3 = item2.select_player_name_font()

                    actions.double_click(element3).perform()
                    actions.double_click(element3).perform()
                    time.sleep(2)
                    font_accents_loc = item2.font_accent_location_player_name()
                    self.driver.execute_script("arguments[0].scrollIntoView();", font_accents_loc)
                    font_accents_loc.click()
                    time.sleep(1)

                    select_font_accent_pl_name = item2.font_accent_list_player_name()
                    interval = 6

                    for i, font_accents_pl_name in enumerate(select_font_accent_pl_name):
                        font_accents_pl_name.click()
                        time.sleep(0.8)

                        if (i + 1) % interval == 0:
                            random_choice = random.choice(select_font_accent_pl_name[i - interval + 1:i + 1])
                            random_choice.click()
                            time.sleep(0.2)

                    base_colors_pl = item2.select_pl_name_base_color()

                    for i, pl_name_base in enumerate(base_colors_pl):
                        pl_name_base.click()
                        time.sleep(0.2)

                        if (i + 1) % interval == 0:
                            random_choice = random.choice(base_colors_pl[i - interval + 1:i + 1])
                            random_choice.click()
                            time.sleep(0.2)

                    time.sleep(1)

        time.sleep(1)

        #start deleting the default texes
        all_trashes = item2.click_trashes()

        for icon in all_trashes:
            self.driver.execute_script("arguments[0].scrollIntoView();", icon)
            icon.click()
            time.sleep(0.8)
            item2.delete_all_dropdown().click()

        #start adding text on team name
        item2.add_a_text().click()
        time.sleep(1)

        text_applications = Select(item2.select_text_application())

        for text_app in text_applications.options:
            print(text_app.text)

            if (text_app.text.lower() == "team name"):
                text_app.click()
                time.sleep(2)

                all_text_body_location_tn = item2.team_name_text_body_locations()

                all_text_body_location_tn.click()
                time.sleep(0.2)
                item2.select_continue_btn().click()
                item2.team_name_front_body().send_keys("Testing")
                time.sleep(2)
                element4 = item2.team_name_font_add()
                actions.double_click(element4).perform()
                actions.double_click(element4).perform()
                self.driver.execute_script("arguments[0].scrollIntoView();",
                                           item2.position_of_tailsweep_team_name())
                tailsweeps_added_team_name = item2.team_name_tailsweep_select()

                time.sleep(1)
                for tn_tailsweep in tailsweeps_added_team_name:
                    tn_tailsweep.click()
                    time.sleep(1.7)

                #tn_font_accents = item2.team_name_font_accent_add()
                #time.sleep(1)

                #for tn_accent in tn_font_accents:
                #tn_accent.click()
                #time.sleep(0.8)


                enable_team_name_location_add = item2.team_name_locations_text_add()
                time.sleep(2)


                for tn_toggle in enable_team_name_location_add:
                    enable_tn = tn_toggle
                    self.driver.execute_script("arguments[0].scrollIntoView();", enable_tn)
                    enable_tn.click()
                    time.sleep(1)
                break

    #--------------------------------------------------------------------

    def bottom_thumbnails(self):
        item2 = Customizer(self.driver)
        self.scroll_into_view(item2.second_image())
        item2.second_image().click()
        time.sleep(0.8)

        self.scroll_into_view(item2.third_image())
        item2.third_image().click()
        time.sleep(0.8)

        self.scroll_into_view(item2.fourth_image())
        item2.fourth_image().click()
        time.sleep(0.8)

        self.scroll_into_view(item2.first_image())
        item2.first_image().click()

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
