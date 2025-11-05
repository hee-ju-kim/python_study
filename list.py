a = []
b = list()

print(type(a))
print(type(b))

a = [1, 2, 3, 4, 5]
print(a[1])

gifts = ['장난감', '케이크', '동화책', '운동화', '가방']

for gift in gifts:
  print(gift)

for i in range(len(gifts)):
  print(f"{i + 1}번째: {gifts[i]}")

for i, gift in enumerate(gifts):
  print(f"{i + 1}번째: {gift}")

print("두 번째 선물부터 네 번째 선물 =", gifts[1:4]) # ['케이크', '동화책', '운동화']

print(gifts[:4])  # ['장난감', '케이크', '동화책', '운동화']
print(gifts[0:4]) # ['장난감', '케이크', '동화책', '운동화']

print(gifts[2:len(gifts)]) # ['동화책', '운동화', '가방']
print(gifts[2:5]) # ['동화책', '운동화', '가방']
print(gifts[2:])  # ['동화책', '운동화', '가방']

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr[1:8]) # [2, 3, 4, 5, 6, 7, 8]
print(arr[1:8:2]) # [2, 4, 6, 8]

print(arr[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(arr[::-3]) # [10, 7, 4, 1]

gift = ['장난감', '케이크', '동화책', '운동화', '가방']

def print_menu():
    print("*" * 20)
    print("레오의 선물 리스트!!")
    print("무엇을 할까요?")
    print("1. 선물 갯수 보기")
    print("2. 선물 전체 보기")
    print("3. 정해진 순서의 선물 보기")
    print("4. 정해진 범위의 선물 보기")
    print("0. 끝내기")

num = 1 # 초기값을 0이 아닌 것으로 하여 while문을 실행한다
while num != 0: # 0의 입력이 들어오면 끝낸다
    print_menu()
    num = int(input())
    if num == 1:
        print(len(gift), "개")
    elif num == 2:
        print(gift)
    elif num == 3:
        idx = int(input("몇 번째 선물을 볼까요?")) - 1
        print(gift[idx])
    elif num == 4:
        slice_start = int(input("몇 번째 선물부터 확인할까요?")) - 1 
        slice_end = int(input("몇 번째 선물까지 볼까요?")) 
        print(gift[slice_start : slice_end])

gift.append('게임기')
print(gift)

gift.insert(1, "색연필")
print(gift)


del gift[1]
print(gift)

del gift[1:4]
print(gift)

gift.remove('가방')
print(gift)

if "색연필" in gifts:
  print("색연필이 있습니다.")
else:
  print("색연필이 없습니다.")

if "동화책" in gifts:
  print("동화책이 있습니다.")
else:
  print("동화책이 없습니다.")


arr = [1, 2, 3, 4, 5]
temp = arr.pop()
print(temp) # 5
print(arr) # [1, 2, 3, 4]
temp = arr.pop(0)
print(temp) # 1
print(arr) # [2, 3, 4]