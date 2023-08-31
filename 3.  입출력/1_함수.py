# 함수 구조
# 들어온 입력값을 받은 후 어떤 처리를 하여 적절한 값을 리턴해준다.

# def 함수_이름(매개변수):
#    수행할_문장1
#    수행할_문장2

a = 3
b = 4


# 매개변수(parameter) : 함수에 입력으로 전달된 값을 받는 변수
# 인수(arguments) : 함수를 호출할 때 전달하는 입력 값

def add(a, b):  # a, b는 매개변수
    return a+b


print(add(3, 4))  # 3, 4는 인수


######### 입력 값이 있고, 리턴 값이 있는 함수 #########
def add(a, b):
    result = a + b
    return result


######### 입력값이 없는 함수 #########
def say():
    return "Hi"


a = say()  # a라는 문자열에 "Hi"를 대입함
print(a)


######### 리턴값이 없는 함수 #########
def sum(c, e):
    print("%d, %d의 합은 %d 입니다." % (c, e, c+e))


f = sum(3, 4)
print(f)  # 리턴값이 없기 때문에 None이 출력됨


######### 입력값과 리턴값이 없는 함수 #########
def say():
    print('Hi')


say()


######### 매개변수를 지정하여 호출하기 #########
def sub(a, b):
    return a - b


result = sub(a=7, b=3)
print(result)


######### 입력값이 몇 개가 될 지 모를때 #########

# def 함수_이름(*매개변수):
#    수행할_문장


def add_many(*args):
    result = 0
    for i in args:
        result = result + i    # *args에 입력받은 모든 값을 더한다.
    return result


result = add_many(1, 2, 3)
print(result)


# 여러개 매개변수 사용하기
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result


result = add_mul('add', 1, 2, 3, 4, 5)
print(result)

result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)


# kwargs : 키워드 매개변수
# 딕셔너리가 되고, 입력값이 딕셔너리에 저장된다.
def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(a=1)
print_kwargs(name='foo', age=3)


########## 함수의 리턴 값은 언제나 1개! ##########
# 단 함수는 return 문을 만나는 순간 리턴 문을 돌려 준 다음 함수를 빠져나가게 된다.
def add_and_mul(a, b):
    return a+b, a*b


result = add_and_mul(3, 4)
print(result)
# result = (7, 12)

# 값을 분리해서 받고 싶을 때
result1, result2 = add_and_mul(3, 4)
print(result1)
print(result2)


# return으로 함수 빠져나가기

# 바보라는 값이 들어오면 문자열을 출력하지 않고 바로 함수를 빠져나간다.
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다. " % nick)


say_nick('야호')
say_nick('바보')


# 매개변수에 초깃값 미리 설정하기
# 이때 꼭 !! 초기화 하고 싶은 매개 변수는 항상 뒤쪽에 놓아야 한다.

def say_myself(name, age, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d 살입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("박응용", 27, True)
say_myself("박응용", 27)  # 변수 입력값을 주지 않아도 man은 초기값 True를 갖게 된다.


say_myself("박응선", 27, False)


# lambda : 함수를 한 줄로 간결하게 만들 때. def를 사용할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳
# return이 없어도 표현식의 결괏값을 리턴한다.
def add_lam(a, b): return a+b


result = add_lam(3, 4)
print(result)
