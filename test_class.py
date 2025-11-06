class 붕어빵틀:
  pass

붕어빵 = 붕어빵틀()
붕어빵.동네 = '수원시'
붕어빵.종류 = '슈크림'
붕어빵.가격 = 1000

print(f'{붕어빵.동네} 붕어빵 종류 = {붕어빵.종류}, 가격 = {붕어빵.가격}') 

붕어빵2 = 붕어빵틀()
붕어빵2.동네 = '수원시'
붕어빵2.종류 = '팥'
붕어빵2.가격 = 1100

def print_bread(붕어빵):
  print(f'{붕어빵.동네} 붕어빵 종류 = {붕어빵.종류}, 가격 = {붕어빵.가격}') 

print_bread(붕어빵2)

# 붕어빵3 = 붕어빵틀()
# 붕어빵3.종류 = '초코'
# 붕어빵3.가격 = 1100

# print_bread(붕어빵3) # 오류 발생

class 붕어빵틀:
  def 초기화(self, 동네, 종류, 가격):
    self.동네 = 동네
    self.종류 = 종류
    self.가격 = 가격

붕어빵 = 붕어빵틀()
붕어빵.초기화('수원시', '슈크림', 1000)

print_bread(붕어빵)


class 붕어빵틀2:
  def __init__(self, 동네, 종류, 가격):
    self.동네 = 동네
    self.종류 = 종류
    self.가격 = 가격

붕어빵3 = 붕어빵틀2('수원시2', '팥', 1100)
print_bread(붕어빵3)

import random

class Hero:
  def __init__(self, name, health, mana, power):
    self.name = name
    self.health = health
    self.mana = mana 
    self.power = power
    self.x = 100
    self.y = 100
    self.stamina = 100
    
  def __str__(self):
    return f'{self.name}의 체력 = {self.health}, 공격력 = {self.power}, 마나 = {self.mana}'
  def __add__(self, value):
    self.health += value
    return self
  def move(self, x, y):
    self.x += x
    self.y += y

    print(f'{self.name}가 x로 {x}만큼, y로 {y}만큼 움직입니다.')
    print(f'{self.name}의 현재 위치 = {self.x}, {self.y}')

  def say_message(self, message):
    print(f'{self.name} : {message}')

  def attack(self, to_name):
    stamina = 10
    if self.stamina < stamina:
        print(f'{self.name}의 스테미너가 부족합니다.') 
        return 0, 0

    if random.random() < 0.2:
        print(f'{to_name}이 {self.name}의 공격을 회피합니다.')
        return 0, 0

    print(f'{self.name}이 {self.power}의 공격력으로 {to_name}을 공격합니다.')
    print(f'{self.name}의 스테미너가 {stamina} 줄어 듭니다.')
    print(f'{self.name}의 현재 스테미너 : {self.stamina - stamina}')

    return self.power


davin = Hero('다빈공주', 100, 20, 20)
leo = Hero('레오왕자', 120, 10, 30)

print(davin.name) # 다빈공주
print(leo.power) # 30


print(davin)
davin += 10
print(davin) # 다빈공주의 체력 = 110, 공격력 = 20, 마나 = 20

davin = Hero('다빈공주', 100, 20, 20)
davin.say_message('안녕!') # 다빈공주 : 안녕!
davin.move(5, -10) # 다빈공주가 x로 5만큼, y로 -10만큼 움직입니다.
                   # 다빈공주의 현재 위치 : x = 105, y = 90
davin.say_message('레오 왕자 반가워!!') # 다빈공주 : 레오 왕자 반가워!!

mon_name = '작은트롤'
mon_health = 50
damege = davin.attack(mon_name)
mon_health -= damege
print(f'{mon_name}의 현재 체력 : {mon_health}')