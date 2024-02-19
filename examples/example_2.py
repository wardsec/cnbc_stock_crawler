# example_2.py
from WebScraper import WebScraper

edge_driver_path = r"path\to\edgedriver.exe"
scraper = WebScraper(driver_path=edge_driver_path, market="US10Y")
scraper.change_asset("AAPL")
new_data = scraper.get_data_frame()
print("\nExample 2: New Data (AAPL - Apple Inc.):")
print(new_data.head())
