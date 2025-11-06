money= [['5월1일', 500], ['5월2일', 600], ['5월3일', 300], 
         ['5월4일', 1000], ['5월5일', 200]]

def my_key(m):
  return m[1]

print(max(money, key=my_key)) # max(iterable, key=함수) > 내장 지원 > 함수의 리턴값으로 비교해서 최대값 구하는거 가능

print(max(money, key=lambda m : m[1])) # ['5월4일', 1000]

# def add(x, y):
#   return x + y

# print(add(10, 20)) # 30

# add2 = lambda x, y : x + y

# print(add2(10, 20)) # 30


def showDollar():
  wonToDollar = 0.00074

  dollar = map(lambda m: [m[0], m[1], m[1] * wonToDollar], money)
  print(*dollar)


showDollar()


tmp = [1, 1, 1, 1, 1]
tmp2 = map(lambda n: (n[0] + 1) * n[1], enumerate(tmp))
print(*tmp2)

tmp3 = [100, 200, 300, 400, 500]
print(*filter(lambda n: n <= 300, tmp3))