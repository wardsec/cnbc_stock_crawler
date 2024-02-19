# example_3.py
from WebScraper import WebScraper

edge_driver_path = r"path\to\edgedriver.exe"
gold_scraper = WebScraper(driver_path=edge_driver_path, market="@GC.1")
gold_data = gold_scraper.get_data_frame()
print("\nExample 3: Gold Prices Data:")
print(gold_data.head())
