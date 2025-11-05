print(5 + 3) # 8
print(5 - 3) # 2
print(5 * 3) # 15
print(5 / 3) # 1.66666
print(5 ** 3) # 5 * 5 * 5 = 125
print(5 // 3) # 1 : 5를 3으로 나누면 몫은 1이다
print(5 % 3) # 2 : 5를 3으로 나누면 나머지는 2이다

num = 87
idx = 11
for i in range(9):
    print(num, "*", idx, "=", num * idx)
    idx += 1

print(range(10))
print(*range(10)) #언패키징 > *는 값을 꺼낼때 쓰는 기호


num = 8
for i in range(1, 9+1):
    print(num, "*", i, "=", num * i)

print("거꾸로 출력되는 구구단")
for i in range(9, 0, -1):
    print(num, "*", i, "=", num * i)

print("짝수만 출력되는 구구단")
for i in range(2, 9 + 1, 2):
    print(num, "*", i, "=", num * i)


print("2-9 구구단")
for i in range(1, 10):
  for j in range(2, 10):
    print(f"{j} * {i} = {i*j}\t", end='')
  print()