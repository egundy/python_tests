from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle as pk
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://twitter.com/i/flow/login")
driver.implicitly_wait(5)

username_box = driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
username_box.click()
driver.send_keys("evangunderson3")
driver.close()
