import time
import random
from seleniumbase import SB

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

        # Wait for the page to load completely
        print("Waiting for the page to load completely...")
        time.sleep(random.uniform(3, 7))

        # Wait for the pagination element to be visible before extracting the page count
        sb.wait_for_element_visible('li.air3-pagination-nr .air3-pagination-nr-btn.is-active span.sr-only')
        page_info = sb.find_element('li.air3-pagination-nr .air3-pagination-nr-btn.is-active span.sr-only').text
        total_pages = int(page_info.split()[-1])  # Extract the total number of pages

        print(f"Total pages to scrape: {total_pages}")

        # Loop through all the pages and scrape data
        for page_number in range(1, total_pages + 1):
            print(f"Scraping page {page_number} of {total_pages}...")

            # Save the page source for the current page
            page_source = sb.get_page_source()
            with open(f"upwork_page_source_page_{page_number}.html", "w", encoding="utf-8") as file:
                file.write(page_source)

           # Wait for the completed jobs container to be visible
            sb.wait_for_element_visible("//div[@id='jobs_completed_desktop']")
            print("The completed jobs container is visible.")

            # Find all job cards within the completed jobs container
            job_elements = sb.find_elements(
                'div#jobs_completed_desktop div.assignments-item.assignments-item-hoverable.air3-card-section.py-0.legacy'
            )
            # Print how many elements have been found
            print(f"Found {len(job_elements)} job elements.")


            if not job_elements:
                print("No job elements found. Double-check your CSS selectors or ensure the page is fully loaded.")
            else:
                print(f"Found {len(job_elements)} job elements.")
                for index, job_element in enumerate(job_elements):
                    try:
                        print(f"Processing job {index + 1}...")

                        # Locate the <a> tag within the current job card using the index
                        job_selector = f'div#jobs_completed_desktop div.assignments-item.assignments-item-hoverable.air3-card-section.py-0.legacy:nth-of-type({index + 1}) a.up-n-link.cursor-pointer.no-underline[tabindex="0"]'

                        # Click the <a> tag to open the modal
                        sb.click(job_selector)
                        print(f"Clicked on job {index + 1}")


                        # Wait for the modal to appear
                        sb.wait_for_element_visible('div.air3-modal-content')

                        sb.sleep(1)
                        modal_content = sb.get_element('div.air3-modal-content').get_attribute("innerHTML")
                        modal_filename = f"page_{page_number}_job_{index + 1}_modal.html"
                        
                        # Save modal content to a file
                        with open(modal_filename, "w", encoding="utf-8") as modal_file:
                            modal_file.write(modal_content)
                            print(f"Saved modal content to {modal_filename}")

                        # Close the modal
                        sb.click('button[data-ev-label="modal_close"]')
                        sb.sleep(random.uniform(1, 3))  # Random wait to avoid detection
                    except Exception as e:
                        print(f"Error processing job {index + 1}: {e}")
                        continue  # Skip any jobs that cause an error

            # If not on the last page, click the next page button
            if page_number < total_pages:
                next_page_button_selector = f'//button[@data-ev-page_index="{page_number + 1}"]'
                sb.click(next_page_button_selector)

                time.sleep(random.uniform(3, 7))  # Wait for the page to load before scraping the next one

        print("Finished scraping all pages and modals.")

# Entry point for the script
if __name__ == "__main__":
    login_and_scrape()
