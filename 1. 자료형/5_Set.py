# set : 집합


s1 = set([1, 2, 3])
print(s1)

s2 = set("hello")
print(s2)

# 특징
# 중복을 허용하지 않는다. -> 데이터 중복 제거용 필터로 사용
# 순서가 없다. -> 인덱싱으로 요소에 접근할 수 없다.

# set 자료형에 저장된 값을 인덱싱으로 접근
# 리스트로 변환
l1 = list(s1)
print(l1[0])

# 튜플로 변환
t1 = tuple(s1)
print(t1[1])


########## 교집합, 합집합, 차집합 구하기 ##########
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])


# 교집합 구하기
# & , intersection()
print(s1 & s2)
print(s1.intersection(s2))


# 합집합 구하기
# | , union
print(s1 | s2)
print(s1.union(s2))


# 차집합 구하기
# - , difference
print(s1 - s2)
print(s2.difference(s1))


########## 집합 자료형 관련 함수 ##########

# add : 값 1개 추가하기
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# update : 값 여러개 추가하기
s1.update([4, 5, 6])
print(s1)

# remove : 특정 값 제거하기
s1.remove(2)
print(s1)
