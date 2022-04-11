from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://google.com")
print(driver.title, "DRIVER TITLE")
driver.implicitly_wait(0.5)


search_box = driver.find_element(By.NAME, "q")
search_button = driver.find_element(By.NAME, "btnK")
search_box.send_keys("selenium")
search_button.click()
driver.find_element_by_name("q").get_attribute("value")

driver.close()