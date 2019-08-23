from contant import DIGIT
from number import printNumbers


def inputGuesses():
    print("\r\n추측을 입력하세요.")
    guesses = [0] * DIGIT  # [0, 0, 0]
    for i in range(DIGIT):
        inputMessage = "[{}] ".format(i + 1)
        value = int(input(inputMessage))
        guesses[i] = value
        # guesses[i] = int(input("[{}}] ".format(i + 1)))

    printNumbers("[추측]", guesses)

    return guesses