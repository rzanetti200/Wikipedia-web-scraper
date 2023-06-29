import requests
from bs4 import BeautifulSoup
import csv
from collections import Counter
import re
import sys

# Function to get the text content and image links from Wikipedia URL
def get_wikipedia_content(wikipedia_url):
    response = requests.get(wikipedia_url)
    
    # If the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text_content = ""
        
        # Extracting text from paragraphs
        for paragraph in soup.find_all('p'):
            text_content += paragraph.get_text()
        
        # Extracting image links
        image_links = []
        for img_tag in soup.find_all('img'):
            image_link = img_tag.get('src')
            if image_link:
                # Convert relative image links to absolute links
                if image_link.startswith("//"):
                    image_link = "https:" + image_link
                image_links.append(image_link)
            
        return text_content, image_links
    else:
        return None, None

# Function to count the words in the text
def count_words(text_content):
    # Removing non-alphanumeric characters and numbers
    words = re.findall(r'\b[a-zA-Z]+\b', text_content.lower())
    return Counter(words)

# Function to save the word frequencies and image links to a CSV file
def save_to_csv(word_freqs, image_links, total_word_count, output_file, top_n):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Writing the total word count
        writer.writerow([f'Total word count: {total_word_count}'])
        writer.writerow('')

        
        # Writing word frequencies with the dynamic header
        writer.writerow([f'Top {top_n} Words'])
        for word, freq in word_freqs.most_common(top_n):
            writer.writerow([f'{word} - {freq}'])
        
        # Writing image links
        writer.writerow('')
        writer.writerow(['Image Links'])
        for link in image_links:
            writer.writerow([link])

if __name__ == "__main__":
    wikipedia_url = input("Enter the Wikipedia URL: ")
    output_file = 'wikipedia_content.csv'
    
    # Set this variable to the number of top words you want
    top_n = 40
    
    text_content, image_links = get_wikipedia_content(wikipedia_url)
    
    if text_content and image_links is not None:
        word_freqs = count_words(text_content)
        total_word_count = sum(word_freqs.values())
        save_to_csv(word_freqs, image_links, total_word_count, output_file, top_n)
        print(f'Content saved to {output_file}')
    else:
        print("Failed to retrieve the content from the URL.")
