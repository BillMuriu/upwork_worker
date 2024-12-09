import time
import random
from seleniumbase import BaseCase
from seleniumbase import Driver

class UndetectedLoginToChatGPT(BaseCase):

    def test_google_login(self):
        # Create the driver in undetected Chrome mode
        driver = Driver(uc=True)

        # URL of the site you want to log in to
        url = "https://chatgpt.com"
        driver.uc_open_with_reconnect(url, 3)  # Open the URL with undetected Chrome mode

        # Wait for the login button to be visible and click it
        driver.wait_for_element_visible('button[data-testid="login-button"]')
        time.sleep(random.uniform(2, 5))  # Random delay between 1 and 2 seconds
        driver.click('button[data-testid="login-button"]')
        
        # Wait for the email input field and enter the email
        driver.wait_for_element_visible('#notion-email-input-2')
        time.sleep(random.uniform(3, 7))  # Random delay between 1 and 2 seconds
        driver.press_keys('#notion-email-input-2', 'laureenchristina@gmail.com')

        # Wait for the Google identifier input field and enter the email again
        driver.wait_for_element_visible("input#identifierId")
        time.sleep(random.uniform(2, 5))  # Random delay between 1 and 2 seconds
        driver.press_keys("input#identifierId", "laureenchristina@gmail.com")
        
        # Click "Next" button
        driver.wait_for_element_visible('button:contains("Next")')
        time.sleep(random.uniform(1, 5))  # Random delay between 1 and 2 seconds
        driver.click('button:contains("Next")')

        # Wait and enter the password
        driver.wait_for_element_visible('input[name="Passwd"]')
        time.sleep(random.uniform(3, 7))  # Random delay between 1 and 2 seconds
        driver.press_keys('input[name="Passwd"]', "Billbill98*")

        # Click "Next" again
        driver.wait_for_element_visible('button:contains("Next")')
        time.sleep(random.uniform(2, 5))  # Random delay between 1 and 2 seconds
        driver.click('button:contains("Next")')

        # Add a final wait to ensure the page is loaded
        time.sleep(random.uniform(3, 5))  # Random final delay

     # the login steps for notion
     # the login steps for notion
        driver.wait_for_element('/html/body/div/div/div[1]/div/div/main/div[1]/section/div/div/div/div[2]/div[1]/div[1]/div[1]/div')
        driver.click('/html/body/div/div/div[1]/div/div/main/div[1]/section/div/div/div/div[2]/div[1]/div[1]/div[1]/div')
        

        window_handles = driver.window_handles
        print("Window Handles:", window_handles)
        driver.switch_to.window(window_handles[1])

        driver.type("//input[@id='identifierId']", "...")
        driver.click("#identifierNext")
        
        driver.wait_for_element_visible("[aria-label='Enter your password']")
        driver.type("[aria-label='Enter your password']", "...")
        driver.click("#passwordNext")

        print("You should be logged in to your Notion By Now!")