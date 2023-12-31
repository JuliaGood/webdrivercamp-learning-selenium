from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Create a new instance of the Chrome driver (Open Browser)
driver = webdriver.Chrome()

# Open the website (Navigate to URL)
url = "https://www.ebay.com/"
driver.get(url)

print('Waiting for the page to load...')

# WebDriverWait - Waiting for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.title_contains("eBay"))
# wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Print URL
print("Current URL:", driver.current_url)

# Find the search field by XPATH
search_field = driver.find_element(By.XPATH, '//input[@id="gh-ac"]')

# Wait for the search field to be clickable
wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="gh-ac"]')))

# Type "women watch" into the search field
search_field.send_keys("women watch")

# Press Enter to perform the search
search_field.send_keys(Keys.RETURN)

# Verify the header contains “results for women watch“
header_xpath = '//div[@id="mainContent"]//h1[@class="srp-controls__count-heading"]'
header_element = driver.find_element(By.XPATH, header_xpath)
wait.until(EC.visibility_of_element_located((By.XPATH, header_xpath)))

expected_text = "results for women watch"
header_text = header_element.text
assert expected_text in header_text
print(f"Expected header text: '{expected_text}', Actual text: '{header_text}'")
print("Verify the header contains “results for women watch“")
time.sleep(5)

# Close the browser window
driver.quit()
