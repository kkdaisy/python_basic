# 조건을 판단하여 해당 조건에 맞는 상황을 수행하는데 쓰는 것


'''
if 조건문:
    수행할_문장1
    수행할_문장2
else:
    수행할_문장A
    수행할_문장B
'''

# 예제
money = 2000

if money >= 3000:
    print("택시를 탄다")
else:
    print("걸어가라")


# not x : x가 거짓이면 참이다.
# x in () : 리스트, 튜플, 문자열 안에 x가 있으면 참
# x not in () : 리스트, 튜플, 문자열 안에 x가 없으면 참


# 조건문에서 아무 일도 하지 않게 설정
pocket = ['paper', 'money', 'cellphone']

if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")


# 한줄로 작성하기
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")


# elif : 다중조건 판단
# 이전 조건문이 거짓일 때 수행된다.
# 개수 제한 없이 사용할 수 있다.

pocket = ['paper', 'cellphone']
card = True

if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")


# 조건부 표현식
score = 50

# 원래 조건문
if score >= 60:
    message = "success"
else:
    message = "failure"


# 조건부 표현식
message = "success" if score >= 60 else "failure"
