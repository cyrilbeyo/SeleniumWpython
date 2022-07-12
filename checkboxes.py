import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/checkboxes") #Heroku app
driver.maximize_window()

#selecting all checkboxes

checkboxes = driver.find_elements_by_css_selector("input[type='checkbox']")

for checkbox in checkboxes:
    checkbox.click()
    
checkbox1 = driver.find_element_by_xpath("(//input[@type='checkbox'])[1]")

assert checkbox1.is_selected()
#No errors