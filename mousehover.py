#On rahul shetty academy practice page
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

Btn = driver.find_element_by_css_selector("button[id='mousehover']")

action = ActionChains(driver)

action.move_to_element(Btn).perform()

action.move_to_element(driver.find_element_by_link_text("Reload")).click().perform()

# time.sleep(10)