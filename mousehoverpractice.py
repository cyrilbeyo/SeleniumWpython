from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")



action = ActionChains(driver)

action.move_to_element(driver.find_element_by_xpath()).perform()

action.double_click().perform()