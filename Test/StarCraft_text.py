#StarCraft Unit Creater
from random import *

class Unit: #유닛 클래스
    def __init__(self, species: str, name: str, hp: int, speed: int) -> None:
        self.species: str = species #종족
        self.name: str = name #이름
        self.hp: int = hp #체력
        self.speed: int = speed #지상 이동속도
        
    def create(self):
        print("유닛이 생성되었습니다.")
        print("[종족: {0} | 유닛명: {1} | 체력: {2}]".format(self.species, self.name, self.hp))
    
    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
              .format(self.name, location, self.speed))

    def damaged(self, damage: int):
        print("{0} : {1}의 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

        
class AttackUnit(Unit): #공격유닛 클래스 / 유닛 클래스를 상속받음
    def __init__(self, species: str, name: str, hp: int, \
                 speed: int, damage: int) -> None:
        Unit.__init__(self, species, name, hp, speed)
        self.damage: int = damage #공격력

    def info(self):
        print("유닛 정보입니다.")
        print("[{0} 공격력: {1}]".format(self.name, self.damage))

    def attack(self, location: str):
        print("{0} : {1} 방향으로 적을 공격합니다. [공격력 {2}]"\
              .format(self.name, location, self.damage))
        
    def damaged(self, damage: int):
        print("{0} : {1}의 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, species: str, name: str,\
                  hp: int, damage: int, flying_speed: int) -> None:
        AttackUnit.__init__(self, species, name, hp, 0, damage) #지상 speed 0처리
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "테란", "마린", 40, 1, 5)
    
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} 체력이 부족합니다.".format(self.name))

class Tank(AttackUnit):
    seize_developed = False #시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "테란", "탱크", 150, 1, 35)
        self.seize_mode = False
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        #시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True    
        #시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "테란", "레이스", 80, 20, 5)
        self.clocked = False #클로킹 모드

    def clocking(self):
        if self.clocked == True:
            print("{0} 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} 클로킹 모드를 설정합니다.".format(self.name))
            self.clocked = True
    
def game_start():
    print("새로운 게임을 시작합니다.")

def game_over():
    print("[player] : GG")
    print("[player] has been laft")

#게임 시작
game_start()

#마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

#탱크 2기 생성
t1 = Tank()
t2 = Tank()

#레이스 1기
w1 = Wraith()

#유닛 부대지정
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#부대 이동
for unit in attack_units:
    unit.move("1시")

#탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 시즈모드 개발이 완료되었습니다.")

#공격모드 준비
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

#공격
for unit in attack_units:
    unit.attack("1시")

#피해
for unit in attack_units:
    unit.damaged(randint(5,20)) #랜덤으로 데미지 받음


#게임종료
game_over()

