import random

MAX_NUMBER = 10 # constant
DIGIT = 3

# 1. 0-9 사이의 중복되지 않는 난수 3가지를 골라서 정답을 생성

answers = [0] * DIGIT #[0, 0, 0]

while True:
    for i in range(DIGIT):
        answers[i] = random.randrange(0, MAX_NUMBER)

    if answers[0] != answers[1] and answers[1] != answers[2] and answers[2] != answers[0]:
        break

print("[정답]")
for i in range(DIGIT):
    print(answers[i], end=" ")

tryCount = 0

while True:
    tryCount += 1

    # 2. 사용자로부터 3개의 숫자(추측)을 입력 받음
    print("\r\n추측을 입력하세요.")
    guesses = [0] * DIGIT # [0, 0, 0]
    for i in range(DIGIT):
        inputMessage = "[{}] ".format(i + 1)
        value = int(input(inputMessage))
        guesses[i] = value
        #guesses[i] = int(input("[{}}] ".format(i + 1)))

    print("[추측]")
    for i in range(DIGIT):
        print(guesses[i], end=" ")


    # 3. 정답과 추측을 비교하여 결과 판정
    strike = 0
    ball = 0
    out = 0

    for i in range(DIGIT):
        j = (i + 1) % DIGIT
        k = (i + 2) % DIGIT

        if guesses[i] == answers[i]:
            strike += 1
        elif guesses[i] == answers[j] or guesses[i] == answers[k]:
            ball += 1
        else:
            out += 1


    # 4. 결과를 화면에 출력
    print("\r\n[결과] S={} B={} O={}".format(strike, ball, out)) # [결과] S=1 B=2 O=0


    # 5. 추측이 결과와 다르면 2번 단계로 돌아가서 반복
    if strike == DIGIT:
        break


# 6. 정답을 맞추는데 소요된 횟수를 출력하고 종료
print("[횟수] : {}".format(tryCount))