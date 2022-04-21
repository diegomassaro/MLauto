from selenium import webdriver
from selenium.webdriver.common.by import By

class Landing:
    link_bolivia_id = "BO"

    def __init__(self, driver):
        self.driver = driver

    def clickCountry(self):
        self.driver.find_element(By.ID, self.link_bolivia_id).click()
