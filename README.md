# Wikipedia Content Scraper

Wikipedia Content Scraper is a Python script I made that extracts and processes text content from a Wikipedia page. It outputs the frequency of the top N words, the total word count, and links to all the images on the page in a CSV file.

## How it works

1. The script takes a Wikipedia URL as input.
2. It sends an HTTP request to the URL and retrieves the HTML content.
3. The script uses Beautiful Soup to parse the HTML and extract the text content and image links.
4. It processes the text content to count the occurrences of each word (excluding numbers).
5. The script then saves the top N word frequencies, total word count, and image links in a CSV file.

## Dependencies

- Python 3.x
- Beautiful Soup 4
- Requests

You can install the dependencies using `pip`:

\```sh
pip install beautifulsoup4 requests
\```

## How to run the code

1. Clone this repository or download the script `wikipedia_content_scraper.py`.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Python:

\```sh
python wikipedia_content_scraper.py
\```

4. When prompted, enter the Wikipedia URL you want to scrape.
5. The script will create a CSV file named `wikipedia_content.csv` containing the word frequencies, total word count, and image links.
6. If you want to change the number of top words saved to the CSV file, modify the `top_n` variable in the script.