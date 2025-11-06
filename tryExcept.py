# try:
#   실행할 문장
# except:
#   예외가 발생할 때 실행할 문장

try:
  a, b = 13, 0
  print(a / b) # 3.0
except ZeroDivisionError as e:    
  print("분모가 0이면 계산할 수 없습니다", e)
except ValueError as e:
  print("두개의 숫자를 입력해야 합니다.", e)

try:
    dan = int(input("구구단 몇 단을 출력할까요?"))
except ValueError as e:
    print("숫자만 입력하세요")
except Exception as e:
    print("에러가 발생 했습니다", type(e))
else:
    for i in range(1, 9 + 1):
        print(f'{dan} * {i} = {dan * i}')


try:
    my_list = ['철수', '영희', '재민']
    num = int(input('사용자 번호를 입력하세요'))
    print(my_list[num])
except:
    print("오류 입니다.")
finally:
    print("finally 문장 입니다.")
print("마지막 문장입니다.")