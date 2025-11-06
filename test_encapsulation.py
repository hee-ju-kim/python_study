# class Human:
#     def __init__(self, name, health, power):
#         self.name = name
#         self.__health = health # 은닉화하려면 앞에 __ 붙이기 > 이럴경우 타 클래스에서 수정 불가
#         self.power = power

#     def __str__(self):
#         return f'{self.name}의 체력 = {self.health}, 공격력 = {self.power}'

# class Hero(Human):
#     def __init__(self, name, health, mana, power):
#         super().__init__(name, health, power)
#         self.mana = mana 

#     def attack(self, other):
#         print(f"{self.name}이(가) {other.name}을 공격합니다.")
#         other.health -= self.power # 여기부분이 에러 

# class Monster(Human):
#     def __init__(self, name, health, power):
#         super().__init__(name, health, power)

# davin = Hero("다빈공주", 100, 20, 20)
# small_troll = Monster('작은트롤', 50, 30)
# davin.attack(small_troll)
# print(small_troll)

class Human:
    def __init__(self, health):
        self.__health = health

    def get_health(self):
        print(f'{self.__health=}')

human = Human(100)
human.__health = 50
print(human.__health) # 50
human.get_health() # self.__health=100

human = Human(100)
print(dir(human))

human.__health = 50
print(human.__health) # 50
human.get_health() # self.__health=100
print(dir(human))

human = Human(100)
human.__health = 50
print(human.__health) # 50
human._Human__health = 50
human.get_health() # self.__health=50