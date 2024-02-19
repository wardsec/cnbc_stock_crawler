# example_6.py
from WebScraper import WebScraper
import time

edge_driver_path = r"path\to\edgedriver.exe"
infinite_scraper = WebScraper(driver_path=edge_driver_path, market="US10Y")
while True:
    data = infinite_scraper.get_data_frame()
    print("\nExample 6: Infinite Data (Press Ctrl+C to stop):")
    print(data.head())
    time.sleep(10)  # Add a delay between iterations
