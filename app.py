import requests
from bs4 import BeautifulSoup
import json

def get_description(keyword):
    # Using Bing search to get the description (modify the URL if you prefer a different search engine)
    search_url = f"https://www.bing.com/search?q={keyword}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0"
    }

    # Make the request
    response = requests.get(search_url, headers=headers)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the description from the search results (modify the selector based on the search engine's HTML structure)
    description_tag = soup.find('div', class_='b_caption')
    description = description_tag.get_text() if description_tag else "Description not found"

    return description

def main():
    # List of keywords
    keywords = ["Live Mint", "Verge", "Financial Times", "CNN"]

    # Dictionary to store keyword and description pairs
    keyword_descriptions = {}

    # Get descriptions for each keyword
    for keyword in keywords:
        description = get_description(keyword)
        keyword_descriptions[keyword] = description

    # Ask the user for the filename to save as
    filename = input("Enter the filename to save the JSON data (e.g., output.json): ") + ".json"

    # Save the data as a JSON file in the same directory
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(keyword_descriptions, json_file, ensure_ascii=False, indent=4)

    print(f"Data saved to {filename}")

if __name__ == "__main__":
    main()
