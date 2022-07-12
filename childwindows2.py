from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")


heading1 = driver.find_element_by_xpath("//h3[contains(text(), 'Opening a new window')]")


driver.find_element_by_link_text("").click()

parentwindow = driver.window_handles[0]
childwindow = driver.window_handles[1]


driver.switch_to.window(childwindow)

heading_in_childw = driver.find_element_by_css_selector("div.example > h3")


assert heading_in_childw.text == "New Window"

sleep(20)









