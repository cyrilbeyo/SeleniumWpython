from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(20)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#scrolling
#
driver.execute_script("window.scrollBy(0,1300)")

time.sleep(10)
