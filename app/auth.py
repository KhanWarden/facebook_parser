import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv


load_dotenv()


cService = webdriver.ChromeService(executable_path='chromedrivers/chromedriver-win64/chromedriver')
driver = webdriver.Chrome(service=cService)

driver.get("https://www.facebook.com/")

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")


def authorization():
    email_elem = driver.find_element(By.ID, "email")  # Locate by ID
    email_elem.send_keys(login)

    password_elem = driver.find_element(By.ID, "pass")  # Locate by ID
    password_elem.send_keys(password)

    password_elem.send_keys(Keys.RETURN)
    time.sleep(10)

driver.get("https://web.facebook.com/meirambek.zhaparov")
time.sleep(5)  # Wait for page to load completely

# Locate the div by `data-pagelet` attribute
data_pagelet_value = "TimelineFeedUnit_0"  # Replace with the desired data-pagelet value
try:
    # Wait until the data-pagelet element is present
    data_pagelet_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, f'div[data-pagelet="{data_pagelet_value}"]'))
    )

    # Use JavaScript to get all inner text within this data-pagelet div, including deeply nested elements
    text_content = driver.execute_script(
        "return arguments[0].innerText;", data_pagelet_div
    )

    # Print or process the extracted text content
    print("Found content in data-pagelet:", data_pagelet_value)
    print(text_content)  # Output the entire text content

except Exception as e:
    print("Could not find content:", e)

# Close the driver
driver.quit()
