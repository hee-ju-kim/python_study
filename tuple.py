tu1 = (1, 2, 3)
tu2 = 4, 5, 6
tu3 = ()
tu4 = tuple()
print(type(tu1), tu1) # <class 'tuple'> (1, 2, 3)
print(type(tu2), tu2) # <class 'tuple'> (4, 5, 6)
print(type(tu3), tu3) # <class 'tuple'> ()
print(type(tu4), tu4) # <class 'tuple'> ()

# gift = ('장난감', '운동화') # 튜플 생성
# gift[1] = '게임기' # 변경 시 오류 발생
# del gift[1] # 삭제 시 오류 발생
# gift.append('색연필') # 추가 시 오류 발생

gift = '장난감', '운동화'
g1, g2 = gift # unpacking을 통해 gift를 풀어 각 변수에 대입
print(g1) # 장난감
print(g2) # 운동화
print(gift) # ('장난감', '운동화')
# 리스트나 튜플 앞에 *을 입력하면 unpacking 됩니다.
print(*gift) # '장난감', '운동화'

gift = '장난감', '운동화', '게임기'
print(gift)

toy, *gift = '장난감', '운동화', '게임기'
print(toy) # 장난감
print(*gift) # 운동화 게임기

a = 10
b = 20
print(a, b) # 10 20
a, b = b, a
print(a, b) # 20 10


def get_data():
    a = 10 * 10
    b = 10 + 10
    c = 10 - 10
    return a, b, c

d, e, f = get_data() # 리턴값은 튜플 한 개이다
print(type(get_data())) # <class 'tuple'>
print(d, e, f) # 100 20 0