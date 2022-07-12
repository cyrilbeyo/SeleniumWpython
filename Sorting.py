import time
from selenium import webdriver
from sortedcontainers import SortedList
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())


#collect all veggies list Browser_sortedlist
#Sort Browser_sortedlist = BrowserSortedList
#assert Browser_sortedlist == SortedList

driver.implicitly_wait(20)


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")


driver.find_element_by_xpath("//a[contains(text(), 'Top Deals')]").click() #top deals

childwindow = driver.window_handles[1]

driver.switch_to.window(childwindow)



#click on column header
driver.find_element(By.XPATH"//span[contains(text(), 'Veg/fruit name')]").click()


#Sort Browser_sortedlist = BrowserSortedList
Browser_sortedlist = []

veggies = driver.find_elements(By.XPATH, "//tr/td[1]")

for veggie in veggies:
    Browser_sortedlist.append(veggie.text)

Sorted_list = Browser_sortedlist.sort()

assert Sorted_list == Browser_sortedlist

time.sleep(10)
    











