# 1, 1, 2, 3, 5, 8, 13, 21, 34

num1 = 1
num2 = 1

print(num1,"", end="")
print(num2,"", end="")

for _ in range(10):
  num3 = num1 + num2
  print(f"{num3} ", end="")

  num1 = num2
  num2 = num3