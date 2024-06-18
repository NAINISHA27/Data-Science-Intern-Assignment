from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Configuration
website_url = 'https://www.wikipedia.org/'
username = 'your_username'
password = 'your_password'
login_page_title = 'Login - Example'
login_page_url = 'https://example.com/login'
chrome_driver_path = r'C:\path\to\chromedriver.exe'  # Update this path

# Initialize WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

def login_to_website(driver, website_url, username, password):
    try:
        driver.get(website_url)
        
        # Wait for the login page to load
        WebDriverWait(driver, 20).until(EC.title_contains(login_page_title))
        
        # Locate and fill the username field
        username_field = driver.find_element(By.NAME, 'username')
        username_field.send_keys(username)
        
        # Locate and fill the password field
        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys(password)
        
        # Locate and click the login button
        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()
        
        # Handle potential login issues like incorrect password alerts
        WebDriverWait(driver, 20).until(EC.url_changes(login_page_url))
        
        return True
    except Exception as e:
        print("Login failed:", e)
        driver.quit()
        return False

def extract_data(driver):
    data = []
    
    try:
        # Example: Navigate to a specific page after login
        data_page_url = 'https://example.com/data-page'
        driver.get(data_page_url)
        
        # Wait for the data page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="data-container"]')))
        
        # Extract data
        items = driver.find_elements(By.XPATH, '//div[@class="data-item"]')
        for item in items:
            try:
                title = item.find_element(By.XPATH, './/h2').text
                description = item.find_element(By.XPATH, './/p').text
                data.append({"Title": title, "Description": description})
            except Exception as e:
                print("Error extracting data:", e)
                continue
    except Exception as e:
        print("Failed to navigate to data page:", e)
    
    return data

# Perform login and extract data
if login_to_website(driver, website_url, username, password):
    print("Login successful")
    data = extract_data(driver)
    driver.quit()
    
    # Save data to CSV
    if data:
        df = pd.DataFrame(data)
        df.to_csv('extracted_data.csv', index=False)
        print("Data saved to extracted_data.csv")
    else:
        print("No data extracted")
else:
    print("Login failed")
