from contant import DIGIT


class Result:
    def __init__(self):
        self.strike = 0
        self.ball = 0
        self.out = 0


def calculateResult(answers, guesses):
    result = Result()

    for i in range(DIGIT):
        j = (i + 1) % DIGIT
        k = (i + 2) % DIGIT

        if guesses[i] == answers[i]:
            result.strike += 1
        elif guesses[i] == answers[j] or guesses[i] == answers[k]:
            result.ball += 1
        else:
            result.out += 1

    return result


def printResult(result):
    # [결과] S=1 B=2 O=0
    print("\r\n[결과] S={} B={} O={}".format(result.strike, result.ball, result.out))


def isCorrectResult(result):
    return result.strike == DIGIT
    # return result.strike == 1 and result.ball == 2
