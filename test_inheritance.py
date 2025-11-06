# 상속

class Human:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.stamina = 100

    def __str__(self):
        return f'{self.name}의 체력 = {self.health}, 공격력 = {self.power}'

    def move(self, x, y):
        print(f'{self.name}가 x방향 {x}만큼, y방향 {y}만큼 움직입니다.')

    def say_message(self, message):
        print(f'{self.name} : {message}')

class Hero(Human):
    def __init__(self, name, health, mana, power):
        super().__init__(name, health, power)
        self.mana = mana 

class Monster(Human):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
    def say_message(self, message):
        print(f'{self.name}이 "{message}" 하며 짖습니다.')


davin = Hero('다빈공주', 100, 20, 20)
small_troll = Monster('작은트롤', 50, 30)



small_troll.move(-10, -5)
small_troll.say_message('크르르르....')





# 오버라이딩

class 부모클래스:
    def prt(self):
        print("부모 클래스 메서도 입니다.")

class 자식클래스(부모클래스):
    pass

child = 자식클래스()
child.prt()

class 자식클래스(부모클래스):
    def prt(self):
        print("자식 클래스 메서드 입니다.")

child = 자식클래스()
child.prt() # 자식 클래스 메서드 입니다.


# 파이썬은 오버로딩 기본제공X

# 다중상속
# 파이썬은 다중상속 지원

class 부모1:
    pass

class 부모2:
    pass

class 자식클래스(부모1, 부모2):
    pass

print(자식클래스.mro()) # mro() 클래스에서 메서드를 검색할 순서를 보여주는 메서드 > 가장 먼저 발견된 메서드 실행