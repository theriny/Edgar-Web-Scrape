# ReadMe.md

This project's purpose is to scrape company filing data from the SEC Edgar website and save the filings as pdfs.

There are 2 steps.

1. Get company ticker data which will be used to search for company filings. The 'get_ticker.py' code converts the company ticker data within a .json file into a csv file. The code in step 2 will iterate the list of companies when scraping the S-1 filings data.
2. The 'webscraping.py' code accesses the Edgar website and populates a dataframe with the .htm links for S-1 filings of each company in the dataset. The content of the .htm links is then converted to individual PDFs.




## Step 1 Code Explanation (get_tickers.py)

This Python script utilizes the Pandas library to handle data and perform operations on a JSON file containing company tickers. The code reads the JSON file into a Pandas DataFrame, transposes it, and then exports the transposed DataFrame to a CSV file.

### Prerequisites

- **Pandas**: Make sure you have the Pandas library installed. If not, you can install it using:
  ```bash
  pip install pandas
  ```

### Usage

1. **JSON File**: Replace 'company_tickers.json' in the `json_file_path` variable with the actual path to your JSON file containing company tickers.

2. **Run the Script**: Execute the script using a Python interpreter:
   ```bash
   python script_name.py
   ```

   Replace `script_name.py` with the name of your Python script file.

### Code Explanation

- **Import Libraries**:
  ```python
  import pandas as pd
  import os
  ```

  This code imports the Pandas library as `pd` and the os module.

- **Specify JSON File Path**:
  ```python
  json_file_path = 'company_tickers.json'
  ```
  
  Replace 'company_tickers.json' with the actual path to your JSON file.

- **Read JSON File into DataFrame**:
  ```python
  df = pd.read_json(json_file_path)
  ```

  The code uses Pandas to read the JSON file into a DataFrame (`df`).

- **Transpose DataFrame**:
  ```python
  df_new = df.transpose()
  ```

  The DataFrame is transposed, swapping rows and columns.

- **Export Transposed DataFrame to CSV**:
  ```python
  df_new.to_csv('sec_edgar_ciks.csv', index=False)
  ```

  The transposed DataFrame is exported to a CSV file named 'sec_edgar_ciks.csv'. The `index=False` parameter ensures that row indices are not included in the CSV file.

### Notes

- Ensure that the JSON file is correctly formatted and contains the necessary data for the script to execute successfully.

- The exported CSV file will be created in the same directory as the script. Ensure that you have write permissions for that directory.

- Adjust the script if needed based on your specific requirements or the structure of your JSON file.


## Step 2 Code Explanation (webscraping.py)


## Selenium Web Scraping Script

This Python script uses the Selenium library to perform web scraping on the U.S. Securities and Exchange Commission (SEC) website (https://www.sec.gov/edgar/searchedgar/companysearch). The goal is to retrieve filing information (specifically, Form Type, Form Description, Filing Date, and Reporting Date) for a list of company tickers stored in a CSV file ('sec_edgar_ciks.csv').

### Prerequisites

- **Selenium**: Ensure you have the Selenium library installed. If not, you can install it using:
  ```bash
  pip install selenium
  ```

- **WebDriver**: Download the appropriate WebDriver for your browser and set the path to the executable in the script. In this example, the Chrome WebDriver ('chromedriver') is used.

- **Pandas**: Make sure you have the Pandas library installed. If not, you can install it using:
  ```bash
  pip install pandas
  ```

- **pdfkit**: Install the pdfkit library for PDF-related functionalities. You can install it using:
  ```bash
  pip install pdfkit
  ```

### Usage

1. **Webdriver Path**: Set the correct path to your WebDriver executable in the script:
   ```python
   webdriver_path = 'chromedriver'
   ```

2. **CSV File**: Ensure that the CSV file ('sec_edgar_ciks.csv') containing the company tickers is in the correct format and path.

3. **Run the Script**: Execute the script using a Python interpreter:
   ```bash
   python script_name.py
   ```
   Replace `script_name.py` with the name of your Python script file.

### Code Explanation

- **Import Libraries**:
  ```python
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC
  from selenium.webdriver.common.keys import Keys
  from selenium.common.exceptions import TimeoutException
  import time
  import pandas as pd
  import pdfkit
  ```

- **Load Ticker Data**:
  ```python
  df = pd.read_csv('sec_edgar_ciks.csv', index_col=False, usecols=['ticker'])
  ```

  Load the company tickers from the CSV file into a Pandas DataFrame.

- **Web Scraping Logic**:
  The script iterates through the tickers, performs a search on the SEC website, and extracts filing information.

- **Data Processing**:
  ```python
  df_table = pd.DataFrame(table_data[1:])
  df_table.columns = ['Ticker', 'PDF Link', 'Form Type', 'Form Desc', 'Filing Date', 'Reporting Date']
  df_table['Form Type'] = df_table['Form Type'].apply(lambda x: x.replace('/', '-'))
  ```

  Convert the extracted data into a Pandas DataFrame, set column names, and process the 'Form Type' column.

- **Closing the Browser**:
  ```python
  driver.quit()
  ```

  Close the Chrome WebDriver instance.

### Notes

- Ensure you comply with the terms of service of the SEC website while using this script.

- Adjust the script as needed based on changes in the website structure or your specific requirements.

- Check for updates to the website's structure or the Selenium library that may affect the script's functionality.


