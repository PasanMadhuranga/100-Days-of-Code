from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfDlns3pSQDp9cn0IBMh6_vpuKvg8erhn0cv2JaUitoTsCyiw/viewform?usp=sf_link"
rental_places_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.79725111914063%2C%22east%22%3A-122.06940688085938%2C%22south%22%3A37.37366724308699%2C%22north%22%3A38.17474567243644%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

# Get the html file of the website.
response = requests.get(url=rental_places_url, headers=headers)
rental_places_website_html = response.text

# Create soup.
soup = BeautifulSoup(rental_places_website_html, "html.parser")

# Get all the prices of the rental places.
rental_prices_tags = soup.select(selector=".kJFQQX span")
rental_prices = [price_tag.text.split("+")[0] for price_tag in rental_prices_tags]

# Get all the addresses of the rental places.
rental_addresses_tags = soup.select(selector=".property-card-data a address")
rental_addresses = [rental_addresses_tag.text for rental_addresses_tag in rental_addresses_tags]

# Get all links for rental places.
rental_links_tags = soup.select(selector=".property-card-data a")  # .property-card-link
rental_links = []
for link in rental_links_tags:
    href = link["href"]
    if "http" not in href:
        rental_links.append(f"https://www.zillow.com{href}")
    else:
        rental_links.append(href)

chrome_driver_path = "D:/My Classes/100 Days of Code - The Complete Python Pro Bootcamp for 2021/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(google_form_url)

if len(rental_addresses) == len(rental_prices) == len(rental_links):
    for index in range(len(rental_links)):
        driver.get(google_form_url)

        # Fill the form
        all_entries = driver.find_elements(By.CSS_SELECTOR, ".Xb9hP .zHQkBf")
        all_entries[0].send_keys(rental_addresses[index])
        all_entries[1].send_keys(rental_prices[index])
        all_entries[2].send_keys(rental_links[index])

        # Submit the form.
        submit_button = driver.find_element(By.CSS_SELECTOR, ".Fxmcue .snByac")
        submit_button.click()
else:
    print("Didn't get all the information correctly.")
    print(f"number of addresses get: {rental_addresses}")
    print(f"number of prices get: {rental_prices}")
    print(f"number of links get: {rental_links}")

