import time
import random
from seleniumbase import SB
import csv

# Function to scrape the first job link from the CSV file
def scrape_first_job_link():
    input_csv = "job_links.csv"
    output_file = "first_job_page_source.html"

    # Read the first link from the CSV file
    with open(input_csv, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        first_row = next(reader, None)  # Get the first data row

    if not first_row:
        print("The CSV file is empty or does not contain any links.")
        return

    first_link = first_row[1]  # Extract the link from the second column

    with SB(uc=True) as sb:
        print(f"Navigating to the first link: {first_link}...")
        sb.open(first_link)  # Open the first link
        time.sleep(random.uniform(7, 12))  # Mimic human-like browsing behavior

        # Get the page source
        page_source = sb.get_page_source()

        # Save the page source to a file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(page_source)

        print(f"Page source for the first link has been saved to {output_file}.")

# Run the script
if __name__ == "__main__":
    scrape_first_job_link()
