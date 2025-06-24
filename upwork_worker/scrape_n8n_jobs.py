import time
import random
import csv
from seleniumbase import SB

def login_to_upwork(sb):
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

def scrape_job_details(sb, url):
    try:
        print(f"Scraping job details from: {url}")
        sb.open(url)
        time.sleep(random.uniform(3, 5))

        # Dictionary to store job details
        job_data = {
            'url': url,
            'title': '',
            'posted_on': '',
            'location': '',
            'main_details': '',
            'description': '',
            'rates': ''
        }

        # Get Title
        try:
            print("Waiting for title element...")
            sb.wait_for_element_visible('h4.d-flex.align-items-center.mt-0.mb-5', timeout=10)
            title_element = sb.find_element('h4.d-flex.align-items-center.mt-0.mb-5')
            job_data['title'] = title_element.text
        except Exception as e:
            print(f"Error getting title: {e}")

        # Get Posted On
        try:
            posted_on_selector = "#main > div.container > div:nth-child(4) > div > div > div.job-details-card.d-flex.gap-0.air3-card.air3-card-outline.p-0 > div:nth-child(1) > section:nth-child(1) > div.d-flex.posted-on-line > div.text-light-on-muted.text-body-sm > div"
            print("Waiting for posted date element...")
            sb.wait_for_element_visible(posted_on_selector, timeout=10)
            posted_on_element = sb.find_element(posted_on_selector)
            job_data['posted_on'] = posted_on_element.text
        except Exception as e:
            print(f"Error getting posted date: {e}")

        # Get Location
        try:
            location_selector = "#main > div.container > div:nth-child(4) > div > div > div.job-details-card.d-flex.gap-0.air3-card.air3-card-outline.p-0 > div:nth-child(1) > section:nth-child(1) > div.d-flex.posted-on-line > div.d-inline-flex.align-items-center.text-base-sm > p"
            print("Waiting for location element...")
            sb.wait_for_element_visible(location_selector, timeout=10)
            location_element = sb.find_element(location_selector)
            job_data['location'] = location_element.text
        except Exception as e:
            print(f"Error getting location: {e}")

        # Get Main Details
        try:
            main_details_selector = "#main > div.container > div:nth-child(4) > div > div > div.job-details-card.d-flex.gap-0.air3-card.air3-card-outline.p-0 > div:nth-child(1) > section:nth-child(2) > div > p"
            print("Waiting for main details element...")
            sb.wait_for_element_visible(main_details_selector, timeout=10)
            main_details_element = sb.find_element(main_details_selector)
            job_data['main_details'] = main_details_element.text
        except Exception as e:
            print(f"Error getting main details: {e}")

        # Get Description
        try:
            description_selector = "#main > div.container > div:nth-child(4) > div > div > div.job-details-card.d-flex.gap-0.air3-card.air3-card-outline.p-0 > div:nth-child(1) > section:nth-child(2) > div"
            print("Waiting for description element...")
            sb.wait_for_element_visible(description_selector, timeout=10)
            description_element = sb.find_element(description_selector)
            job_data['description'] = description_element.text
        except Exception as e:
            print(f"Error getting description: {e}")

        # Get Rates
        try:
            rates_selector = "#main > div.container > div:nth-child(4) > div > div > div.job-details-card.d-flex.gap-0.air3-card.air3-card-outline.p-0 > div:nth-child(1) > section.air3-card-section.text-base-sm > ul > li:nth-child(4) > div.d-flex"
            print("Waiting for rates element...")
            sb.wait_for_element_visible(rates_selector, timeout=10)
            rates_element = sb.find_element(rates_selector)
            job_data['rates'] = rates_element.text
        except Exception as e:
            print(f"Error getting rates: {e}")

        return job_data
    except Exception as e:
        print(f"Error scraping job details: {e}")
        return None

def scrape_jobs(sb):
    # Navigate to the n8n jobs search URL
    base_url = "https://www.upwork.com/nx/search/jobs/?nbs=1&q=n8n&page=1&per_page=50"
    print(f"Visiting URL: {base_url}")
    sb.open(base_url)
    time.sleep(random.uniform(7, 12))  # Sleep to allow the page to load
    sb.driver.uc_gui_click_captcha()

    # Wait for the page to load completely
    print("Waiting for the search results to load...")
    time.sleep(random.uniform(3, 7))

    # Using the specific h2 class to find job links
    selector = 'h2.job-tile-title a'
    print(f"Looking for job links using selector: {selector}")

    try:
        sb.wait_for_element_visible(selector, timeout=10)
        job_links = sb.find_elements(selector)
        print(f"Found {len(job_links)} job links")
    except Exception as e:
        print(f"Error finding job links: {str(e)}")
        return []

    # Get the href attributes of all links
    job_urls = []
    for link in job_links:
        try:
            href = link.get_attribute('href')
            if href and 'jobs' in href:
                job_urls.append(href)
                print(f"Found job URL: {href}")
        except Exception as e:
            print(f"Error getting href: {str(e)}")
            continue

    print(f"Total job links collected: {len(job_urls)}")

    # Scrape details from first 3 jobs
    all_job_data = []
    for i, job_url in enumerate(job_urls[:3]):
        print(f"\nScraping job {i+1} of 3...")
        job_data = scrape_job_details(sb, job_url)
        if job_data:
            all_job_data.append(job_data)
        time.sleep(random.uniform(2, 4))  # Wait between jobs

    # Save to CSV
    if all_job_data:
        csv_filename = 'n8n_jobs.csv'
        fieldnames = ['url', 'title', 'posted_on', 'location', 'main_details', 'description', 'rates']
        
        print(f"\nSaving data to {csv_filename}...")
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_job_data)
        print(f"Data saved to {csv_filename}")

    return all_job_data

def login_and_scrape():
    with SB(uc=True) as sb:
        login_to_upwork(sb)
        scrape_jobs(sb)

# Entry point for the script
if __name__ == "__main__":
    login_and_scrape()
