# Amazon Audible Best Sellers Scraper

This Python script scrapes the best-selling Audible books from Amazon and saves the data to a CSV file.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- Selenium
- BeautifulSoup
- Pandas
- Chrome WebDriver (compatible with your Chrome browser version)

Install the required Python packages using pip:

```bash
pip install selenium beautifulsoup4 pandas
```

Download the Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it's in your system PATH.

## Usage

1. Clone or download this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Run the script:

```bash
python amazon_audible_scraper.py
```

The script will scrape the Audible best sellers from Amazon and save the data to a CSV file named `amazon_audible_best_sellers.csv` in the project folder.

## Output

The CSV file contains the following columns:

- Book Name
- Author
- Rating
- Number of Ratings
- Price
- Book Image (URL)
