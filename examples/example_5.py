# example_5.py
from WebScraper import WebScraper

edge_driver_path = r"path\to\edgedriver.exe"
custom_scraper = WebScraper(driver_path=edge_driver_path, market="US10Y")
custom_scraper.scrape_data(max_iterations=5)
custom_data = custom_scraper.get_data_frame()
print("\nExample 5: Custom Data (Max Iterations = 5):")
print(custom_data.head())
