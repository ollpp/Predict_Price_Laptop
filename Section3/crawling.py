from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd


# 크롬드라이버 경로 입력
driver = webdriver.Chrome('/Users/seokhwan/OneDrive/sh/cd_states/Project/Section3/chromedriver')
time.sleep(1)


names_all = []
plus = []

# 네이버 쇼핑 노트북 검색 첫화면
driver.get('https://search.shopping.naver.com/search/all?query=%EB%85%B8%ED%8A%B8%EB%B6%81&frm=NVSHATC&prevQuery=%EB%85%B8%ED%8A%B8%EB%B6%81')


while len(review) < 20:

    time.sleep(1)
    # 스크롤 내리기
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(3)
    name = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div/li/div[1]/div[2]/div[1]/a')
    size = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div/li/div/div[2]/div[4]/div[1]/a[1]')
    weight = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div/li/div/div[2]/div[4]/div[1]/a[2]')
    kind = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div/li/div/div[2]/div[4]/div[1]/a[3]')
    out_os = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div/li/div/div[2]/div[4]/div[1]/a[4]')
    cpu = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div/li/div/div[2]/div[4]/div[1]/a[5]')
    chipset = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div/li/div/div[2]/div[4]/div[1]/a[6]')
    core = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div/li/div/div[2]/div[4]/div[1]/a[7]')
    code = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div/li/div/div[2]/div[4]/div[1]/a[8]')
    size = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div/li/div/div[2]/div[4]/div[1]/a[9]')
 


    for i in name:
        names_all.append(i.text)

    time.sleep(3)
    # 한 페이지 내 리뷰 뽑은 후 다음 페이지로 이동
    driver.find_element_by_class_name('pagination_next__1ITTf').click()

breakpoint()
# game_review = pd.DataFrame({'txt':review,'label':None})

# secs = time.time()+32400
# tm = time.localtime(secs)
# time_log = '{0}-{1}-{2}-{3}-{4}-{5}_gameRV'.format(tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec)


# game_review.to_csv('GameRV/%s.csv' %time_log, encoding = 'utf-8-sig')