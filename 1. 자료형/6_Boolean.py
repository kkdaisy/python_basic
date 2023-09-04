# Bool 자료형
# 참(true)와 거짓 (false) 를 나타냄

a = True
b = False

print(type(a))

# 참거짓 판별
print(1 == 1)

# 문자열, 리스트, 튜플, 딕셔너리 등 값이 비어있으면 거짓, 값이 있으면 참이 된다.
# 단 숫자 0 은 거짓

if []:
    print("참")
else:
    print("거짓")


########## bool연산 ##########
print(bool('python'))
