import csv
from bs4 import BeautifulSoup


def extract_client_info(html):
    soup = BeautifulSoup(html, "html.parser")

    # Extract the "About the client" section
    about_client_section = soup.find("div", {"data-test": "AboutClientVisitor"})
    if not about_client_section:
        print("Debug: 'About the client' section not found.")
        return None

    # Extract individual data points
    member_since_elem = about_client_section.find("div", {"data-qa": "client-contract-date"})
    member_since = member_since_elem.small.text.strip() if member_since_elem else None
    print(f"Debug: Member since: {member_since}")

    location_elem = about_client_section.find("li", {"data-qa": "client-location"})
    location = location_elem.strong.text.strip() if location_elem else None
    print(f"Debug: Location: {location}")

    local_time_elem = location_elem.find("span", {"data-test": "LocalTime"}) if location_elem else None
    local_time = local_time_elem.text.strip() if local_time_elem else None
    print(f"Debug: Local time: {local_time}")

    industry_elem = about_client_section.find("li", {"data-qa": "client-company-profile"})
    industry = industry_elem.find("strong", {"data-qa": "client-company-profile-industry"}).text.strip() if industry_elem else None
    print(f"Debug: Industry: {industry}")

    company_size_elem = industry_elem.find("div", {"data-qa": "client-company-profile-size"}) if industry_elem else None
    company_size = company_size_elem.text.strip() if company_size_elem else None
    print(f"Debug: Company size: {company_size}")

    # Return the extracted information as a dictionary
    return {
        "member_since": member_since,
        "location": location,
        "local_time": local_time,
        "industry": industry,
        "company_size": company_size,
    }

def extract_job_details(html):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")

    # Extract the main section
    features_section = soup.find("section", {"data-test": "Features"})
    if not features_section:
        print("Debug: Features section not found.")
        return None

    # Extract individual data points
    working_hours_elem = features_section.find("div", {"data-cy": "clock-hourly"})
    working_hours = working_hours_elem.find_next("strong").text.strip() if working_hours_elem else None
    print(f"Debug: Working hours: {working_hours}")

    duration_elem = features_section.find("div", {"data-cy": "duration4"})
    duration = duration_elem.find_next("strong").text.strip() if duration_elem else None
    print(f"Debug: Duration: {duration}")

    experience_level_elem = features_section.find("div", {"data-cy": "expertise"})
    experience_level = experience_level_elem.find_next("strong").text.strip() if experience_level_elem else None
    print(f"Debug: Experience level: {experience_level}")

    # Improved hourly rate extraction logic
    hourly_rate_elem = features_section.find("div", {"data-cy": "clock-timelog"})
    hourly_rate = None
    if hourly_rate_elem:
        rate_parts = hourly_rate_elem.find_all("strong")
        if rate_parts and len(rate_parts) >= 2:
            hourly_rate = f"{rate_parts[0].text.strip()} - {rate_parts[1].text.strip()}"
    print(f"Debug: Hourly rate: {hourly_rate}")

    remote_job_elem = features_section.find("div", {"data-cy": "local"})
    remote_job = remote_job_elem.find_next("strong").text.strip() if remote_job_elem else None
    print(f"Debug: Remote job: {remote_job}")

    project_type_elem = features_section.find("div", {"data-cy": "briefcase-outlined"})
    project_type = project_type_elem.find_next("strong").text.strip() if project_type_elem else None
    print(f"Debug: Project type: {project_type}")

    # Extract the "Contract-to-hire" section
    contract_to_hire_section = soup.find("section", {"data-test": "ContractToHireBanner"})
    contract_to_hire = None
    if contract_to_hire_section:
        contract_to_hire = contract_to_hire_section.find("h4").text.strip()
    print(f"Debug: Contract-to-hire: {contract_to_hire}")

    # Return the extracted information as a dictionary
    return {
        "working_hours": working_hours,
        "duration": duration,
        "experience_level": experience_level,
        "hourly_rate": hourly_rate,
        "remote_job": remote_job,
        "project_type": project_type,
        "contract_to_hire": contract_to_hire,
    }


