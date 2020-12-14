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
따라서 본 프로젝트는 라즈베리파이를 이용한 저가의 하드웨어를 이용하여 음주운전 시도 시 주변 사람들에게 텔레그램으로 알람을 주는 키트를 제작함.

-----------------------------------------------------------------                                                                                                                               
<br>
<br>

## 프로젝트 소개
 
<p align="center"><img src="https://user-images.githubusercontent.com/55028104/101986434-2dd99e00-3cd1-11eb-9627-da640e38ac69.jpg" alt="car" width="800"/></p>    
 <br>
 이번 프로젝트에 제작하게 된 mq3센서를 이용한 차량부착형 알코올 감지키트는 운전자 좌석 차량옆면이나 위에 부착하여 사용한다. 운전자의 날숨에서 알코올을 감지하여 시각적, 청각적으로 알림을 주고 주변 사람들에게 메세지를 보낸다.

-------------------------------------------------------------------

<br>
<br> 

## 사용 품목 
<br>
 <img src="https://user-images.githubusercontent.com/55028104/101988037-b14bbd00-3cda-11eb-9af6-fe8842f54ec7.jpg" alt="sensor"/></p>

 <br>

-------------------------------------------------------------------

<br>
<br> 

## 라즈베리파이 구성도

<br>
 <p align="center"><img src="https://user-images.githubusercontent.com/55028104/101988074-0091ed80-3cdb-11eb-8f6e-930be7482161.png" alt="configuration"/></p>

 <br>
 MQ-3 센서, LED, 부저, 저항을 연결한 브레드보드를 라즈베리파이에 연결한 구성도이다.
-------------------------------------------------------------------
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
<p align="center"><img src="img/problem.jpg alt="drive" width="600"/></p>
 <br>

 <br>
문제점과 해결과정- 저희 프로젝트의 목표가 공기중에 있는 알코올 부지를 감지가 되면 LED와 부저를 이용해서 운전자에게 알려주고 텔레그램을 이용해서 주변지인들에게 알려주는 것이다. 
우선 LED는 문제가 없고 부저에서 문제가 있다.
테스트 결과, 정상적인 오픈소스 코드로 코딩을 진행 해도 소리가 나지 않아, 하드웨어적인 결함이 있다고 판단을 내려서 다른부저로도 테스트 중이다. 
단순히 텔레그램으로 메시지가 보내지나 안보내지나만 테스트 하면 돼서 한 명에게만 보내면 되는데, 그래서 이 부분을 해결하고자 현재 노력 중에 있다.
이 외에는 구현 부분에서 문제점은 없다. 
한계점은 저희 키트를 차량 대쉬보드에 설치를 해야한다는 점인데 텔레그램을 사용하기 위해서는 인터넷에 반드시 연결이 되어 있어야 하고
제도 적인 측면에서도 운전자가 도덕적인 판단으로 측정하지않고 운전을 한다던지 운전자가 설치하지않으면 별 효과가 없다는 단점이 있다
-------------------------------------------------------------------

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

