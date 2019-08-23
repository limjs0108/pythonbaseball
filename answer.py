import random

from contant import DIGIT, MAX_NUMBER
from number import printNumbers


def generateAnswers():
    answers = [0] * DIGIT  # [0, 0, 0]

    while True:
        for i in range(DIGIT):
            answers[i] = random.randrange(0, MAX_NUMBER)

        if answers[0] != answers[1] and answers[1] != answers[2] and answers[2] != answers[0]:
            break

    printNumbers("[정답]", answers)

    return answers
