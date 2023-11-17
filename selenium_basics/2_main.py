from selenium import webdriver
from selenium.webdriver.common.by import By
from components.base import Base


driver = webdriver.Chrome
base = Base(driver)

print(dir(base))

