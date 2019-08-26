from answer import Answer
from contant import DIGIT
from guess import Guess


class Result:
    def __init__(self):
        self.__strike = 0
        self.__ball = 0
        self.__out = 0

    def print(self):
        # [결과] S=1 B=2 O=0
        print("\r\n[결과] S={} B={} O={}".format(self.__strike, self.__ball, self.__out))

    def isCorrect(self):
        return self.__strike == DIGIT

    def calculate(self, answer: Answer, guess: Guess):
        for i in range(DIGIT):
            j = (i + 1) % DIGIT
            k = (i + 2) % DIGIT

            if guess[i] == answer[i]:
                self.__strike += 1
            elif guess[i] == answer[j] or guess[i] == answer[k]:
                self.__ball += 1
            else:
                self.__out += 1

