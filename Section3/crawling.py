from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient

options = Options()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"    #chrome binary location specified here
options.add_argument("--start-maximized") #open Browser in maximized mode
options.add_argument("--no-sandbox") #bypass OS security model
options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)



# driver 실행 및 페이지 접속
# 메모리 부족으로 인해 반씩 나누어 진행
driver = webdriver.Chrome('/Users/seokhwan/OneDrive/sh/cd_states/Project/Section3/chromedriver')
# driver.get('https://search.shopping.naver.com/search/all?query=%EB%85%B8%ED%8A%B8%EB%B6%81&frm=NVSHATC&prevQuery=%EB%85%B8%ED%8A%B8%EB%B6%81')
driver.get('https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&pagingIndex=126&pagingSize=40&productSet=total&query=%EB%85%B8%ED%8A%B8%EB%B6%81&sort=rel&timestamp=&viewType=list')


# result_list : 모든 특성을 가진 노트북 전체 데이터
result_list = []


while len(result_list) < 5000:

    time.sleep(1)

    # 맨 밑까지 스크롤 이동
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  

    time.sleep(1)

    # xpath 로 docu 가져오기
    docu = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div/li')

    # 해당 페이지 html 정보 갖고 오기
    req = driver.page_source
    soup = BeautifulSoup(req, 'html.parser')


    # 각 페이지에 보여지는 제품 종류 만큼 가져오기
    docu = soup.find_all(class_='basicList_item__2XT81')

    # 보여지는 제품 각각의 특성 가져오기
    # docu_rslt : 조회된 하나의 li (상품1개에 대한 전체 정보)
    # all_rslt : 조회된 하나의 노트북에 대한 모든 정보 ()
    docu_rslt = {}
    all_rslt = {}

    for i in docu:
        
        docu_detail = i.find_all(class_='basicList_detail__27Krk')
        item_name = i.find(class_='basicList_title__3P9Q7').find('a').text
        price = i.find(class_='price_num__2WUXn').text                

        for j in docu_detail:
            if ' : ' in j.text:
                col = j.text.split(' : ')[0]
                val = j.text.split(' : ')[1]        
                docu_rslt[col] = val
                # col_set[col] = val
        
        all_rslt["item_name"] = item_name
        all_rslt["price"] = price  
        for col in docu_rslt:
            all_rslt[col] = docu_rslt[col]
        
        result_list.append(all_rslt)
        
        docu_rslt = {}
        all_rslt = {}

    # 한 페이지 내 리뷰 뽑은 후 다음 페이지로 이동
    driver.find_element_by_class_name('pagination_next__1ITTf').click()

# 시간
secs = time.time()+32400
tm = time.localtime(secs)

HOST = 'cluster0.biivj.mongodb.net'
USER = 'ollpp'
PASSWORD = 'Qkrtjrghks12!'
DATABASE_NAME = 'Section3'
COLLECTION_NAME = "naver_db_2022_4_19_15_8"
MONGO_URI = f"mongodb+srv://ollpp:Qkrtjrghks12!@cluster0.biivj.mongodb.net/Section3?retryWrites=true&w=majority"

# client 설정
client = MongoClient(MONGO_URI)
# database 설정
database = client[DATABASE_NAME]
# collection(table) 설정
collection = database[COLLECTION_NAME]
# 데이터 insert
collection.insert_many(result_list)

print(len(result_list))
print("종료")

while(True):
    pass