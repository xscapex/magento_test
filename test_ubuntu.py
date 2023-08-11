from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


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


get_page_content('https://www.hannstar.com/news-detail/financial_2021Q1/')