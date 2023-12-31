# 반복문

# 기본 구조
# while 조건문:
#   수행할_문장1
#   수행할_문장2

# 예시
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1  # treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")


# break : 강제로 while문 빠져나가기
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


# continue : while 문의 맨 처음으로 다시 돌아가게 만들기
a = 0
while a < 0:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)


# 자판기
coffee = 10
while True:
    pocket_money = int(input("돈을 넣어 주세요: "))
    if pocket_money == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1
    elif pocket_money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (pocket_money - 300))
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
