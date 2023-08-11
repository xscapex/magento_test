from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

# Function to fetch the web page content using Selenium
def get_page_content(url):

    service = Service(executable_path = '/usr/bin/chromedriver')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    # options.add_argument('--disable-extensions')
    # options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(service=service,chrome_options=options) # Change to the appropriate driver for your browser
    driver.get(url)
    page_content = driver.page_source
    driver.quit()
    return page_content

# # Function to parse the table and convert it to a pandas DataFrame
# def parse_table_to_dataframe(html_content):
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Find the table
#     table = soup.find('table')

#     print(table)

#     # if not table:
#     #     return None

#     # Extract the table data
#     table_data = []
#     rows = table.find_all('tr')
#     for row in rows:
#         cols = row.find_all(['th', 'td'])
#         row_data = [col.text.strip() for col in cols]
#         table_data.append(row_data)

#     # Convert table data to DataFrame
#     df = pd.DataFrame(table_data[2:], columns=table_data[1])

#     return df


# def parse_text_to_dataframe(html_content):

#     soup = BeautifulSoup(html_content, 'html.parser')


#     text_editor_divs = soup.find_all('div', class_='textEditor clearfix')

#     # text_content = text_editor_divs.get_text()

#     table_data = []
#     df = pd.DataFrame({'text_content': []})

#     for div in text_editor_divs:
#         text_content = ''.join(str(tag) for tag in div.contents if isinstance(tag, str))
#         table_data.append(text_content)
    

#     merged_string = ''.join([line.strip() for line in table_data]).replace('\n', '').replace('    ', '').replace('文字編輯器', '').replace('註1：','').replace('註: 1.','').replace(' ','').replace('\xa0', '')


#     df.at[0, 'text_content'] = merged_string

#     with open("file1.txt", "w") as file:
#         file.write(merged_string)

#     return df


# def parse_news_to_dataframe(html_content):

#     soup = BeautifulSoup(html_content, 'html.parser')


#     text_editor_divs = soup.find_all('div', class_='textEditor clearfix')


#     # text_content = text_editor_divs.get_text()

#     table_data = []
#     df = pd.DataFrame({'text_content': []})


#     for div in text_editor_divs:
#         text_content = ''.join(str(tag) for tag in div.contents if isinstance(tag, str))
#         table_data.append(text_content)
    

#     merged_string = ''.join([line.strip() for line in table_data]).replace('\n', '').replace('    ', '').replace('文字編輯器', '').replace('註1：','').replace('註: 1.','').replace(' ','').replace('\xa0', '')


#     second_period_index = merged_string.find('。', merged_string.find('。') + 1)  
#     extracted_text = merged_string[:second_period_index + 1] 

#     df.at[0, 'text_content'] = extracted_text


#     with open("file1.txt", "w") as file:
#         file.write(extracted_text)

#     return df

# # # URL of the web page to crawl
# # url = "https://www.hannstar.com/news-detail/113__59/"  # Replace with the URL you want to crawl

# # # Get the web page content
# # page_content = get_page_content(url)

# # # Parse the table and convert it to a pandas DataFrame
# # dataframe1 = parse_table_to_dataframe(page_content)


# # # Parse the table and convert it to a pandas DataFrame
# # dataframe2 = parse_news_to_dataframe(page_content)

# # print(dataframe2)


# # output_file = 'file1.xlsx'
# # with pd.ExcelWriter(output_file) as writer:
# #     dataframe1.to_excel(writer, sheet_name='table', index=False)
# #     dataframe2.to_excel(writer, sheet_name='content', index=False)



# def crawler_news(url,filename):

#     # Get the web page content
#     page_content = get_page_content(url)

#     # Parse the table and convert it to a pandas DataFrame
#     dataframe1 = parse_table_to_dataframe(page_content)


#     # Parse the table and convert it to a pandas DataFrame
#     dataframe2 = parse_news_to_dataframe(page_content)

#     print(dataframe2)


#     output_file = f'./old/tw/{filename}.xlsx'
#     with pd.ExcelWriter(output_file) as writer:
#         dataframe1.to_excel(writer, sheet_name='table', index=False)
#         dataframe2.to_excel(writer, sheet_name='content', index=False)


# def crawler_financials(url,filename):

#     # Get the web page content
#     page_content = get_page_content(url)

#     # Parse the table and convert it to a pandas DataFrame
#     dataframe1 = parse_table_to_dataframe(page_content)


#     # Parse the table and convert it to a pandas DataFrame
#     dataframe2 = parse_text_to_dataframe(page_content)

#     print(dataframe2)

#     output_file = f'./old/tw/{filename}.xlsx'
#     with pd.ExcelWriter(output_file) as writer:
#         dataframe1.to_excel(writer, sheet_name='table', index=False)
#         dataframe2.to_excel(writer, sheet_name='content', index=False)



# file_url_pairs_financials = [
# ("https://www.hannstar.com/news-detail/financial_2021Q1/","little_test")

# ]


# for url, filename in file_url_pairs_financials:
#     crawler_financials(url,filename)



get_page_content('https://www.hannstar.com/news-detail/financial_2021Q1/')