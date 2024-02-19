from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import pandas as pd
from datetime import datetime
import time


class WebScraper:
    """
    A class to scrape financial data from CNBC website.

    Attributes:
    - driver_path (str): The path to the WebDriver executable.
    - market (str): The name of the market to scrape data for.
    """
    
    def __init__(self, driver_path, market):
        """
        Initializes the WebScraper object with the provided driver path and market.
        Automatically starts scraping data.

        Parameters:
        - driver_path (str): The path to the WebDriver executable.
        - market (str): The name of the market to scrape data for.
        """

        self.driver_path = driver_path
        self.market = market
        self.url = f"https://www.cnbc.com/quotes/{market}"
        self.options = Options()
        self.options.headless = True
        self.options.add_argument("--log-level=3")
        self.driver = None
        self.data_list = []
        
        
        # Automatically scrape data when the class is instantiated
        self._scrape_data()

    def setup_driver(self):
        """
        Sets up the WebDriver for scraping.
        """
        self.driver = webdriver.Edge(executable_path=self.driver_path, options=self.options)

    def _scrape_data(self, max_iterations=10):
        """
        Method to scrape data from the CNBC website for the specified market.

        Parameters:
        - max_iterations (int, optional): The maximum number of iterations to scrape data.
          If None, the method will run indefinitely.

        Returns:
        - None
        """
        self.setup_driver()
        self.driver.get(self.url)
        iteration_count = 0

        while True:
            try:
                html = self.driver.page_source
                soup = BeautifulSoup(html, "lxml")
                results = soup.find_all('span', {"class": "QuoteStrip-lastPrice"})

                for result in results:
                    price = float(result.get_text().replace('%', '')) / 100
                    date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
                    self.data_list.append([date, price])

                time.sleep(1)

                iteration_count += 1

                if max_iterations is not None and iteration_count >= max_iterations:
                    break

            except Exception as e:
                print("An error occurred:", e)
                break

        self.close_driver()

    def get_data_frame(self):
        """
        Returns the scraped data as a DataFrame.

        Returns:
        - pandas.DataFrame: The scraped data.
        """
        data_df = pd.DataFrame(self.data_list, columns=['Date', 'Price'])
        return data_df

    def close_driver(self):
        """
        Closes the WebDriver.

        Returns:
        - None
        """
        if self.driver:
            self.driver.quit()
            
    def change_asset(self, new_market):
        """
        Change the market to scrape data for.

        Parameters:
        - new_market (str): The name of the new market.

        Returns:
        - None
        """
        self.market = new_market
        self.url = f"https://www.cnbc.com/quotes/{self.market}"
        self.data_list.clear()
        self._scrape_data()
