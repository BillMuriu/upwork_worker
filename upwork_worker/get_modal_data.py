import csv
from bs4 import BeautifulSoup

def extract_modal_data():
    # Read the saved modal HTML content
    with open('modal_source.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Define the output CSV file
    csv_file = "modal_data.csv"
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write headers only if the file is empty
        if file.tell() == 0:
            writer.writerow([
                "Title", "Date Range", "Amount Earned", 
                "Price Type", "Client Rating"
            ])

        # Extract data from the modal
        modal = soup.find("div", class_="modal-content")  # Adjust class to match your modal's HTML

        if modal:
            # Extract the title
            title = modal.find("div", class_="air3-modal-title").get_text(strip=True)

            # Extract the date range
            date_range_tag = modal.find("span", class_="up-port-i18n")
            date_range = date_range_tag.get_text(strip=True) if date_range_tag else "N/A"

            # Extract the earned amount
            earned_tag = modal.find("strong", class_="feedback-summary-col")
            earned = earned_tag.get_text(strip=True) if earned_tag else "N/A"

            # Extract the fixed price label
            price_type_tag = modal.find("div", class_="mb-3x")
            price_type = price_type_tag.get_text(strip=True) if price_type_tag else "N/A"

            # Extract the client's rating
            rating_tag = modal.find("div", class_="air3-rating-foreground")
            client_rating = rating_tag["style"].replace("width:", "").strip() if rating_tag else "N/A"

            # Write the extracted data into the CSV
            writer.writerow([title, date_range, earned, price_type, client_rating])
        else:
            print("No modal found in the provided HTML.")

# Call the function
extract_modal_data()
