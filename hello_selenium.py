#!/usr/bin/env python3

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


class App:
    def __init__(self, email="", password=""):
        self.email = os.getenv("email")
        self.password = os.getenv("password")
        self.driver = webdriver.Chrome(
            service=ChromiumService(ChromeDriverManager().install())
        )
        self.main_url = "https://www.facebook.com"
        self.driver.get(self.main_url)
        self.log_in()
        # self.used_item_links = []
        # self.scrape_item_links()
        # self.scrape_item_details()
        self.driver.quit()

    def log_in(self):
        try:
            email_input = self.driver.find_element("id", "email")
            email_input.send_keys(self.email)
            sleep(0.5)
            password_input = self.driver.find_element("id", "pass")
            password_input.send_keys(self.password)
            sleep(0.5)
            login_button = self.driver.find_element(
                By.XPATH,
                "//*[@type='submit']",
            )
            login_button.click()

            sleep(30)
        except Exception:
            print("Ops, algo salio mal prro")
            sleep(10)

    # def scrape_item_links(self):


# marketplace_button = self.driver.find_element_by_xpath()

load_dotenv()
App()
