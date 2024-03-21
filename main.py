import time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup


driver = webdriver.Chrome()

# URL of the Amazon Audible Best Sellers
url = "https://www.amazon.com/best-sellers-audible-books/zgbs/audible"

driver.get(url)

# Wait for page to load
time.sleep(2)


def scrape_category_page():

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')


    products = soup.find_all("div", class_="p13n-sc-uncoverable-faceout")
    data = []
    for product in products:
        try:
            # Get book name
            book_name = product.find("div", class_="_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y").get_text().strip()
        except AttributeError:
            book_name = "N/A"
        
        try:
            # Get author
            author = product.find("div", class_="a-row a-size-small").get_text().strip()
        except AttributeError:
            author = "N/A"

        try:
            # Get rating
            rating = product.find("div", class_="a-icon-row").get_text().strip("").split()[0]
        except AttributeError:
            rating = "N/A"
        
        try:
            # Get number of ratings
            num_ratings = product.find('div', class_='a-icon-row').text.strip().split("stars")[-1].strip()
        except AttributeError:
            num_ratings = "N/A"
        try:
            #Get price
            price = product.find('span', class_='a-size-base').text.strip()
        except AttributeError:
            price= "N/A"
        try:
            #get image link
             book_img_link = product.find('img')['src']
        except AttributeError:
            book_img_link = "N/A"
        
        # Append product 
        data.append([book_name, author, rating, num_ratings,price,book_img_link])
     
    # Create DataFrame from data
    df = pd.DataFrame(data, columns=['Book Name', 'Author', 'Rating', 'Number of Ratings','Price','Book Image'])
    return df

# Scrape initial category page
df = scrape_category_page()

# Save DataFrame to CSV file in project folder
output_file = "amazon_audible_best_sellers.csv"
df.to_csv(output_file, index=False)
print(f"DataFrame saved as '{output_file}' in the project folder.")



driver.quit()
