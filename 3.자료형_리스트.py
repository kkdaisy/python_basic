# 리스트의 표현
# 리스트는 어떠한 자료형도 포함할 수 있다.

# 비어있는 리스트
# a = list()
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']

# 리스트 자체를 요솟값으로.
e = [1, 2, ['Life', 'is']]


########## 리스트의 인덱싱 ##########
odd = [1, 2, 3]

print(odd[0])
print(odd[0] + odd[2])

abc = [1, 2, 3, ['a', 'b', 'c']]
print(abc[0])
print(abc[-1])
print(abc[3])

# 리스트 abc에서 한개씩 꺼내는 방법
print(abc[-1][0])
print(abc[-1][1])
print(abc[3][2])


########## 리스트의 슬라이싱 ##########
xyz = [1, 2, 3, 4, 5]
print(xyz[0:2])

# 중첩 리스트 슬라이싱
abc = [1, 2, 3, ['a', 'b', 'c']]
print(abc[2:4])

# 중첩 리스트 안의 요소 슬라이싱
print(abc[3][:2])


########## 리스트 연산하기 ##########
# 리스트 더하기
print(abc+xyz)

# 리스트 반복하기
print(abc * 3)

# 리스트 길이 구하기
print(len(abc))


########## 리스트 수정하기 ##########

# 값 수정하기
s = [1, 2, 3, 4, 5, 6, 7, 8]
s[2] = 4
print(s)

# 값 삭제하기
del s[0]
print(s)

# 한꺼번에 삭제하기
del s[2:]
print(s)

# 연산을 위해 형 변환하기
# str() : 정수나 실수를 문자열로 바꾸어주는 함수
print(str(xyz[2]) + "hi")


######### 리스트 관련 함수 ##########
# append : 리스트 맨 마지막에 요소 추가
# 리스트 안에는 모든 자료형을 추가할 수 있따.
test = [1, 2, 3]
test.append(4)
test.append([5, 6])
test.append('a')

print(test)


# sort : 리스트의 요소를 순서대로 정렬
new = [1, 4, 6, 9, 8, 7]
new.sort()
print(new)

alp = ['s', 'g', 'c', 'a']
alp.sort()
print(alp)


# reverse : 리스트 뒤집기
# 현재의 리스트를 그대로 거꾸로 뒤집는다.
new.reverse()
print(new)


# index : 인덱스 반환
# 해당 값이 있는 인덱스 값을 리턴한다.
new = [1, 4, 6, 9, 8, 7]
print(new.index(8))


# insert(a, b) : 리스트의 a번째 위치에 b를 삽입
num = [1, 2, 3]
num.insert(0, 1)
print(num)


# remove(x) : 리스트에서 첫번째로 나오는 x를 삭제함
# 같은 값이 2개일 경우 처음에 나오는 값만 제거됨
num = [1, 2, 3, 1, 2, 3]
num.remove(1)
print(num)


# pop() : 리스트의 맨 마지막 요소를 리턴하고 삭제한다.
# pop(x) : 리스트의 x번째 요소를 리턴하고 삭제한다.
num = [1, 2, 3]
num.pop()
num.pop(0)
print(num)


# count(x) : 리스트에 포함된 x요소 갯수 새기
num = [1, 2, 3, 1, 2, 3]
print(num.count(1))


# extend(x) : x는 리스트. 기존 리스트에 x 리스트를 더한다.
num = [1, 2, 3]

# num += [4, 5]
num.extend([4, 5])
print(num)
