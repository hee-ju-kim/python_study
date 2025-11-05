score = 75

if 90 <= score:
  print("매우 잘함")
elif 80 <= score:
  print("잘함")
elif 70 <= score:
  print("보통")
elif 60 <= score:
  print("부족")
else:
  print("매우 부족") 

gender = '여자'
age = 9

if gender == '여자' and age < 10: 
  print("여자아이 입니다") # 여자아이 입니다
else:
  print("여자아이가 아닙니다.")

if gender == '남자' or gender == '여자' or 60 < age or age < 13:
  print("남녀노소입니다") # 남녀노소입니다
else:
  print("남녀노소가 아닙니다.")

check = True

if not check:
  print("거짓입니다.")
else:
  print("참입니다.") # 참입니다.

print(2 * 2 == 4) # True
print(2 * 2 == 3) # False
