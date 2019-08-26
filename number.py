from contant import DIGIT


class NumberContainer:
    def __init__(self):
        self._numbers = [0] * DIGIT  # [0, 0, 0]

    def printWithPrefix(self, prefix):
        print(prefix)
        for i in range(DIGIT):
            print(self._numbers[i], end=" ")

    def __getitem__(self, item):
        '''
        [] 연산자를 재정의한다.
        :param item:
        :return:
        '''
        return self._numbers[item]
