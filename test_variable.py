# my_age = 12

# def get_american_age(birthday, thatday):
#     this_year, today = int(thatday[:4]), thatday[4:]
#     birth_year, birth_day = int(birthday[:4]), birthday[4:]
#     my_age = this_year - birth_year

#     if today < birth_day:
#         my_age -= 1
#     print("함수 내에서의 만 나이 :", my_age) # 함수 내에서의 만 나이 : 11
#     return my_age

# my_age = get_american_age('20120330', '20230521')
# print("함수 밖에서의 나이 :", my_age) # 함수 밖에서의 나이 : 11



# birthday = '20120330'

# def get_birthday():
#     birthday = '201203301530' # 함수 내에서 사용할 변수 새로 생성
#     print("함수 내에서의 생일 :",birthday)

# get_birthday() # '201203301530'
# print("함수 밖에서의 생일 :",birthday) # '20120330'




birthday = '20120330'

def get_birthday():
  global birthday # 문자열, 숫자 등 불변객체는 함수 밖을 참조할수 있지만 수정은 불가능 > 수정하려면 global 붙이기
  birthday += '1530' # 수정 시 에러 발생
  print(birthday)

get_birthday()


birthday = ['20120330', '20091022']

def get_birthday():
    birthday[0] += '1500' # 리스트, 딕셔너리, 집합같은 가변객체는 global선언 안해도 에러 안남
    print(birthday) # ['201203301500', '20091022']

get_birthday() 
print(birthday) # ['201203301500', '20091022']