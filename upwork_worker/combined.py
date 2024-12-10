import csv
from bs4 import BeautifulSoup


# Load and parse the HTML file
with open("upwork_page_source.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the page with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all <article> elements with the given attributes
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

# Output the total number of matched <article> elements
print(f"Total number of <article> elements found: {len(articles)}\n")

# Extract data from each <article> element and save it into a CSV
csv_file = "output.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write CSV headers
    writer.writerow(["Name", "Title", "Location", "Rate per Hour", "Profile Link", "Job Success Score", "Skills"])

    # Process each <article> element
    for article in articles:
        # Extract relevant data fields
        name_tag = article.find("a", class_="up-n-link profile-link")
        name = name_tag.text.strip() if name_tag else "N/A"

        title_tag = article.find("h4", class_="title")
        title = title_tag.text.strip() if title_tag else "N/A"

        location_tag = article.find("p", class_="m-0 location")
        location = location_tag.text.strip() if location_tag else "N/A"

        rate_tag = article.find("span", {"data-test": "rate-per-hour"})
        rate = rate_tag.text.strip() if rate_tag else "N/A"

        profile_link = name_tag['href'] if name_tag and name_tag.has_attr('href') else "N/A"

        # Assuming that job success percentage comes from a class like 'air3-progress-circle-93' data
        job_success_tag = article.find("circle", class_="air3-progress-circle-fg")
        job_success_score = job_success_tag['stroke-dasharray'].split(' ')[0] if job_success_tag and 'stroke-dasharray' in job_success_tag.attrs else "N/A"

        # Extract skills
        skills_div = article.find("div", class_="air3-token-container")
        skills = []
        if skills_div:
            skill_tags = skills_div.find_all("button", class_="air3-token")
            for skill in skill_tags:
                # Ignore non-visible skills like those with 'd-none'
                if 'd-none' not in skill.get('class', ''):
                    skills.append(skill.text.strip())
        skills_string = ', '.join(skills) if skills else "N/A"

        # Write extracted data to the CSV
        writer.writerow([name, title, location, rate, f"https://www.upwork.com{profile_link}", job_success_score, skills_string])

print(f"Data has been successfully saved to {csv_file}")
