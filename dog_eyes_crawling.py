# 필요한 라이브러리 불러오기
from selenium import webdriver
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import urllib.request
import os

print(2222222222)
# 2. 크롬 웹드라이버 연결
driver=webdriver.Edge(EdgeChromiumDriverManager().install())
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")


print(333333333)
# 3. 검색어 입력하기
search = "강아지눈"
elem = driver.find_element(By.NAME, "q")
elem.send_keys(search)
elem.send_keys(Keys.RETURN)


print(4444444444444)
# 4. 스크롤 끝까지 내리기
SCROLL_PAUSE_TIME = 1

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        try:
            driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
        except:
            break
    last_height = new_height


print(5555555555)
    # 5. 이미지 찾아서 원본 파일로 저장하기
images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
# print(images)
count = 1

#"//*[@id='Sva75c']/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img"

"//*[@id='Sva75c']/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a"
xpath = "//*[@id='Sva75c']/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]"
"//*[@id='Sva75c']/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]"
for image in images:
    try:
        print(image)
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element(By.XPATH, xpath).get_attribute('src')
        print(imgUrl)
        urllib.request.urlretrieve(imgUrl, "./images/" + search + "_" + str(count) + ".jpg")
        print("Image saved: 도라에몽_{}.jpg".format(count))
        count += 1
    except:
        pass

driver.close()