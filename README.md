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

* python 3.7.3, cv2 4.1.2
* numpy, RPi.GPIO, PiCamera
* twophase.solver (to install `$ pip install RubikTwoPhase`) 
* Dynamixel_SDK (to install [link](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/download/#repository))
  
## Files
작성한 코드가 각자 어떤 역할을 하는지 설명해준다. 
1. cube_detect_pi.py
    * 큐브 인식하기 위한 알고리즘
	* 이미지 프로세싱 포함
	
2. gpio_control.py
    * LCD화면, LED 등 외부 회로를 제어하기 위한 코드
	* 쓰레드를 사용함
	
3. main.py
    * 전체적인 코드를 통합한 코드
	* 각 코드를 연결하기 위한 코드이다. (main)
	
4. motor_control.py
    * 모터를 제어하기 위한 코드
	* 3개의 모터를 제어해 큐브를 돌린다.

추가적으로 motor제어에 안정화를 위해서 "Dynamixel_SDK"의 다음 라이브러리를 수정했다. 
-> 어떤 내용인지 작성하기

## Usage
작품을 실행하기 위한 방법에 대해 설명한다. 
1. Environment를 참고해 3d 모델을 뽑아 조립한다.
2. 그후 Hardware을 연결한다.
3. Software을 참고해 Raspberry Pi의 환경 세팅한다. 
4. git clone을 통해 CODE 부분을 Raspberry Pi에 저장한다. 
5. 명령창을 CODE의 폴더로 이동해 다음과 같이 명령어를 입력한다. 
```
$ python3 main.py
```
6. 그 후 외부 회로를 만들어 (회로도 참고) 버튼을 클릭해 실행한다. 
7. 만든 로봇을 통해 큐브를 맞춘다!

---------------------------------------------------------
