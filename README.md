# auto_academic_timetable
for the best academic schedule, making timetable automatically, according to credits, elective classes, professor and class day.

whenever before the start of the semester, I have a hard time to make the best timetable.   
So I want to make "automatically making the best academic timetable that meets the conditions I put in.   

Right now I made UI, web screping to extract lecture planner but I have a difficult to make algorithm.(making the best academic timetable)   

It will be developed later.   

* **제작자 : 정우진(Woo)**
* **중간 제작 일 : 20.11.04**
* **보고서 작성 일 : 22.07.19**


## Description

개강 시즌이 다가옴에 따라 시간표를 짜던 중 내가 원하는 조건을 모두 만족하는 시간표 짜기에 어려웠다.    
따라서 인공지능의 힘을 빌려(?) 내가 입력한 조건을 모두 만족하는 다양한 시간표를 모두 보여주는 시스템을 만들어,    
이 중에 내가 원하는 시간표만 선택하는 방식으로 해결하고자 하였다.   

시간표는 에브리타임 홈페이지에서 자동 스크롤을 통해 다운을 한다. 그 후 학과를 선택하면 된다.   
원하는 교수님이 있다면 선택해서 입력하고, 강의가 있다면 선택해서 모두 넣기로 한다.    
그 밖에 시간표 짤때 중요한 조건들을 입력해주면 (오전시간 피하기, 최대학점 21학점 채우기, 연강 최대한 피하기 등등)
자동으로 이에 맞는 여러 시간표를 찾아서 보여준다.   

이것이 내가 고안한 프로그램이다.    

그러나 현재 시간표를 웹 스크래핑으로 가져오는 것과, UI를 통해 조건을 입력받는것을 모두 완성시켰지만   
젤 중요한 시간표 짜는 알고리즘을 구현하지 못했다.   
이번 기회에 구현해보고자 한다. 

## Environment
실행에 필요한 package이다.   

* python 3.8.10
* tkinter, csv, webbrowser
* selenium (to download latest selenium chromedriver [download_link](https://sites.google.com/chromium.org/driver/)), bs4
* openpyxl
  
## Files
작성한 코드가 각자 어떤 역할을 하는지 설명해준다. 
1. 1_layout.py
    * UI를 나타내는 코드. 
	* 학과 선택, 등 시간표를 짜기 위한 여러가지 설정을 정하기 위한 UI이다. 
	
2. 2_data_loader.py
    * Everytime 홈페이지를 통해 시간표를 다운받는 코드
	* Selenium과 chromedriver을 통해 시간표 data를 다운한다. 
	
3. 3_main.py
    * 전체적인 코드를 통합한 코드
	* 각 코드를 연결하기 위한 코드이다. (main) - 미완성
	
4. 4_timetable.py
    * 완성된 시간표를 시각적으로 표현하기 위한 코드
	* Excel을 통해 시각적으로 표현해본다. - 미완성

## Usage
작품을 실행하기 위한 방법에 대해 설명한다.   

1. 2_data_loader.py를 통해 학교 시간표 law data를 다운 받는다. 

|데이터 수집 장면|
|--|
|![nn](/image/data_loader.png)|


2. 1_layout.py를 통해 UI를 열어 시간표를 설정하기 위한 여러 조건들을 입력한다.   

|(1) 처음화면|(2) 전공선택|(3) 전공선택 완료|(4) main화면|
|--|--|--|--|
|![nn](/image/main_img.png)|![nn](/image/subject_select.png)|![nn](/image/subject_select_1.png)|![nn](/image/complete_1.png)|  

|(5) 상세선택화면|(6) 교수, 과목 검색|(7) 과목 선택완료|(8) main화면|
|--|--|--|--|
|![nn](/image/pro_lec_select.png)|![nn](/image/pro_lec_select_1.png)|![nn](/image/pro_lec_select_2.png)|![nn](/image/complete_2.png)|   

|(9) 기타 조건 선택|(10) main화면|
|--|--|
|![nn](/image/complete_3.png)|![nn](/image/complete_4.png)|

3. 입력된 조건들을 통합해 4_timetable.py로 시각적으로 표현한다.    

이 모든것을 3_main.py로 통합할 예정이다. 

---------------------------------------------------------

## 개발 과정

개발하면서 크게 어려웠던 점을 순서대로 나열하고 해결방법은 아래에 작성한다.

첫날.
1. gui를 구상해보고 짜봄. 자꾸 2번째 frame에서 표시가 안됐음. 원인을 찾다가
2. 다음날에 .pack()을 안했다는 사실을 알고 gui 전체 마무리 작업 함
3. 데이터 정보 다운로드 하기 위해서 bs4사용함. 에타 로그인하는 방법까지 함. (자꾸 로그인 검색 누르기 등 방법을 찾기 어려워 찾음)
4. 이번엔 작은 창의 스크롤 내리기 방법을 고색하다가 겨우 찾아냄
5. 정보 업로더 완성
6. 버튼 하나하나 명령어 넣기 시작. 과 검색버튼 만들기 . 새로운 창을 만드는 방법을 찾다가 만듦.
7. 만들다가 개편이 필요해 보여 gui등 여러 버튼 동작이나 설명을 바꿈
8. 교수님/강의 버튼 gui만듦(radiobutton 포함)
9. 정보 업로드에 이상한 정보가 포함되어있다는 것을 알게된 후 업로드 코드 개편
10. treeview를 배우고(csv파일 내용을 표로 표시하기 위해 필요) gui 고민, 개편
11. treeview 첫 번째 입력. (정보 넣는 방법을 알게 됨.) / 정보 업로드에 index번호 포함시킴. 
12. 11/8일 treeview 및 교수님/강의 gui 완성 treeview 유투브 보고 공부함
13. get_children을 사용해 선택된 항목이 중복된 것이 있으면 오류나게 하거나 등 오류 처리 완료
그밖의 모든 창의 버튼을 명령 생성 / 교수님/강의 gui 완성! -> 20.11.04일

