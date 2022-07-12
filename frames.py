from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe") #Heroku app


driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='mce_0_ifr']"))

driver.find_element_by_css_selector("#tinymce").clear()

driver.find_element_by_css_selector("#tinymce").send_keys("Happy To Automate")


time.sleep(10)



 