from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import csv

# 初始化浏览器
driver = webdriver.Chrome()
driver.get("https://appgallery.huawei.com/app/C10194368")
driver.maximize_window()

# 等待加载出“更多”按钮
sleep(20)

soup = BeautifulSoup(driver.page_source, 'html.parser')

list_container = soup.select('div.comment_item')

reviews = []

for review in list_container:
    review_soup = BeautifulSoup(str(review), 'html.parser')
    content = review_soup.select('.part_middle')
    review_content = content[0].text.strip()
    user = review_soup.select('.userName')
    review_userName = user[0].text.strip()
    phoneName = review_soup.select('.deviceName span')
    review_phoneName = phoneName[0].text.strip()
    date = review_soup.select('.deviceName .right')
    review_date = date[0].text.strip()
    score = review_soup.select('div.newStarBox')
    str_score = BeautifulSoup(str(score), 'html.parser')
    img = str_score.select('img', {'src': 'data:image/svg+xml;base64,PD94bWwg...'})
    point = len(img)
    if img:
        point += 1
    else:
        point = 0
    print(review_userName, review_content, review_phoneName, review_date, point)
    reviews.append({'内容': review_content, '名称': review_userName, '手机型号': review_phoneName, '评论日期': review_date, '评分': point})

driver.quit()
keys = reviews[0].keys()
with open('小红书评论.csv', 'w', newline='', encoding='utf-8-sig') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(reviews)
