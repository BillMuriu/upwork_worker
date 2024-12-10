from bs4 import BeautifulSoup

# Read the HTML file
with open('upwork_page_source.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <h5> elements with the specific attributes
matching_elements = soup.find_all('h5', {
    'role': 'presentation',
    'class': 'align-items-center mb-2x',
    'data-v-6ba7fa90': ''
})

# Print the elements and count
print(f"Number of matching elements: {len(matching_elements)}")
for index, element in enumerate(matching_elements, 1):
    print(f"{index}: {element.text.strip()}")
