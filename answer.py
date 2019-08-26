import random

from contant import DIGIT, MAX_NUMBER
from number import printNumbers

class Answer:
    '''
    중복되지 않는 세 개의 수로 이루어진 정답
    '''

    def __init__(self):
        self.__numbers = [0] * DIGIT  # [0, 0, 0]


    def generate(self):
        while True:
            for i in range(DIGIT):
                self.__numbers[i] = random.randrange(0, MAX_NUMBER)

            if self.__numbers[0] != self.__numbers[1] and self.__numbers[1] != self.__numbers[2] and self.__numbers[2] != self.__numbers[0]:
                break

        printNumbers("[정답]", self.__numbers)

    def __getitem__(self, item):
        '''
        [] 연산자를 재정의한다.
        :param item:
        :return:
        '''
        return self.__numbers[item]
