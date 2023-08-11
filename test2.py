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

    service = Service(executable_path = ChromeDriverManager().install())
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-extensions')
    options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(service=service,options=options) # Change to the appropriate driver for your browser
    driver.get(url)
    # time.sleep(5)
    # driver.get(url)
    # # 使用XPath选择器定位语言选择按钮元素
    # language_button = driver.find_element(By.XPATH, "//button[@id='switcher-language-trigger']")  # 请替换为实际的按钮选择器

    # # 点击语言选择按钮
    # language_button.click()
    page_content = driver.page_source
    driver.quit()
    return page_content

# Function to parse the table and convert it to a pandas DataFrame
def parse_table_to_dataframe(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table
    table = soup.find('table')

    print(table)

    # if not table:
    #     return None

    # Extract the table data
    table_data = []
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all(['th', 'td'])
        row_data = [col.text.strip() for col in cols]
        table_data.append(row_data)

    # Convert table data to DataFrame
    df = pd.DataFrame(table_data[2:], columns=table_data[1])

    return df


def parse_text_to_dataframe(html_content):

    soup = BeautifulSoup(html_content, 'html.parser')

    # 找到<div class="textEditor clearfix">标签
    text_editor_divs = soup.find_all('div', class_='textEditor clearfix')

    # 提取标签内的文字内容
    # text_content = text_editor_divs.get_text()

    # 建立空的DataFrame
    table_data = []
    df = pd.DataFrame({'text_content': []})

    # 提取每个标签内的文字内容
    for div in text_editor_divs:
        text_content = ''.join(str(tag) for tag in div.contents if isinstance(tag, str))
        table_data.append(text_content)
    

    merged_string = ''.join([line.strip() for line in table_data]).replace('\n', '').replace('    ', '').replace('文字編輯器', '').replace('註1：','').replace('註: 1.','').replace(' ','').replace('\xa0', '')
    # merged_string = ''.join([line.strip() for line in table_data]).replace('    ', '').replace('文字編輯器', '').replace('註1：','').replace('註: 1.','').replace('\n', '')
    # 移除 '文字編輯器'、\n 以及註解 '註: 1.'，並去除空白鍵
    # cleaned_data = [line.replace('文字編輯器', '').replace('\n', '').replace('註: 1.', '').replace('\xa0', '').replace(' ', '').strip() for line in table_data]

    # cleaned_data2 = [line.replace(' ', '') for line in cleaned_data]

    # 將列表中的元素結合成一個字串
    # merged_string = '\n'.join(cleaned_data)

    df.at[0, 'text_content'] = merged_string

    # 打开文件以写入模式
    with open("file1.txt", "w") as file:
        file.write(merged_string)

    return df


def parse_news_to_dataframe(html_content):

    soup = BeautifulSoup(html_content, 'html.parser')

    # 找到<div class="textEditor clearfix">标签
    text_editor_divs = soup.find_all('div', class_='textEditor clearfix')

    # 提取标签内的文字内容
    # text_content = text_editor_divs.get_text()

    # 建立空的DataFrame
    table_data = []
    df = pd.DataFrame({'text_content': []})

    # 提取每个标签内的文字内容
    for div in text_editor_divs:
        text_content = ''.join(str(tag) for tag in div.contents if isinstance(tag, str))
        table_data.append(text_content)
    

    merged_string = ''.join([line.strip() for line in table_data]).replace('\n', '').replace('    ', '').replace('文字編輯器', '').replace('註1：','').replace('註: 1.','').replace(' ','').replace('\xa0', '')
    # merged_string = ''.join([line.strip() for line in table_data]).replace('    ', '').replace('文字編輯器', '').replace('註1：','').replace('註: 1.','').replace('\n', '')
    # 移除 '文字編輯器'、\n 以及註解 '註: 1.'，並去除空白鍵
    # cleaned_data = [line.replace('文字編輯器', '').replace('\n', '').replace('註: 1.', '').replace('\xa0', '').replace(' ', '').strip() for line in table_data]

    # cleaned_data2 = [line.replace(' ', '') for line in cleaned_data]

    # 將列表中的元素結合成一個字串
    # merged_string = '\n'.join(cleaned_data)

    second_period_index = merged_string.find('。', merged_string.find('。') + 1)  # 找到第二個句點的索引位置
    extracted_text = merged_string[:second_period_index + 1]  # 提取子字串

    df.at[0, 'text_content'] = extracted_text

    # 打开文件以写入模式
    with open("file1.txt", "w") as file:
        file.write(extracted_text)

    return df

# # URL of the web page to crawl
# url = "https://www.hannstar.com/news-detail/113__59/"  # Replace with the URL you want to crawl

# # Get the web page content
# page_content = get_page_content(url)

# # Parse the table and convert it to a pandas DataFrame
# dataframe1 = parse_table_to_dataframe(page_content)


# # Parse the table and convert it to a pandas DataFrame
# dataframe2 = parse_news_to_dataframe(page_content)

# print(dataframe2)

# # 将两个DataFrame保存到同一个Excel文件的不同工作表中
# output_file = 'file1.xlsx'
# with pd.ExcelWriter(output_file) as writer:
#     dataframe1.to_excel(writer, sheet_name='table', index=False)
#     dataframe2.to_excel(writer, sheet_name='content', index=False)



def crawler_news(url,filename):

    # Get the web page content
    page_content = get_page_content(url)

    # Parse the table and convert it to a pandas DataFrame
    dataframe1 = parse_table_to_dataframe(page_content)


    # Parse the table and convert it to a pandas DataFrame
    dataframe2 = parse_news_to_dataframe(page_content)

    print(dataframe2)

    # 将两个DataFrame保存到同一个Excel文件的不同工作表中
    output_file = f'./old/tw/{filename}.xlsx'
    with pd.ExcelWriter(output_file) as writer:
        dataframe1.to_excel(writer, sheet_name='table', index=False)
        dataframe2.to_excel(writer, sheet_name='content', index=False)


def crawler_financials(url,filename):

    # Get the web page content
    page_content = get_page_content(url)

    # Parse the table and convert it to a pandas DataFrame
    dataframe1 = parse_table_to_dataframe(page_content)


    # Parse the table and convert it to a pandas DataFrame
    dataframe2 = parse_text_to_dataframe(page_content)

    print(dataframe2)

    # 将两个DataFrame保存到同一个Excel文件的不同工作表中
    output_file = f'./old/tw/{filename}.xlsx'
    with pd.ExcelWriter(output_file) as writer:
        dataframe1.to_excel(writer, sheet_name='table', index=False)
        dataframe2.to_excel(writer, sheet_name='content', index=False)





#news是營收報告
# 假设有多组文件名和URL
# file_url_pairs_news = [
#  ("https://www.hannstar.com/news-detail/108/","瀚宇彩晶2021年1月份營收報告"),
# ("https://www.hannstar.com/news-detail/financial_11002/","瀚宇彩晶2021年2月份營收報告"),
# ("https://www.hannstar.com/news-detail/financial_11003__1/","瀚宇彩晶2021年3月份營收報告"),
# ("https://www.hannstar.com/news-detail/financial_11004/","瀚宇彩晶2021年4月份營收報告"),
# ("https://www.hannstar.com/news-detail/financial_11005/","瀚宇彩晶2021年5月份營收報告"),
# ("https://www.hannstar.com/news-detail/financial_11006/","瀚宇彩晶2021年6月份營收報告"),
# ("https://www.hannstar.com/news-detail/financial_11007/","瀚宇彩晶2021年7月份營收報告"),
# ("https://www.hannstar.com/news-detail/financial_11008/","瀚宇彩晶2021年8月份營收報告"),
# ("https://www.hannstar.com/news-detail/113/","瀚宇彩晶2021年9月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__2/","瀚宇彩晶2021年10月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__5/","瀚宇彩晶2021年11月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__8/","瀚宇彩晶2021年12月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__11/","瀚宇彩晶2022年1月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__14/","瀚宇彩晶2022年2月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__17/","瀚宇彩晶2022年3月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__20/","瀚宇彩晶2022年4月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__23/","瀚宇彩晶2022年5月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__26/","瀚宇彩晶2022年6月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__29/","瀚宇彩晶2022年7月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__32/","瀚宇彩晶2022年8月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__35/","瀚宇彩晶2022年9月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__38/","瀚宇彩晶2022年10月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__41/","瀚宇彩晶2022年11月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__44/","瀚宇彩晶2022年12月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__48/","瀚宇彩晶2023年1月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__49/","瀚宇彩晶2023年2月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__51/","瀚宇彩晶2023年3月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__52/","瀚宇彩晶2023年4月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__56/","瀚宇彩晶2023年5月份營收報告"),
# ("https://www.hannstar.com/news-detail/113__59/","瀚宇彩晶2023年6月份營收報告")
#     # 添加更多的文件名和URL组合
# ]


# # # 遍历每组文件名和URL，并调用process_file函数
# for url, filename in file_url_pairs_news:
#     crawler_news(url,filename)






#financials營業報告新聞稿
# 假设有多组文件名和URL
file_url_pairs_financials = [
("https://www.hannstar.com/news-detail/financial_2021Q1/","瀚宇彩晶2021_1Q營業報告新聞稿")

    # 添加更多的文件名和URL组合
]


# 遍历每组文件名和URL，并调用process_file函数
for url, filename in file_url_pairs_financials:
    crawler_financials(url,filename)