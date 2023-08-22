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
