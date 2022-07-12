from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(ChromeDriverManager().install())
"""
Login to the Edureka
Navigate to ‘My Profile’

Update professional and personal details

Explore the blogs and navigate to the Main page

Logout of the portal

NOTE: Make sure that you are logged out of Edureka’s website while performing this practical.
"""


