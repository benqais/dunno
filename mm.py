import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def automate_action():
    # Initialize Chrome webdriver
    driver = webdriver.Chrome()
    
    # Navigate to the website
    driver.get('https://tikfollowers.com/tiktok-free-followers')
    time.sleep(5)
    
    try:
        # Type the username
        username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@class='form-control un']")))
        username_field.send_keys('freefirenpc')
        
        # Click the "Find Account" button
        find_account_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-block') and contains(@class, 'solid-btn') and contains(@class, 'border-radius') and contains(@class, 'mt-4') and contains(@class, 'mb-3') and contains(@class, 'submit')]")))
        find_account_button.click()
        
        # Wait for 20 seconds
        time.sleep(20)
        
        # Click the "Send Followers" button
        send_followers_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-block') and contains(@class, 'solid-btn') and contains(@class, 'border-radius') and contains(@class, 'mt-4') and contains(@class, 'mb-3') and contains(@class, 'submit')]")))
        send_followers_button.click()
        
        # Wait for 60 seconds
        time.sleep(60)
        
    except Exception as e:
        # Handle the exception (print the error message, log it, etc.)
        print(f"An error occurred: {str(e)}")
        
        # Close the browser
        driver.quit()
        
        # Restart the task by calling automate_action() again
        automate_action()
        
    finally:
        # Close the browser
        driver.quit()

# Automate the action
while True:
    automate_action()
    
    # Wait for 16 minutes
    time.sleep(960)
