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
        
        # Loop through pagination from page=2 to page=370
        for page_num in range(43, 370):  # Loop from 2 up to 370
            url = f'https://www.upwork.com/nx/search/talent/?nbs=1&q=Data%20Analyst&revenue=10000&page={page_num}'
            print(f"Visiting page {page_num}...")
            sb.open(url)
            time.sleep(random.uniform(7, 12))  # Sleep between 7 to 12 seconds before scraping next page
            page_source = sb.get_page_source()
            with open("upwork_page_source.html", "w", encoding="utf-8") as file:
                file.write(page_source)
            extract_and_save_data()
            print(f"Processed page {page_num}.")


# Function to parse data from a page's source and save results into CSV
def extract_and_save_data():
    # Read the saved page source
    with open('upwork_page_source.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <article> elements
    articles = soup.find_all(
        "article",
        attrs={
            "data-ev-contractor_uid": True,
            "data-ev-label": True,
            "data-ev-page_number": True,
            "data-ev-position": True,
            "data-ev-results_count": True,
            "data-ev-search_guid": True,
        },
    )

    # Extract and save data into a CSV
    csv_file = "output2.csv"
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write CSV headers only if it's the first page
        if file.tell() == 0:  # Check if the file is empty
            writer.writerow([
                "Name", 
                "Title", 
                "Location", 
                "Rate per Hour", 
                "Profile Link", 
                "Job Success Score", 
                "Skills",
                "Earnings", 
                "Hourly Jobs Count", 
                "Fixed Price Jobs Count", 
                "Hours Worked"
            ])

        # Loop over articles and extract the desired data fields
        for article in articles:
            name_tag = article.find("a", class_="up-n-link profile-link")
            name = name_tag.text.strip() if name_tag else "N/A"

            title_tag = article.find("h4", class_="title")
            title = title_tag.text.strip() if title_tag else "N/A"

            location_tag = article.find("p", class_="m-0 location")
            location = location_tag.text.strip() if location_tag else "N/A"

            rate_tag = article.find("span", {"data-test": "rate-per-hour"})
            rate = rate_tag.text.strip() if rate_tag else "N/A"

            profile_link = name_tag['href'] if name_tag and name_tag.has_attr('href') else "N/A"

            job_success_tag = article.find("circle", class_="air3-progress-circle-fg")
            job_success_score = job_success_tag['stroke-dasharray'].split(' ')[0] if job_success_tag and 'stroke-dasharray' in job_success_tag.attrs else "N/A"

            skills_div = article.find("div", class_="air3-token-container")
            skills = []
            if skills_div:
                skill_tags = skills_div.find_all("button", class_="air3-token")
                for skill in skill_tags:
                    if 'd-none' not in skill.get('class', ''):
                        skills.append(skill.text.strip())
            skills_string = ', '.join(skills) if skills else "N/A"

            # Extract earnings data
            earnings_tag = article.find(
                "span", 
                {"data-test": "UpCPopover FreelancerTileEarnings"}
            )
            earnings = earnings_tag.text.strip() if earnings_tag else "N/A"

            # Extract hourly jobs count
            hourly_jobs_tag = article.find(
                "p", 
                string=lambda x: x and "hourly jobs" in x.lower()
            )
            hourly_jobs_count = hourly_jobs_tag.text.strip().split()[0] if hourly_jobs_tag else "N/A"

            # Extract fixed price jobs count
            fixed_price_jobs_tag = article.find(
                "p", 
                string=lambda x: x and "fixed price jobs" in x.lower()
            )
            fixed_price_jobs_count = fixed_price_jobs_tag.text.strip().split()[0] if fixed_price_jobs_tag else "N/A"

            # Extract worked hours
            hours_worked_tag = article.find(
                "p", 
                string=lambda x: x and "hours worked" in x.lower()
            )
            hours_worked = hours_worked_tag.text.strip().split()[0] if hours_worked_tag else "N/A"

            # Write the extracted row into CSV
            writer.writerow([
                name, 
                title, 
                location, 
                rate, 
                f"https://www.upwork.com{profile_link}", 
                job_success_score, 
                skills_string, 
                earnings, 
                hourly_jobs_count, 
                fixed_price_jobs_count, 
                hours_worked
            ])

# Run the full scraper sequence
if __name__ == "__main__":
    login_and_scrape()
