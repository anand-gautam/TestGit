from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options_chrome = Options()
options_chrome.add_argument("--start-maximized")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options_chrome)

google_url = "https://www.google.com"
search_items = "//*[@role='presentation']//*[@role='option']"
EXCLUDE_LIST = ['testing', 'test', 'selenium', 'interview', 'download', 'tutorial', 'maven', 'dependency', 'seleniumhq', 'ide', 'questions', 'java', 'python', 'webdriver', 'qa']

def google_test_for_partial_keyword_selenium():
    driver.get(google_url)
    time.sleep(3)
    driver.find_element(By.NAME, 'q').send_keys('selenium')
    time.sleep(2)
    items = driver.find_elements(By.XPATH, search_items)
    ls=[]
    for i in range(len(items)):
        search_item = driver.find_element(By.XPATH, '(' + search_items + ')' + '[' + str(i+1) + ']')
        ls.append(search_item.text)
    print(f"Search_list is : {ls}")
    split_list = [i.split() for i in ls[:-1]]
    p_list = []
    for i in split_list:
        if len(i)>1:
            x = i[1:]
        else:
            x=i
        p_list.append(x)
    for i in p_list:
        if len(i)>1:
            for j in i:
                if j.lower() not in EXCLUDE_LIST:
                    print(f"The word '{j}' may not be related to Selenium Testing Library")
        else:
            s_join = ''.join(i)
            if s_join not in EXCLUDE_LIST:
                print(f"The word '{s_join}' may not be related to Selenium Testing Library")

    driver.quit()



google_test_for_partial_keyword_selenium()