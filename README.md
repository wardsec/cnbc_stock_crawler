
# Stock CNBC Crawler

A `WebScraper` class foi desenhada para retiramos dados de ativos de dentro da cnbc

Esta classe foi projetada para trabalhar com o driver do microsoft edge, baixe o driver em: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#downloads





## Instalação

Configure um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    .\venv\Scripts\activate    # On Windows
    ```

    Install the required packages:

    ```bash
    pip install beautifulsoup4  pandas
    pip install selenium==4.2.0
    ```







    
## Uso/Exemplo
Pegando dados de um asset e trocando para outro asset
```python
from WebScraper import WebScraper

# Instantiate the class with the initial asset (US10Y Treasury Bond Prices)
edge_driver_path = r"path\to\edgedriver.exe"
scraper = WebScraper(driver_path=edge_driver_path, market="US10Y")

# Scrape data for the initial asset
initial_data = scraper.get_data_frame()
print("Initial Data:")
print(initial_data.head())

# Change the asset to scrape data for AAPL (Apple Inc.)
scraper.change_asset("AAPL")

# Scrape data for the new asset (AAPL)
new_data = scraper.get_data_frame()
print("\nNew Data:")
print(new_data.head())


```

Por padrão a classe traz 10 segundos de preço, neste exemplos conseguimos modificar a quantidade de segundos que queremos.
```python
# Instantiate the class with max_iterations set to 5
custom_scraper = WebScraper(driver_path=edge_driver_path, market="US10Y")
custom_scraper.scrape_data(max_iterations=5)

# Get the scraped data
custom_data = custom_scraper.get_data_frame()
print("\nCustom Data (Max Iterations = 5):")
print(custom_data.head())
```
Rodando por tempo inderteminado

``` python
# Instantiate the class without specifying max_iterations
infinite_scraper = WebScraper(driver_path=edge_driver_path, market="US10Y")

# Scrape data indefinitely (until interrupted)
while True:
    # Scrape data for the initial asset
    data = infinite_scraper.get_data_frame()
    print("\nInfinite Data (Press Ctrl+C to stop):")
    print(data.head())
    time.sleep(10)
```
Exemplo de retornos

```shell
Date                 Price
2024-02-19 12:00:00  1.997
2024-02-19 12:00:01  1.998
2024-02-19 12:00:02  1.999
...

```
