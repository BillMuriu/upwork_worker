import time
import random
from seleniumbase import SB
from bs4 import BeautifulSoup
import csv


# Function to handle the initial scraping & save data from multiple pages
# Function to handle the initial scraping & save data from multiple pages
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
        
       # Loop through pagination from page=1 to page=4
        output_csv = "job_links.csv"

# Initialize CSV file with headers
        with open(output_csv, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Page Number", "Job Link"])

        # Loop through pagination from page=1 to page=4
        for page_num in range(0, 5):
            url = f'https://www.upwork.com/nx/search/jobs/?q=n8n&page={page_num}&per_page=50'
            print(f"Visiting page {page_num}...")
            sb.open(url)
            time.sleep(random.uniform(7, 12))  # Sleep between 7 to 12 seconds before scraping the next page
            page_source = sb.get_page_source()

            # Save the page source to a unique file for each page
            file_name = f"upwork_page_source_{page_num}.html"
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(page_source)

            # Parse the page source and extract href values
            soup = BeautifulSoup(page_source, "html.parser")
            links = []
            for a_tag in soup.find_all("a", class_="air3-link", attrs={"data-test": "job-tile-title-link UpLink"}):
                href = a_tag.get("href")
                if href:
                    # Prepend the base URL if necessary
                    links.append(f"https://www.upwork.com{href}" if href.startswith("/") else href)

            # Save links to CSV file
            with open(output_csv, "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                for link in links:
                    writer.writerow([page_num, link])

            # Log the total number of links found on the page
            print(f"Page {page_num}: Extracted {len(links)} links.")

        print(f"All links have been saved to {output_csv}.")

# Run the full scraper sequence
if __name__ == "__main__":
    login_and_scrape()
