num1 = 1
num2 = '2'
num3 = '1.1'

print(type(num1)) # <class 'int'> 
print(type(num2)) # <class 'str'> 
print(type(num3)) # <class 'str'> 

num1 = str(num1) # 숫자를 문자로 변환
num2 = int(num2) # 문자를 정수형으로 변환
num3 = float(num3) # 문자를 실수형으로 변환

print("자료형 변환 후 자료형")
print(type(num1))
print(type(num2))
print(type(num3))


num = input('숫자를 입력하세요')
print(type(num))

num = int(input("몇 단을 출력할까요?"))
for i in range(1, 9+1):
  print(num, "*", i, "=", num * i)
