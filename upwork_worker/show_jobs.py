from bs4 import BeautifulSoup

# Initialize counters for job status
job_in_progress_count = 0
job_completed_count = 0
completed_jobs = []  # List to store completed job titles

# Loop through each HTML page from 1 to 11
for page_num in range(1, 12):
    # Construct the filename for each page
    filename = f'upwork_page_source_page_{page_num}.html'
    
    # Read the HTML content of the current page
    with open(filename, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all <div> elements representing jobs
    job_elements = soup.find_all('div', class_='assignments-item assignments-item-hoverable air3-card-section py-0 legacy')

    # Loop through each job element to check its status
    for job in job_elements:
        # Find the job status
        job_status = job.find('p', class_='mb-0 text-light-on-inverse')
        
        # If the status is "Job in Progress", count it as in progress
        if job_status and 'Job in progress' in job_status.text:
            job_in_progress_count += 1
        else:
            # Otherwise, count it as completed and get the <a> tag
            job_completed_count += 1
            
            # Find the <a> tag within the completed job element
            a_tag = job.find('a', class_='up-n-link cursor-pointer no-underline')
            
            # If the <a> tag is found, store or print the job title
            if a_tag:
                completed_jobs.append(a_tag.text.strip())

# Print the totals
print(f"Total number of 'Job in Progress' jobs: {job_in_progress_count}")
print(f"Total number of completed jobs: {job_completed_count}")

# Print the completed job titles
print("\nCompleted Jobs:")
for job in completed_jobs:
    print(f"- {job}")

