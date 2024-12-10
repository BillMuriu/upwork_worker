import time
import random
from seleniumbase import SB


# Define the login_and_scrape function
def login_and_scrape():
    with SB(uc=True) as sb:
        print("Opening Upwork...")
        sb.driver.uc_open_with_reconnect("https://www.upwork.com/", 10)

        # Login Steps
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

        # Navigate directly to the URL
        url = "https://www.upwork.com/freelancers/~0195e48a1102adba8d?referrer_url_path=/nx/search/talent/"
        print(f"Visiting URL: {url}")
        sb.open(url)
        time.sleep(random.uniform(7, 12))  # Sleep to allow the page to load

        # Wait for a few seconds before interacting with the element
        print("Waiting for the page to load completely...")
        time.sleep(random.uniform(3, 7))

        # Wait for and click on only the first matching element
        print("Waiting for the first matching element to be visible...")
        sb.wait_for_element_visible('h5[role="presentation"].align-items-center.mb-2x[data-v-6ba7fa90=""]:first-of-type')
        sb.click('h5[role="presentation"].align-items-center.mb-2x[data-v-6ba7fa90=""]:first-of-type')
        print("Clicked on the first matching element.")
        time.sleep(random.uniform(7, 8))

        # Save the source HTML
        page_source = sb.get_page_source()
        with open("upwork_page_source.html", "w", encoding="utf-8") as file:
            file.write(page_source)

        print(f"Processed URL: {url}.")


# Entry point for the script
if __name__ == "__main__":
    login_and_scrape()
