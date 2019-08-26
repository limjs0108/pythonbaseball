from contant import DIGIT
from number import NumberContainer


class Guess(NumberContainer):
    def input(self):
        print("\r\n추측을 입력하세요.")

        for i in range(DIGIT):
            inputMessage = "[{}] ".format(i + 1)
            value = int(input(inputMessage))
            self._numbers[i] = value
            # guesses[i] = int(input("[{}}] ".format(i + 1)))

        self.printWithPrefix("[추측]")
