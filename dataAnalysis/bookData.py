#from selenium import webdriver
#from selenium.webdriver import By
import pandas as pd

''' The goal of this script is to scrape the internet for data on different books.
    Data should include sales, reception, and ideological trends of the book'''

# Scrape webpages for data
#driver = webdriver.Chrome()
#driver.get()

prh = pd.read_json("penguinRandomHouse.json")
prh.append("Test")
