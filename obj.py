# 가변객체

my_list = [60, 95, 85, 75]
check_list = my_list
check_list.sort()

print(my_list) # [60, 75, 85, 95]
print(check_list) # [60, 75, 85, 95]

print(id(my_list)) 
print(id(check_list)) 

# 불변객체

my_score = 80
change_score = my_score
my_score = 90

print(my_score) # 90
print(change_score) # 80

print(id(my_score))     
print(id(change_score)) 