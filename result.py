from answer import Answer
from contant import DIGIT
from guess import Guess


class Result:
    def __init__(self):
        self.strike = 0
        self.ball = 0
        self.out = 0

    def print(self):
        # [결과] S=1 B=2 O=0
        print("\r\n[결과] S={} B={} O={}".format(self.strike, self.ball, self.out))

    def isCorrect(self):
        return self.strike == DIGIT

    def calculate(self, answer: Answer, guess: Guess):
        for i in range(DIGIT):
            j = (i + 1) % DIGIT
            k = (i + 2) % DIGIT

            if guess[i] == answer[i]:
                self.strike += 1
            elif guess[i] == answer[j] or guess[i] == answer[k]:
                self.ball += 1
            else:
                self.out += 1

