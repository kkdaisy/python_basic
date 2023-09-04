########## 사용자 입력 받기 ##########

# input() : 사용자가 키보드로 입력한 모든 것을 *문자열*로 저장한다.
a = input()
print(a)


# 안내 문구를 입력하여 입력 받기
num = input("안내_문구 : ")
print(num)


# 큰따옴표로 둘러싸인 문자열은 + 연산과 동일
print("life" "is" "too short")
print("life", "is", "too short")  # 띄어쓰기는 쉼표로 구분


# 한줄에 결괏값 출력하기
# end='' : 끝 문자를 지정해야 한다. 매개변수의 초깃 값은 줄바꿈(\n) 문자이다.
for i in range(10):
    print(i, end=' ')
