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

# Output the matched elements or their attributes
# for article in articles:
#     # Print the entire element
#     print(article.prettify())  # Use prettify for better formatting

#     # Alternatively, print specific attributes if needed
#     print("Attributes found:")
#     for attr in article.attrs:
#         print(f"  {attr}: {article.attrs[attr]}")

#     print("-" * 80)  # Separator for readability
