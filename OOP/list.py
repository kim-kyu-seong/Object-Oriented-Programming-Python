#list 와 List 의 차이
#datetime이 안 와지나?
list()
[]
from datetime import datetime
from typing import List

class TrainingData:
    def __init__(self) -> None:
        self.name : str
        self.datetime : datetime

class Sample:
    def __init__(self) -> None:
        self.sepal_length : float
        self.sepal_width : float
        self.petal_length : float
        self.petal_length : float

    def move(self) -> List[tuple[str, int]]:
        return NotImplementedError
#리스트 안에 구조는 맞춰서 알아서 설정 하는 거고


#List[sample]