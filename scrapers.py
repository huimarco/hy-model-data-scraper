# Import required packages
import pandas as pd
import yfinance as yf
import requests
import json
from bs4 import BeautifulSoup
from datetime import date
from datetime import timedelta

def scrape(url, headers, span, class_):
    # Send an HTTP GET request to the provided URL with custom headers
    response = requests.get(url, headers=headers)

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the HTML element with the specified tag and class name
    element = soup.find(span, class_=class_)

    # Extract the text content of the HTML element and remove leading/trailing spaces
    value = element.get_text(strip=True)

    return value

# Function to scrape data from Investing.com for oil prices
def scrape_oil_futures(url, headers):
    # Send an HTTP GET request to the provided URL with custom headers
    response = requests.get(url, headers=headers)
    
    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find HTML table
    element = soup.find_all('table')[1]
    
    # Read the table data into a DataFrame
    df = pd.read_html(str(element), flavor='bs4')[0].reset_index(drop=True)
    
    # Get the price from the second record (previous day)
    crude_oil_futures = df.iloc[1][1]
    
    # Return the scraped data (Oil price)
    return crude_oil_futures

# Function to scrape data from WSJ (Wall Street Journal)
def scrape_nyse_adv_dec(url, headers):
    # Send an HTTP GET request to the provided URL with custom headers
    response = requests.get(url, headers=headers)
    
    # Convert the response text to a JSON string and parse
    element = json.loads(str(response.text))
    
    # Extract relevant data from the JSON structure
    adv = element["data"]["instrumentSets"][0]["instruments"][1]["latestClose"].replace(',','')
    dec = element["data"]["instrumentSets"][0]["instruments"][2]["latestClose"].replace(',','')
    
    # Return the scraped data (Advances and Declines)
    return adv, dec

# Function to scrape data from NASDAQ using yfinance
def scrape_nasdaq_composite():
    # Get date of previous day
    yesterday = (date.today() - timedelta(days = 1)).strftime('%m/%d/%Y')

    # Create a Ticker object for NASDAQ index
    nasdaq_ticker = yf.Ticker('^IXIC')
    
    # Retrieve historical data and reset the index
    df = nasdaq_ticker.history().reset_index()
    
    # Filter the DataFrame for the specified previous weekday's date
    filtered_df = df[df['Date'] == yesterday].reset_index()
    
    # Extract the 'Close' value for the specified date
    nasdaq_composite = filtered_df.loc[0, 'Close']
    
    # Return the scraped data (NASDAQ closing value)
    return nasdaq_composite