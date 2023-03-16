class SquidGame:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        if age > 40:
            raise ValueError("나이가 40세를 넘었습니다!")
        self.age: int = age

    @property
    def age(self, age) -> int:
        return self.age
    
    @age.setter
    def age(self, age):
        if self.age > 40 and isinstance(self.age, int):
            raise ValueError("나이가 40세를 넘었습니다!")
        self.age = age

SquidGame("Kyuseong",23)
