party_set = {3, 6, 10, 7, 3, 18, 5, 2, 15, 6}
print(party_set) # {2, 3, 5, 6, 7, 10, 15, 18}
print(type(party_set)) # <class 'set'>


party_list = [3, 6, 10, 7, 3, 18, 5, 2, 15, 6]
party_set1 = set([3, 6, 10, 7, 3, 18, 5, 2, 15, 6])
party_set2 = set(party_list)
print(party_set1) # {2, 3, 5, 6, 7, 10, 15, 18}
print(party_set2) # {2, 3, 5, 6, 7, 10, 15, 18}

my_set = {3, 6, 10, 7, 3, 18, 5, 2, 15, 6}
print(my_set) # {2, 3, 5, 6, 7, 10, 15, 18}
my_set.add(3) # 기존에 3이 있어 추가 되지 않음
my_set.add(9) # 기존에 없어 9가 추가됨
print(my_set) # {2, 3, 5, 6, 7, 9, 10, 15, 18}

my_set = {3, 6, 10, 7, 3, 18, 5, 2, 15, 6}
print(my_set)
my_set.update([3, 9]) # 3은 중복으로 추가되지 않고, 9만 추가됨
print(my_set)

my_set = {3, 6, 10, 7, 3, 18, 5, 2, 15, 6}
print(my_set) # {2, 3, 5, 6, 7, 10, 15, 18}
my_set.remove(3) # 3을 삭제함
print(my_set) # {2, 5, 6, 7, 10, 15, 18}

my_set = {3, 6, 10, 7, 3, 18, 5, 2, 15, 6}
print(my_set) # {2, 3, 5, 6, 7, 10, 15, 18}
my_set.discard(1) # 기존에 없던 1을 삭제하지만 에러 발생하지 않음
print(my_set) # {2, 3, 5, 6, 7, 10, 15, 18}



# 합집합
my_set1 = {1, 2, 3, 4, 5, 6}
my_set2 = {4, 5, 6, 7, 8, 9}

my_set3 = my_set1.union(my_set2)
my_set4 = my_set1 | my_set2
print(my_set3) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(my_set4) # {1, 2, 3, 4, 5, 6, 7, 8, 9}


# 교집합
my_set1 = {1, 2, 3, 4, 5, 6}
my_set2 = {4, 5, 6, 7, 8, 9}

my_set3 = my_set1.intersection(my_set2)
my_set4 = my_set1 & my_set2
print(my_set3) # {4, 5, 6}
print(my_set4) # {4, 5, 6}

# 차집합
my_set1 = {1, 2, 3, 4, 5, 6}
my_set2 = {4, 5, 6, 7, 8, 9}

my_set3 = my_set1.difference(my_set2)
my_set4 = my_set1 - my_set2
print(my_set3) # {1, 2, 3}
print(my_set4) # {1, 2, 3}



party_list = [3, 6, 10, 7, 3, 18, 5, 11112, 15, 126, 22, 111]
print("원본 리스트 = ", party_list) 
# 원본 리스트 =  [3, 6, 10, 7, 3, 18, 5, 11112, 15, 126, 22, 111]

party_set = set(party_list)
print("중복 제거 집합 = ", party_set) 
# 중복 제거 집합 =  {3, 5, 6, 7, 11112, 10, 15, 111, 18, 22, 126}

party_list2 = list(party_set)
party_list2.sort()
print("정렬된 리스트 =", party_list2) 
# 정렬된 리스트 = [3, 5, 6, 7, 10, 15, 18, 22, 111, 126, 11112]