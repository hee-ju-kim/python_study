a = {}
print("a =", a, ", a type =", type(a)) 
# a = {} , a type = <class 'dict'>

b = dict()
print("b =", b, ", b type =", type(b)) 
# b = {} , b type = <class 'dict'>

scores = dict(국어=80, 영어=75, 수학=80, 과학=85)

for key in scores.keys():
  print(f'{key} = {scores[key]}')

for value in scores.values():
  print(value)

for k, v in scores.items():
  print(k, v)


from functools import reduce

result = reduce(lambda acc, cur: acc + cur, scores.values(), 0)
print(result)

result2 = sum(scores.values())
print(result2)

print(result2 / len(scores))

del scores['국어']

if '국어' not in scores:
  print('no')
else:
  print(scores)