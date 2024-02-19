# example_1.py
from WebScraper import WebScraper

edge_driver_path = r"path\to\edgedriver.exe"
scraper = WebScraper(driver_path=edge_driver_path, market="US10Y")
initial_data = scraper.get_data_frame()
print("Example 1: Initial Data (US10Y Treasury Bond Prices):")
print(initial_data.head())
