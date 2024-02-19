# example_4.py
from WebScraper import WebScraper

edge_driver_path = r"path\to\edgedriver.exe"
gold_scraper = WebScraper(driver_path=edge_driver_path, market="@GC.1")
gold_scraper.change_asset("@CL.1")
oil_data = gold_scraper.get_data_frame()
print("\nExample 4: Oil Prices Data:")
print(oil_data.head())
