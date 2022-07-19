from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import csv

#input_user_agent=input('What is your user-agent')
#user_id=input('What is your everytime Id')
#user_pw=input('What is your everytime password')

options=webdriver.ChromeOptions()
options.add_argument("widow-size=1920*1080")
options.add_argument() #add your user-agent

browser=webdriver.Chrome(options=options)
browser.maximize_window() #창 최대화

#페이지 이동
url="https://everytime.kr"
browser.get(url)

#로그인 하기
browser.find_element_by_link_text("로그인").click()
#->id, pw 입력
user_id=#add your everytime ID
user_pw=#add your everytime password
browser.find_element_by_name("userid").send_keys(user_id)
browser.find_element_by_name("password").send_keys(user_pw)
#->로그인 버튼 클릭
browser.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()

#시간표 찾아 모든 정보 다운로드
#->시간표까지 진입
browser.find_element_by_link_text("시간표").click()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="sheet"]/ul/li[3]/a').click()
browser.find_element_by_xpath('//*[@id="container"]/ul/li[1]').click()
time.sleep(2)
#->정보 스크롤 다운
##->soup으로 변환해, 테이블의 가장 마지막 값을 저장/가장 마지막 값이 같을때까지 계속 스크롤
soup=BeautifulSoup(browser.page_source, "lxml")
data_rows=soup.find("div", attrs={"id":"subjects"}).find("tbody").find_all("tr")
element=data_rows[-1]

#반복 스크롤(end키를 눌러 스크롤)
interval=2 #2초마다 스크롤
while True:
    test=browser.find_element_by_xpath('//*[@id="subjects"]/div[2]/table/tbody')
    ActionChains(browser).move_to_element(test).send_keys(Keys.END).perform()    #keys.End를 매번 누르는 형식으로 대처. input으로 입력받는 곳이 없어 actionchain를 사용해 억지로 이용
    time.sleep(interval)

    #테이블의 마지막 값 가져오기
    soup=BeautifulSoup(browser.page_source, "lxml")
    curr_element=soup.find("div", attrs={"id":"subjects"}).find("tbody").find_all("tr")[-1]
    if curr_element==element:
        break
    element=curr_element

#파일 저장
filename="전체수강표.csv"
f=open(filename, "w", encoding="utf-8-sig", newline="")
writer=csv.writer(f)

title="인덱스	계획서	학년	이수구분	과목번호	교과목명	학점	담당교수	강의교시/강의실	강의평	평점링크	담은 인원	정원	수강학과	비고".split("\t") #탭으로 구분된 항목들이 리스트로 들어감
writer.writerow(title)

#파일 정보 가져오기
soup=BeautifulSoup(browser.page_source, "lxml")
data_rows=soup.find("div", attrs={"class":"list"}).find("tbody").find_all("tr")   #리스트 형식으로 모든 td(강의 1개의 모든 내용)가 들어가 있음

num=0
for row in data_rows: #row=한개 강의만 가져온다면,
    data=[]
    num+=1
    data.append(num)
    trash_data=False
    columns=row.find_all("td") #각각 한가지 속성끼리 가져옴/리스트로 저장
    for column in columns: #한개의 속성을 가져온다면, 
        if column.get_text()=="조회":      #조회는 강의세부계획 링크로
            link="https://everytime.kr"+row.find("a", attrs={"class":"syllabus"})["href"]
            data.append(link)
            continue
        if column.get_text()=='':         #평점 가져오기
            if len(data)!=9:
                trash_data=True
                continue
            star=row.find("a", attrs={"class":"star"})["title"]
            data.append(star)
            star_link="https://everytime.kr"+row.find("a", attrs={"class":"star"})["href"]
            data.append(star_link)
            continue
        data.append(column.get_text())
    if trash_data==False:
        writer.writerow(data)
    else:
        num-=1

f.close()
#브라우저 종료
print("정보 수집 완료!")
browser.quit() #전체 브라우저 종료


