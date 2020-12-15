 <p align="center"><img src="https://user-images.githubusercontent.com/55028104/101986756-3cc15000-3cd3-11eb-9458-e2183839231b.PNG" alt="logo"  width="600" />    
 <br>
 <div align="center">

__😎 Team__  
🔥 __BLOCKBUS_TOP__ 🔥  
<br/>

__🥰 Member__  
[사영훈](https://github.com/tkdudgns95) | [유혜상](https://github.com/Yuhye) | [이창해](https://github.com/vip7gain) | [전민수](https://github.com/GodofPig) | [차민재](https://github.com/charmingjae)  

</div>

<br/>

* * *
<br/>


<div align="center">

## __음주운전 방지를 위한 차량부착형 MQ-3 알코올 감지 키트__<br/>
*Vehicle-attached MQ-3 alcohol detection kit for preventing drunk driving*
</div><br/>

* * *
<br/>

## 🚩 __Contents__

1. Abstract
2. 프로젝트 소개
3. 사용 품목
4. 라즈베리파이 구성도
5. 도식화
6. 문제점과 해결과정 
7. 동작 시연
8. Q&A
9. 기대효과

<br>

## Abstract 
<br>
<p align="center"><img src="https://user-images.githubusercontent.com/55028104/101987654-e3f4b600-3cd8-11eb-8a66-434f1d07e1d4.jpeg" alt="drive" width="600"/></p>
 <br>
 
사람들은 음주 후의 운전의 위험함과 심각성을 충분히 인지하고 있지만, 음주운전으로 인한 사고 비율은 [__여전히 높은 추세 이다.__](https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%9D%8C%EC%A3%BC%EC%9A%B4%EC%A0%84)  
따라서 라즈베리파이를 이용하여 가격, 활용 면에서 실용적이고 운전자의 음주운전을 예방하고자 본 프로젝트를 진행하게 되었다.

-----------------------------------------------------------------                                                                                                                               
<br>
<br>

## __프로젝트 소개__
 
<p align="center"><img src="https://user-images.githubusercontent.com/55028104/101986434-2dd99e00-3cd1-11eb-9627-da640e38ac69.jpg" alt="car" width="400"/></p>  
<br/>
본 프로젝트의 주제는 차량 부착형 알코올 감지 키트이다. 운전자의 음주 여부를 판독하기 위해 운전자의 **날숨을 감지할 수 있는** 차량의 대시보드(Dashboard), 핸들 등의 위치에 부착된다.

-------------------------------------------------------------------

<br>
<br> 

## __사용 품목__
<br>
 <img src="https://user-images.githubusercontent.com/55028104/102213357-f90c5780-3f19-11eb-876a-d7ed229707db.jpg" alt="sensor"/></p>

 <br>
**MQ-3 센서** : 알코올 감지를 위한 센서.
**LED** : 시작적으로 운전자에게 알코올 감지 신호를 전달해 주기위함.
**부저** : 청각적으로 운전자에게 알코올 감지 신호를 전달해 주기위함.
**브레드보드** : MQ-3센서와 LED, 부저, 라즈베리파이를 브레드보드를 통해 연결


-------------------------------------------------------------------

<br>
<br> 

## __라즈베리파이 구성도__

<br>
 <p align="center"><img src="https://user-images.githubusercontent.com/55028104/101988074-0091ed80-3cdb-11eb-8f6e-930be7482161.png" alt="configuration"/></p>

 <br>
 MQ-3 센서, LED, 부저, 저항을 연결한 브레드보드를 라즈베리파이에 연결한 구성도이다.
  <br>

<br>
<br> 
 
## 도식화 

<br>
<p align="center"><img src="https://user-images.githubusercontent.com/55028104/101988164-4fd81e00-3cdb-11eb-8034-b2187fb11fb7.PNG" alt="schematization"/></p>

 <br>
먼저 날숨을 MQ-3 센서에서 감지 해 기준 값(Reference) 보다 낮으면 루프를 돌면서 감지한다. 만약 기존 값(Reference) 보다 감지 값(Levels)가 높다면 LED와 부저(Buzzer)가 작동된다. 그 후에 텔레그램으로 운전자의 상태 값이 전송이 된다. 전송을 한 후 LED와 부저는 자동적으로 꺼지며 다시 처음으로 돌아가 날숨을 감지한다.

-------------------------------------------------------------------

<br>
<br>  

## 문제점과 해결과정

<br>
<br>

<br>
문제점과 해결과정
 <br>
<br>
1. 하드웨어적인 결함 - 테스트 결과 정상적인 코드 실행에도 하드웨어적인 결함으로 사운드가 들리지 않는 문제
<br>
<br>
2. 보급의 문제 - 서비스를 이용하기 위해서 해당 기기를 보급하여 차량에 설치해야 한다는 점과 차량내 인터넷이 활성화 되어야 하는 문제
<br>
 <br>
3. 제도,법률,도덕적인 문제 - 서비스를 위한 기기를 운전자가 반드시 설치, 이용해야 한다는 제도,법률적인 조항이 없어,
 <br>
개인의 도덕적인 판단으로 기기 설치와 서비스 이용을 맡겨야 한다는 점에서 궁극적인 프로젝트의 목표인 음주운전 방지에 어려움을 갖을 수 있는 문제
<br>
 

<br>
<br> 

## 동작시연  

<br>
 <img src="" alt=""/>

 <br>

-------------------------------------------------------------------
<br>
<br>

## 기대효과 

<br>
 <img src="" alt=""/>
 
1.LED와 부저를 사용하여 운전자의 음주여부를 시/청각화 가능.


2.텔레그램 메시지 전송을 통해 주변인들의 적극적인 제지 기대.
 
 
-------------------------------------------------------------------

<br>
<br> 
 
<h1 align="center"> Q & A </h1>

 <br>

