# def 함수명():
#     함수의 동작 정의하기



def say_hello():
    print("안녕하세요 반갑습니다.")
    print("좋은 하루 보내세요~")

say_hello()

def get_area(width, height):
    area = (width * height) / 2
    return area

tri = get_area(3, 4)
print(tri) # 6

my_name = "다빈치"

def say_hello(name='게스트'):
    print(f'{name}님 안녕하세요')

say_hello(my_name) # 다빈치님 안녕하세요
say_hello() # 게스트님 안녕하세요

# def say_hello(name='게스트', age): # 오류 발생 기본값이있는 파라미터는 뒤쪽으로
#     print(f'{age}살이 되신 {name}님 안녕하세요')

def say_hello(age, name='게스트'): # 이렇게 만들어야 합니다.
    print(f'{age}살이 되신 {name}님 안녕하세요')

say_hello(34)
say_hello(34, '히히')


def add_all(*nums): # 파라미터갯수가 몇개인지 모를때
    result = 0
    for n in nums:
        result += n
    return result

print(add_all(1, 2, 3, 4, 5)) # 15

def my_func(**kwargs): # **는 딕셔너리 파라미터라고 알려주는거
    print(type(kwargs))

my_func(a=1, b=2, c=3) # <class 'dict'>

def factorial(n, s):
    if n == 1:
        print(f'{s}1 =')
        return 1
    s += f'{n} * '
    print(f'{s}factorial({n-1}) =')    
    return n * factorial(n - 1, s)

print(factorial(5, ''))