import pandas as pd
import os


# Replace 'your_file.json' with the actual path to your JSON fil
json_file_path = 'company_tickers.json'

# Read JSON file into a DataFrame
df = pd.read_json(json_file_path)

df_new = df.transpose()

df_new.to_csv('sec_edgar_ciks.csv',index=False)