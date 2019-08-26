from contant import DIGIT


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

    def calculate(self, answers, guesses):
        for i in range(DIGIT):
            j = (i + 1) % DIGIT
            k = (i + 2) % DIGIT

            if guesses[i] == answers[i]:
                self.strike += 1
            elif guesses[i] == answers[j] or guesses[i] == answers[k]:
                self.ball += 1
            else:
                self.out += 1

