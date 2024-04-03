# Import scraper functions
from datetime import date, timedelta
from scrapers import scrape, scrape_oil_futures, scrape_nyse_adv_dec, scrape_nasdaq_composite

def scrape_all():
    # Define inputs
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    bofa_hy_total_inputs = ['https://fred.stlouisfed.org/series/BAMLHYH0A0HYM2TRIV', headers, 'span', 'series-meta-observation-value']
    value_line_geo_inputs = ['https://www.google.com/finance/quote/VALUG:INDEXNYSEGIS?sa=X&ved=2ahUKEwjbzZC47-P_AhXpJEQIHZLDDZ8Q3ecFegQIExAX&window=1M', headers, 'div', 'P6K39c']
    crude_oil_futures_inputs = ['https://www.investing.com/commodities/crude-oil-historical-data', headers]
    nyse_adv_dec_inputs = ['https://www.wsj.com/market-data/stocks/marketsdiary?id=%7B%22application%22%3A%22WSJ%22%2C%22marketsDiaryType%22%3A%22diaries%22%7D&type=mdc_marketsdiary', headers]

    # Run the scraper functions
    bofa_hy_total = scrape(*bofa_hy_total_inputs)
    value_line_geo = scrape(*value_line_geo_inputs)
    crude_oil_futures = scrape_oil_futures(*crude_oil_futures_inputs)
    nyse_adv_dec = scrape_nyse_adv_dec(*nyse_adv_dec_inputs)
    nasdaq_composite = scrape_nasdaq_composite()

    # Get date of previous day
    yesterday = date.today() - timedelta(days=1)

    return yesterday, float(bofa_hy_total.replace(',','')), float(nasdaq_composite), float(value_line_geo), int(nyse_adv_dec[0]), int(nyse_adv_dec[1]), float(crude_oil_futures)