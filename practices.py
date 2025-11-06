# input()으로 사용자로부터 정수를 한 개 입력받아, 그 숫자를 숫자 크기만큼 반복해서 출력하는 파이썬 스크립트를 작성하세요. 이때 출력 앞에 공백을 한 칸 주어서, 입력과 출력이 구분되게 합니다.
# 단, while 문을 사용하세요.

# num = int(input("숫자 입력"))
num = 1

i = 0
sum = 0
while i < num:
  sum += num
  i += 1

print(sum)

# 정수를 한 개 입력받아, 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트하는 프로그램을 작성해 보세요. 단, while 문을 사용하세요.1
i = 1
while i <= num:
  print(f"{i} {i** 2}")
  i += 1

# 고무공을 100 미터 높이에서 떨어뜨리는데, 이 공은 땅에 닿을 때마다 원래 높이의 3/5 만큼 튀어오릅니다. 공이 열 번 튈 동안, 그때마다 공의 높이를 계산합니다.
hei = 100

for i in range(10):
  hei = round(hei * (3/5), 4)
  print(f"{i+1} {hei}")

# 양(陽)의 정수를 입력받아, 그 수가 몇 자리 숫자인지 출력하는 함수 numOfDigits()를 만들어 보세요.

def numOfDigits(num):
  print(len(str(num)))

numOfDigits(12345)
numOfDigits(1234567890)

# 생일 반환
from datetime import datetime
def korean_age(year):
  today = datetime.today()
  print(today.year - year + 1)

korean_age(1996)

# 주어진 단어가 회문인지 판별하는 함수 palindrome()을 작성하세요. 단, 문자열 입력은 모두 소문자로 이뤄지며 공백을 포함하지 않는다고 가정합니다.

def palindrome(s):
  s = s.lower()
  s = s.replace(' ', '')
  print(s[:] == s[::-1])

# palindrome('anna')
# palindrome('banana')
# palindrome('Anna')
palindrome('My gym')


# 정수 num을 매개변수로 받아 각 자리 숫자(digit)의 합을 계산하는 sumOfDigits() 함수를 작성하세요. 단, 나눗셈을 이용하지 말고, 리스트와 map() 함수를 이용해 풀어보세요.

def sumOfDigits(nums): 
  sum = 0
  for i in str(nums):
    sum += int(i)

  print(sum)

sumOfDigits(643)


