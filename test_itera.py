# iterator
# next 사용가능

a = [1, 2, 3, 4, 5]
print(type(a)) # <class 'list'>
it = iter(a)
print(type(it)) # <class 'list_iterator'>

print(f'{next(it)=}') # next(it)=1
print(f'{next(it)=}') # next(it)=2


for ni in it:
  print(f'{ni=}')

# iterable 객체
# next는 사용하지 못하지만 for in문을 사용해서 하나씩 꺼낼 수 있는 객체

# arr = [1, 2, 3, 4, 5]
# print(f'{next(arr)=}') # 에러

from itertools import *

cnt = count(-2, 3)
print(list(islice(cnt, 5)))
print(next(cnt)) # -2
print(next(cnt)) # 1
