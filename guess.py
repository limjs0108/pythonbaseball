from contant import DIGIT
from number import printNumbers

class Guess:
    def __init__(self):
        self.numbers = [0] * DIGIT  # [0, 0, 0]

    def input(self):
        print("\r\n추측을 입력하세요.")

        for i in range(DIGIT):
            inputMessage = "[{}] ".format(i + 1)
            value = int(input(inputMessage))
            self.numbers[i] = value
            # guesses[i] = int(input("[{}}] ".format(i + 1)))

        printNumbers("[추측]", self.numbers)


    def __getitem__(self, item):
        '''
        [] 연산자를 재정의한다.
        :param item:
        :return:
        '''
        return self.numbers[item]
