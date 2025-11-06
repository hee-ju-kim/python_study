# 얕은복사

import copy

# copy 모듈 
my_list = [85, 95, 60, 75]
check_list = copy.copy(my_list)
check_list[1:3] = [30, 40, 50, 60]
print("my_list id =", id(my_list), ", data =", my_list) 
# id = 140045090847152 , data = [85, 95, 60, 75]
print("check_list id =", id(check_list), ", data =", check_list) 
# id = 140045029395424 , data = [85, 30, 40, 50, 60, 75]

# copy() 
my_list2 = [85, 95, 60, 75]
check_list2 = my_list2.copy()
check_list2.sort()
print("my_list2 id =", id(my_list2), ", data =", my_list2) 
# id = 140045090847152 , data = [85, 95, 60, 75]
print("check_list2 id =", id(check_list2), ", data =", check_list2) 
# id = 140045029395424 , data = [60, 75, 85, 95]


# 슬라이싱
my_list3 = [85, 95, 60, 75]

check_list3 = my_list3[:]

del check_list3[1::2]
print("my_list3 id =", id(my_list3), ", data =", my_list3) 
# id = 140045090847152 , data = [85, 95, 60, 75]
print("check_list3 id =", id(check_list3), ", data =", check_list3) 
# id = 140045029395424 , data = [85, 60]

my_score = [[30, 40, 50], [60, 70, 80]]

check_score = my_score.copy()
my_score[0] = [40, 50, 60]

print(my_score)     # [[40, 50, 60], [60, 70, 80]]
print(check_score)  # [[30, 40, 50], [60, 70, 80]]

# 2차 리스트는 얕은복사로는 X
my_score[1][2] = 100

print(my_score)     # [[40, 50, 60], [60, 70, 100]]
print(check_score)  # [[30, 40, 50], [60, 70, 100]]


# 깊은복사

# copy 모듈 
my_score = [[30, 40, 50], [60, 70, 80]]

check_score = copy.deepcopy(my_score)

my_score[1][2] = 100

print(my_score)     # [[30, 40, 50], [60, 70, 100]]
print(check_score)  # [[30, 40, 50], [60, 70, 80]]


# 슬라이싱, 반복문

my_score2 = [[30, 40, 50], [60, 70, 80]]

check_score2 = [row[:] for row in my_score2]

my_score2[1][1] = [50, 75]

print(my_score2)     # [[30, 40, 50], [60, [50, 75], 80]]
print(check_score2)  # [[30, 40, 50], [60, 70, 80]]

N = 3
arr = [[] * (N+1)] * (N+1)
arr[1].append(2)
arr[2].append(3)
arr[3].append(4)

print(arr)


N = 3
arr = [[] * (N+1) for _ in range(N+1)]
arr[1].append(2)
arr[2].append(3)
arr[3].append(4)

print(arr)