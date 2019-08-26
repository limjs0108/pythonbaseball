from answer import Answer
from guess import Guess
from result import Result

# 1. 0-9 사이의 중복되지 않는 난수 3가지를 골라서 정답을 생성
answer = Answer()
answer.generate()

tryCount = 0

while True:
    tryCount += 1

    # 2. 사용자로부터 3개의 숫자(추측)을 입력 받음
    guess = Guess()
    guess.input()
    #guesses = inputGuesses()

    # 3. 정답과 추측을 비교하여 결과 판정
    result = Result()
    result.calculate(answer, guess)

    # 4. 결과를 화면에 출력
    result.print()
    #printResult(result)

    # 5. 추측이 결과와 다르면 2번 단계로 돌아가서 반복
    if result.isCorrect():
        break

# 6. 정답을 맞추는데 소요된 횟수를 출력하고 종료
print("[횟수] : {}".format(tryCount))
