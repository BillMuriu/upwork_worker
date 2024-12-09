import time
import random
from seleniumbase import SB

with SB(uc=True) as sb:
    print("Opening ChatGPT...")
    sb.driver.uc_open_with_reconnect("https://www.upwork.com/", 10)
    sb.wait_for_element_visible('.up-n-link.nav-item.login-link.d-none.d-md-block.px-6x')
    time.sleep(random.uniform(2, 10))
    sb.click('.up-n-link.nav-item.login-link.d-none.d-md-block.px-6x')
    sb.wait_for_element_visible('#login_google_submit')
    time.sleep(random.uniform(2, 7))
    sb.click('#login_google_submit')
    sb.wait_for_element_visible("input#identifierId")
    time.sleep(random.uniform(2, 5))
    sb.press_keys("input#identifierId", "njorogekamau63@gmail.com")
    sb.wait_for_element_visible('button:contains("Next")')
    time.sleep(random.uniform(1, 5))
    sb.click('button:contains("Next")')
    sb.wait_for_element_visible('input[name="Passwd"]')
    time.sleep(random.uniform(2, 5))
    sb.press_keys('input[name="Passwd"]', "Billbill98*")
    sb.wait_for_element_visible('button:contains("Next")')
    time.sleep(random.uniform(2, 5))
    sb.click('button:contains("Next")')
    time.sleep(20)
    window_handles = sb.driver.window_handles
    sb.driver.switch_to.window(window_handles[0])  
    sb.open('https://www.upwork.com/nx/search/talent/?nbs=1&q=Data%20Analyst&revenue=10000')
    time.sleep(5)
    page_source = sb.get_page_source()
    print(page_source)
    with open("upwork_page_source.html", "w", encoding="utf-8") as file:
        file.write(page_source)
    sb.sleep(10)
    print("Logged into upwork.")
