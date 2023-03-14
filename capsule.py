#캡슐화 #정보은닉 #자바에서 가능 (public private protected)
#클래스 안에서 def선언하면 메소드 밖에서하면 함수
#        self.__age = 23 #__로 은닉. 스페셜 메소드와 닮음..
# #_해당 클래스에서만 사용하자고 약속함
class SquidGame: #객체 생성, 클래스 만들기
    """
    여기에 첨가를 넣어서 협업시에 참조에 예시를 넣어줄 수 있음.
    """
    def __init__(self, name: str, age: int) -> None: #언더바2개를 더던이라고 부르고 스페셜메소드. 생성자
        self.name: str = name #: type -- 타입선언 /파이썬에선 안됨. 리딩에 유용하도록 만듦
        if age > 40:
            raise ValueError("나이가 40세를 넘었습니다!")

        self.age: int = age 

    @property
    def age(self) -> int:
        return self.age

    @age.setter
    def age(self, age)
        if self.age > 40: and isinstance(self.age, str):
            raise ValueError("나이가 40세를 넘었습니다!")
        self.age = age


Squid_game1 = Squid_game("Kyu-seong",23)
Squid_game1.age = 140






#print(Squid_game.age)
#Squid_game.age = 10
#print(Squid_game.age)
#        self._generate_player()

    
#    def _generate_player(self):
#        self._age

#squid_game = SquidGame()
#squid_game.generate_player()
#squid_game.name
# squid_game._age






#if __name__ == "__main__": #C의 메인메소드 선언과 같은 역할
#    capsule = Capsule()
