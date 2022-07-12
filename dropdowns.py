
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/dropdown") #Heroku app


dropdowns = Select(driver.find_element_by_css_selector("select[id='dropdown']"))

dropdowns.select_by_value('1')


dropdown1= driver.find_element_by_xpath("//option[contains(text(), 'Option 1')]")

assert dropdown1.is_selected() 