from selenium import webdriver
from selenium.webdriver.common.by import By

class Homepage:
    search_input_id = "cb1-edit"
    search_icon_xpath = "//*[contains(@aria-label,'Buscar')]"
    new_filter_xpath = "//button[contains(@aria-label,'Nuevo')]"
    old_filter_xpath = "//button[contains(@aria-label,'Usado')]"
    products_result_class = "ui-search-layout__item"

    def __init__(self, driver):
        self.driver = driver

    def searchKeyword(self):
        search_textbox = self.driver.find_element(By.ID, self.search_input_id)
        search_textbox.clear()
        search_textbox.send_keys("iPhone")
        self.driver.find_element(By.XPATH, self.search_icon_xpath).click()

    def filterConditionNew(self):
        self.driver.find_element(By.XPATH, self.new_filter_xpath).click()

    def filterConditionOld(self):
        self.driver.find_element(By.XPATH, self.old_filter_xpath).click()

    def countProducts(self):
        count = self.driver.find_elements(By.CLASS_NAME, self.products_result_class)
        return len(count)

