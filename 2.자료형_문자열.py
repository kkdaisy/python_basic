########## 문자열 ##########

# 문자열에 작은 따옴표 포함하기 - 서로 다른 따옴표 사용
# 큰(작은) 따옴표 안에 작은(큰) 따옴표는 문자열 기호로 인식하지 않음

food = "Python's favorite food is perl"
print(food)

say = '"Python is very easy." he says'
print(say)


# 역슬래시 뒤에 따옴표
food1 = 'Python\'s favorite food is perl'
say1 = "\"Python is very easy.\" he says"
print(food1)
print(say1)


# 여러줄 입력하기
# 이스케이프코드 \n
multiline = "Life is too short\n You need Python"
print(multiline)

# 따옴표 3개 (큰, 작은 따옴표 상관 없음)
multiline1 = """
Life is too short 
You need Python
"""
print(multiline1)


# 문자열 연산
# 문자열 더하기
head = "Python"
tail = "is fun!"
print(head + tail)


# 문자열 곱하기 => 반복
a = "Python"
print(a * 2)

# 응용
print("=" * 50)
print("My program")
print("=" * 50)


########## 문자열 응용 ##########
# 문자열 길이 구하기
# 문자열 길이에는 공백 문자도 포함된다.
a = "Life is too short"
print(len(a))

# 인덱싱
b = "Life is too short, You need Python"  # 공백 포함해서 숫자 셈
print(b[3])

# 슬라이싱
print(b[0:4])  # 끝번호에 해당하는 문자를 포함하지 않기 때문에 실제로 출력되는 문자는 0 ~ 3


# 슬라이싱으로 문자열 나누기
c = "20230331Rainy"
date = c[:8]
day = c[4:8]
weather = c[8:]
print(date)
print(day)
print(weather)


########## 문자열 포매팅 ##########
# 문자열 안의 특정한 값을 바꿔야 할 경우, 문자열 안에 어떤 값을 삽입하는 방법

# 숫자 대입
print("I eat %d apples." % 3)  # 숫자 대입할 때 %d

# 문자열 바로 대입
print("I eat %s apples." % "five")  # %s는 어떤 형태의 값이든 변환해서 넣을 수 있음

# 숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." % number)

# 2개 이상의 값 넣기
newday = "three"
print("I ate %d apples. so I was sick for %s days." % (number, newday))


# 포매팅 연산자와 %를 같이 쓸때 %%로 표기
print("Error is %d%%" % 98)

# 정렬과 공백
# %10s : 전체 길이가 10인 문자열공간에 값을 오른쪽으로 정렬하고, 그 앞의 나머지는 공백으로 남겨둠
print("%10s" % "hi")

# hi는 왼쪽으로 정렬하고 나머지는 공백으로 정렬. 10인 문자열 공간 뒤에 jane
print("%-10sjane" % "hi")


########## 소수점 표현하기 ##########
# 소수점 4번째 자리까지만 출력하기
print("%0.4f" % 3.4256473466)
print("%.4f" % 3.4256473466)

# 문자열 전체길이 지정 및 소수점 자리 표시
print("%10.4f" % 3.4256473466)


########## format 함수를 사용한 포매팅 ##########

print("I eat {0} apples.".format(3))
print("I eat {0} apples.".format("five"))
print("I eat {0} apples.".format(number))


# 2개 이상의 값 넣기
print("I ate {0} apples. so I was sick for {1} days.".format(number, newday))


# 인덱스와 name=value 혼용
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))


# 왼쪽 정렬
# 문자열의 총 자릿수는 10, 문자열 왼쪽으로 정렬
print("{0:<10}".format("hi"))


# 오른쪽 정렬
# 문자열의 총 자릿수는 10, 문자열 오른쪽으로 정렬
print("{0:>10}".format("hi"))


# 공백 문자값으로 채우기
print("{0:!<10}".format("hi"))
# 가운데 정렬
print("{0:=^10}".format("hi"))


# 소수점 표현하기
y = 3.42134234

# 소수점 4자리까지만 표시
print("{0:0.04f}".format(y))

# {} 표시
print("{{ and }}".format())


########## f문자열 포매팅 ##########
# python 3.6 이상

name = "홍길동"
age = 30
print(f"나의 이름은 {name}입니다. 나이는 {age} 입니다.")

# 표현식 사용
print(f"내년이면 {age + 1} 살이 됩니다.")

# 딕셔너리의 f문자열 포매팅 사용
d = {'name': '홍길동', 'age': 30}
print(f"나의 이름은 {d['name']} 입니다. 나이는 {d['age']} 입니다.")

# 공백 채우기
print(f'{"hi":=^10}')
print(f'{"hi":!<10}')

# 소수점
print(f'{y:0.4f}')
print(f'{y:10.4f}')


# {} 문자 표시
print(f'{{ and }}')


# 문자열 관련함수
# 문자 개수 세기 : count
z = "hobby"
print(z.count('b'))  # 문자열 에서 b의 갯수를 리턴

# 위치 알려주기
# find
c = "Python is the best choice"
print(c.find('b'))  # b의 위치 출력
print(c.find('k'))  # 찾는 문자열 없을 경우 -1 반환


# index
print(c.index('t'))
# print(c.idex('k'))  # 찾는 문자열 없을 경우 오류 반환


# 문자열 삽입 : join
print(",".join('abcd'))  # 문자열 각각의 문자 사이에 ',' 삽입


# 소문자를 대문자로 : upper
g = "hi"
print(g.upper())


# 대문자를 소문자로 : lower
h = 'HI'
print(h.lower())


# 공백 지우기
# 왼쪽 공백 지우기 : lstrip
i = " hi "
print(i.lstrip())

# 오른쪽 공백 지우기 : rstrip
print(i.rstrip())

# 양쪽공백 지우기 : strip
print(i.strip())


# 문자열 바꾸기 : replace
# 바뀔문자열, 바꿀 문자열
print(a.replace("Life", "Your leg"))
