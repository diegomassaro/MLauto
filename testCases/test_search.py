from selenium import webdriver
from pageObjects.LandingPage import *
from pageObjects.HomePage import *

class Test_001_Search_and_filter:
    baseURL = "https://mercadolibre.com/"
    text = "iPhone"

    def test_searchNewFilter(self):
        self.driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = Landing(self.driver)
        self.lp.clickCountry()

        self.home = Homepage(self.driver)
        self.home.searchKeyword()
        self.home.filterConditionNew()

        count = self.home.countProducts()
        self.driver.quit()
        if count >= 3:
            assert True
        else:
            assert False

    def test_searchOldFilter(self):
        self.driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = Landing(self.driver)
        self.lp.clickCountry()

        self.home = Homepage(self.driver)
        self.home.searchKeyword()
        self.home.filterConditionOld()

        count = self.home.countProducts()
        self.driver.quit()
        if count >= 3:
            assert True
        else:
            assert False



