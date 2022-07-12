from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

# import time


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")


h3 = driver.find_element_by_css_selector("div.example > h3")

print(h3.text)

click_here = driver.find_element_by_xpath("//a[contains(text(),'Click Here')]")

click_here.click()



childwindow = driver.window_handles[1]


driver.switch_to.window(childwindow)

print(driver.find_element_by_xpath("//h3[contains(text(),'New Window')]").text)



