# Edgar-Web-Scrape

This project's purpose is to scrape company filing data from the SEC Edgar website and save the filings as pdfs.

The 'webscraping.py' code accesses the Edgar website and populates a dataframe with the .htm links for S-1 filings of each company in the dataset. The content of the .htm links is then coverted to individual PDFs.
The 'get_ticker.py' code converts the company ticker data within a .json file into a csv file. The 'webscraping.py' code iterates thhe list of companies when scraping the S-1 filings data.
