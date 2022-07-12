"""
1.verify products in page 1 are in page 2
2.price decreases after discount/promo

3. sum of products in checkout matches the total amount
4.verrify search functionality afte inputting keys 
"""

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(7)


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")

cart_btn = driver.find_element_by_xpath("(//div[@class='product-action']/button)[1]").click()






for add_btn in add_cart:
    
    add_btn.click()

driver.find_element_by_css_selector("img[alt='Cart']")

driver.find_element_by_xpath("(//button[@type='button'])[contains(text(), 'PROCEED TO CHECKOUT')]").click()

driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")


driver.find_element_by_css_selector("button.promoBtn").click()








