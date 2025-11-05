gift = ['장난감', '동화책']
food = ['불고기', '피자']

newArr = gift + food
print(newArr)

gift.extend(food)
print(gift)

gift.append(food)
print(gift)

food = food * 2
print(food)

arr = [0] * 10 # 0으로 10개 넣는거
print(arr)

gift = ['장난감', '동화책']
print("총 선물의 개수 =", len(gift)) # 총 선물의 개수 = 2

math_score = [30, 70, 80, 60, 80, 90, 80, 85]
print(math_score.count(80)) # 3

myList = []
for i in range(1, 10):
  myList.append(i * i)

print(myList)

myList2 = [i * i for i in range(1, 10)]
print(myList2)

num = 5
my_list = [[num * i + j for j in range(num)] for i in range(num)]
print(my_list)

# 리스트 정렬
scores = [60, 95, 75, 85, 90]
scores.sort() # 원본 배열이 바뀜
print(scores)

scores = [60, 95, 75, 85, 90]
scores.sort(reverse=True)  # reverse 반대로 정렬
print(scores)


scores = [60, 95, 75, 85, 90]
sorted_scores = sorted(scores) # sorted() 원본 배열은 안바뀜
print(scores)
print(sorted_scores)

scores = [60, 95, 75, 85, 90]
sorted_scores = sorted(scores, reverse=True)
print(scores)
print(sorted_scores)

# 리스트 뒤집기
scores = [60, 95, 75, 85, 90]
print(scores[::-1]) # [90, 85, 75, 95, 60]

scores.reverse() # reverse() 원본 배열이 바뀜
print(scores) # [90, 85, 75, 95, 60]

scores = [60, 95, 75, 85, 90]
reversed_scores = list(reversed(scores)) # reversed() 사용시 원본 배열은 안뒤집힘

print(scores) # [90, 85, 75, 95, 60]
print(reversed_scores)

arr = [[3, 6], [7, 8], [2, 9], [6, 4], [9, 3]]

score = 0
for a, b in arr:
    result = int(input(f'{a} * {b} = ? '))
    if result == a * b:
        score += 20
        print("맞았습니다.")
    else:
        print("틀렸습니다.")

print("최종 점수는", score, "점입니다.")