# File name containing the page source
input_file = "first_job_page_source.html"

# Read the HTML content
with open(input_file, "r", encoding="utf-8") as file:
    page_source = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Extract job title from the <title> element
title_element = soup.find("title")
if title_element:
    job_title = title_element.text.strip()
    print("Job Title found in <title>:", job_title)
else:
    job_title = "N/A"
    print("Job Title element not found in <title>.")

# Extract job description
job_description_element = soup.find("p", class_="text-body-sm")
if job_description_element:
    job_description = job_description_element.text.strip()
    print("Job Description found:", job_description)
else:
    job_description = "N/A"
    print("Job Description not found.")

# Extract date posted and location
# Date posted
date_posted_element = soup.find("div", {"data-test": "PostedOn"})
date_posted = (
    date_posted_element.find("span").text.strip() if date_posted_element else "N/A"
)
print("Date Posted:", date_posted)

# Location
location_element = soup.find("div", {"data-test": "LocationLabel"})
location = (
    location_element.find("span").text.strip() if location_element else "N/A"
)
print("Location:", location)

# Extract skills and expertise
skills_section = soup.find("section", {"data-test": "Expertise"})
if skills_section:
    skill_badges = skills_section.find_all("span", class_="air3-badge air3-badge-highlight badge disabled")
    skills = [badge.get_text(strip=True) for badge in skill_badges]
    skills_and_expertise = ", ".join(skills) if skills else "N/A"
    print("Skills and Expertise found:", skills_and_expertise)
else:
    skills_and_expertise = "N/A"
    print("Skills and Expertise section not found.")

# Extract client activity details
client_activity_section = soup.find("ul", class_="client-activity-items list-unstyled visitor")
if client_activity_section:
    activity_details = {}
    activity_items = client_activity_section.find_all("li", class_="ca-item")
    print(f"Number of items found: {len(activity_items)}")

    for item in activity_items:
        title = item.find("span", class_="title").text.strip() if item.find("span", "title") else None
        value = item.find("span", class_="value").text.strip() if item.find("span", "value") else None
        value_alt = item.find("div", class_="value").text.strip() if item.find("div", "value") else None

        if title and value:
            activity_details[title] = value

        if title and value_alt:
            if title in ["Interviewing:", "Invites sent:", "Unanswered invites:"]:
                activity_details[title] = value_alt

    print("Combined client activity details:", activity_details)
else:
    activity_details = {}
    print("Client activity details not found.")

def extract_hourly_rate(html):
    soup = BeautifulSoup(html, "html.parser")

    # Locate the hourly rate container
    rate_container = soup.find("div", class_="d-flex", attrs={"data-v-1e9c74a8": True})
    if not rate_container:
        print("Debug: Rate container not found.")
        return None

    # Extract the rate parts
    rate_parts = rate_container.find_all("strong", attrs={"data-v-8d6ae40e": True})
    if len(rate_parts) == 2:
        # Extract and clean both rates
        min_rate = rate_parts[0].text.strip()
        max_rate = rate_parts[1].text.strip()
        return f"{min_rate} - {max_rate}"
    else:
        print("Debug: Unexpected rate format or missing rates.")
        return None
    
# Extract client information
client_info = extract_client_info(page_source)
job_features = extract_job_details(page_source)
hourly_rate = extract_hourly_rate(page_source)
print("Client Information:", client_info)
print("Job Features:", job_features)
print("Hourly Rate:", hourly_rate)

# Save the details to a CSV file
output_file = "job_details.csv"
with open(output_file, mode="w", encoding="utf-8", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(
        [
            "Job Title",
            "Job Description",
            "Date Posted",
            "Location",
            "Skills and Expertise",
            "Client Activity",
            "Client Info",
        ]
    )
    writer.writerow(
        [
            job_title,
            job_description,
            date_posted,
            location,
            skills_and_expertise,
            activity_details,
            client_info,
        ]
    )

print(f"Job details have been extracted and saved to {output_file}.")
