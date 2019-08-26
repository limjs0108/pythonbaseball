import random

from contant import DIGIT, MAX_NUMBER
from number import NumberContainer


class Answer(NumberContainer):
    def generate(self):
        while True:
            for i in range(DIGIT):
                self._numbers[i] = random.randrange(0, MAX_NUMBER)

            if self._numbers[0] != self._numbers[1] and self._numbers[1] != self._numbers[2] and self._numbers[2] != self._numbers[0]:
                break

        self.printWithPrefix("[정답]")
