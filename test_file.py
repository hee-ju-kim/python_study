# 문자	의미
# 'w'	파일 쓰기 및 생성용. 기존 파일은 삭제
# 'r'	파일 읽기용으로 열기(기본값)
# 'a'	기존 파일 뒤에 추가용으로 열기
# 't'	텍스트 모드(기본값)
# 'b'	바이너리 모드
# 'x'	파일이 이미 있으면 에러. 없으면 생성
# '+'	읽기, 쓰기 모두 가능한 용도로 열기

import os

my_dict = {'apple':'사과', 'banana':'바나나', 'peach':'복숭아'}
file_name = "new_file.txt"
mode = 'w'

if os.path.exists(file_name):
    mode = 'r'

with open(file_name, mode, encoding='utf-8') as my_file:
  if mode == 'w':
    for k, v in my_dict.items():
        my_file.write(f'{k} {v}\n')
  else:
    # file_content = my_file.read()
    # print(file_content)

    tmp = {}
    for line in my_file.readlines():
      key, value = line.split()
      print(key, value)
      tmp[key] = value

    print(tmp)

import csv
import pandas as pd

data = [['이름', '나이'], ['철수', 20], ['영희', 22]]
csv_name = 'people.csv'
mode = 'w'

if os.path.exists(csv_name):
    mode = 'r'

with open(csv_name, mode, newline='', encoding='utf-8') as f:
  if mode == 'w':
    writer = csv.writer(f)
    writer.writerows(data)
  else:
    df = pd.read_csv(csv_name, encoding='utf-8')
    data = df.to_dict(orient='records')

    print(data)