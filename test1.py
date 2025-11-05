import random

print(random.random())

num = random.randint(1, 9) # 1부터 9 사이의 숫자를 반환 
print(num)

random.seed(1) # seed값을 1로 정의
num = random.randint(1, 100) # 1부터 100사이의 숫자를 반환
print(num) # 어떤 시간, 컴퓨터에서 실행해도 결과는 18로 동일

import math

# 원주율 𝛑 
print(math.pi) # 3.141592653589793
# 자연상수 e
print(math.e) # 2.718281828459045
# 무한대
print(math.inf) # inf
math.gcd(10, 8) # 2 최대 공약수
math.ceil(math.pi) # 4 올림
math.floor(math.e) # 2 내림
math.sqrt(25) # 5 제곱근
math.fabs(-1.5) # 1.5 절댓값

a = -10
print(abs(a)) # 10
print(math.fabs(a)) # 10.0

b = -10.5
print(abs(b)) # 10.5
print(math.fabs(b)) # 10.5


x = 45
math.sin(x) # 사인
math.cos(x) # 코사인
math.tan(x) # 탄젠트


from datetime import datetime
datetime.now() # 현재의 날짜, 시간을 알 수 있다.
print(datetime.now())

today = datetime.now() # 현재의 시간 가져오기
year = today.year # 현재의 년도 가져오기
month = today.month # 현재의 월 가져오기
day = today.day # 현재의 날짜 가져오기
hour = today.hour # 현재의 시간 가져오기
minute = today.minute # 현재의 분 가져오기
second = today.second # 현재의 초 가져오기
ms = today.microsecond # 현재의 마이크로세컨드 가져오기

print(f"{year}년 {month}월 {day}일 {hour}시 {minute}분 {second}초 {ms} 밀리초")

import time as t # time 모듈을 앞으로 t라는 별명으로 부르겠다고 정의

print(t.time())

import calendar 
print(calendar.calendar(2023)) # 2023년 전체 달력을 보여준다