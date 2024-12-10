from bs4 import BeautifulSoup

# Read the HTML file
with open('upwork_page_source.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <div> elements representing jobs
job_elements = soup.find_all('div', class_='assignments-item assignments-item-hoverable air3-card-section py-0 legacy')

# Initialize counters
job_in_progress_count = 0
job_completed_count = 0

# Loop through each job element
for job in job_elements:
    # Check if the job has the text "Job in Progress" inside it
    job_status = job.find('p', class_='mb-0 text-light-on-inverse')
    
    # If the status is "Job in Progress", count it as in progress
    if job_status and 'Job in progress' in job_status.text:
        job_in_progress_count += 1
    else:
        # Otherwise, count it as completed and get the <a> tag
        job_completed_count += 1
        
        # Find the <a> tag within the completed job element
        a_tag = job.find('a', class_='up-n-link cursor-pointer no-underline')
        
        # If the <a> tag is found, print or store it
        if a_tag:
            print(f"Completed Job: {a_tag.text.strip()}")

# Print the totals
print(f"Total number of 'Job in Progress' jobs: {job_in_progress_count}")
print(f"Total number of completed jobs: {job_completed_count}")

