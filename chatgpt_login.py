import time
import random
from seleniumbase import SB

# Use the SB context manager for undetected Chrome and session handling
with SB(uc=True) as sb:
    print("Opening ChatGPT...")
    
    # Open the URL
    sb.driver.uc_open_with_reconnect("https://chatgpt.com", 10)

    # Wait for the login button and click
    sb.wait_for_element_visible('button[data-testid="login-button"]')
    time.sleep(random.uniform(2, 5))
    sb.click('button[data-testid="login-button"]')

    # Wait for the Google login button and proceed
    sb.wait_for_element_visible('button:contains("Continue with Google")')
    time.sleep(random.uniform(2, 5))
    sb.click('button:contains("Continue with Google")')

    # Input credentials when prompted
    sb.wait_for_element_visible("input#identifierId")
    time.sleep(random.uniform(2, 5))
    sb.press_keys("input#identifierId", "njorogekamau63@gmail.com")

    # Click "Next"
    sb.wait_for_element_visible('button:contains("Next")')
    time.sleep(random.uniform(1, 5))
    sb.click('button:contains("Next")')

    # Input password
    sb.wait_for_element_visible('input[name="Passwd"]')
    time.sleep(random.uniform(2, 5))
    sb.press_keys('input[name="Passwd"]', "Billbill98*")

    # Click "Next"
    sb.wait_for_element_visible('button:contains("Next")')
    time.sleep(random.uniform(2, 5))
    sb.click('button:contains("Next")')

    sb.sleep(10)
    sb.press_keys('div#prompt-textarea', "Hey there")
    sb.save_cookies(name="cookies.txt")
    sb.sleep(5)

    url2 = 'https://chatgpt.com/c/674a3d4f-b378-800f-9c32-794cceec1327'
    sb.open(url2)

    # Wait for login to complete
    time.sleep(10)
    print("Logged into the dashboard.")
