from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
import pdfkit


#import company data
df = pd.read_csv('sec_edgar_ciks.csv',index_col = False,usecols= ['ticker'])

# Set the path to your webdriver executable
webdriver_path = 'chromedriver'

# URL of the website you want to scrape
url = 'https://www.sec.gov/edgar/searchedgar/companysearch'

# Define the XPaths for the button and the search box
button_xpath = '//*[@id="btnViewAllFilings"]'
search_box_xpath = '//*[@id="searchbox"]'

# Create a Chrome WebDriver instance with the Service object
#driver = webdriver.Chrome(executable_path=webdriver_path)
driver = webdriver.Chrome()

# Open the websit
driver.get(url)

# empty list for data
table_data = []

try:
    for i in range(10088,10089):
        
        try:
            # Wait for the popup element to be visible
            element = WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="fsrInvite"]/section[3]/button[2]'))
            )

            # Click the element
            element.click()

        except TimeoutException:
            print("The element is not visible within the specified timeout. Continuing with the rest of the code.")



        # Wait until ticker search is visible
        wait = WebDriverWait(driver, 4)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="edgar-company-person"]')))

        #find ticker search field
        search_field = driver.find_element(By.XPATH, '//*[@id="edgar-company-person"]')

        #enter text into ticker search field
        print(df['ticker'][i])
        #search_field.send_keys(df['ticker'][i])
        
        
        # type one character at a time into search field
        for char in df['ticker'][i]:
            search_field.send_keys(char)
            time.sleep(1)
         
        #safety measure to ensure table has populated
        time.sleep(2)
            
        #hit return key
        search_field.send_keys(Keys.ENTER)
        

        
        try:
            
        
            # Check if the filing button is visible
            if wait.until(EC.visibility_of_element_located((By.XPATH, button_xpath))).is_displayed():
                print("Filing Button is visible")
                
                # Wait until filing button is visible
                wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnViewAllFilings"]')))

                #find filings button
                filings = driver.find_element(By.XPATH, '//*[@id="btnViewAllFilings"]')

                #click filings button
                filings.click()

                #wait 5 seconds
                time.sleep(5)

                #Find search field
                s1_search = driver.find_element(By.XPATH, '//*[@id="searchbox"]')

                #type in form type
                s1_search.send_keys('S-1')

                #find table element
                table = driver.find_element(By.XPATH, '//*[@id="filingsTable"]')

                # Extract data from the table
                rows = table.find_elements(By.XPATH, ".//tr")

                # check if autocomplete table is populating
                if len(rows) == 2:
                    print('No rows')

                    #i = i - 1

                    # Open the website
                    driver.get(url)
                    
                else:

                    for row in rows:
                        link_element = row.find_elements(By.XPATH, ".//td[2]//a")
                        link = link_element[0].get_attribute("href") if link_element else ""
                        row_data = [cell.text for cell in row.find_elements(By.XPATH, ".//td")]
                        table_data.append([df['ticker'][i]] + [link] + row_data)

                    # Go back to home page
                    driver.get(url)
            
            elif wait.until(EC.visibility_of_element_located((By.XPATH, search_box_xpath))).is_displayed():
                print("Search box is visible")
                
                #Find search field
                s1_search = driver.find_element(By.XPATH, search_box_xpath)

                #type in form type
                s1_search.send_keys('S-1')

                #find table element
                table = driver.find_element(By.XPATH, '//*[@id="filingsTable"]')

                # Extract data from the table
                rows = table.find_elements(By.XPATH, ".//tr")

                # check if autocomplete table is populating
                if len(rows) == 2:
                    print('No rows')

                    #i = i - 1

                    # Open the website
                    driver.get(url)
                    
            else:
                print('Neither filing button or search box is visible')
                # Open the website
                driver.get(url)
                
                
        except Exception as e:
            print(f" An error occurred: {e}")
            
            #go back to home page
            driver.get(url)
                
                    
        
except Exception as e:
    print(f"An error occurred: {e}")
    
    #go back to home page
    driver.get(url)

# Convert the table data to a DataFrame
df_table = pd.DataFrame(table_data[1:])
print(df_table.shape)

# add column names
df_table.columns = ['Ticker','PDF Link','Form Type', 'Form Desc', 'Filing Date','Reporting Date']

# Replace '/' in Form Type with '-'
df_table['Form Type'] = df_table['Form Type'].apply(lambda x: x.replace('/','-'))




# Close the browser window
driver.quit()