import random

MAX_NUMBER = 10 # constant
DIGIT = 3

# 1. 0-9 사이의 중복되지 않는 난수 3가지를 골라서 정답을 생성

answer0 = 0
answer1 = 0
answer2 = 0

while True:
    answer0 = random.randrange(0, MAX_NUMBER) # literal, hard-coded, magic number
    answer1 = random.randrange(0, MAX_NUMBER)
    answer2 = random.randrange(0, MAX_NUMBER)

    if answer0 != answer1 and answer1 != answer2 and answer2 != answer0:
        break

print("[정답]")
print(answer0, end=" ")
print(answer1, end=" ")
print(answer2, end=" ")

tryCount = 0

while True:
    tryCount += 1

    # 2. 사용자로부터 3개의 숫자(추측)을 입력 받음
    print("\r\n추측을 입력하세요.")
    guess0 = int(input("[1] "))
    guess1 = int(input("[2] "))
    guess2 = int(input("[3] "))

    print("[추측]")
    print(guess0, end=" ")
    print(guess1, end=" ")
    print(guess2, end=" ")


    # 3. 정답과 추측을 비교하여 결과 판정
    strike = 0
    ball = 0
    out = 0

    # 3-1. guess0
    if guess0 == answer0:
        strike += 1 # strike = strike + 1
    elif guess0 == answer1 or guess0 == answer2:
        ball += 1
    else:
        out += 1

    # 3-2. guess1
    if guess1 == answer1:
        strike += 1 # strike = strike + 1
    elif guess1 == answer2 or guess1 == answer0:
        ball += 1
    else:
        out += 1

    # 3-3. guess2
    if guess2 == answer2:
        strike += 1 # strike = strike + 1
    elif guess2 == answer0 or guess2 == answer1:
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