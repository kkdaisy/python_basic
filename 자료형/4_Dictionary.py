# 딕셔너리
# 키:값 형태의 자료형

dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

# value에 리스트를 넣을 수도 있음
a = {'a': [1, 2, 3]}


########## 추가, 삭제하기 ##########

# 쌍 추가하기
# dictionary[key] = value
a = {1: 'a'}
a[2] = 'b'
print(a)

# 삭제하기
# del a[key] => key : value 값이 삭제된다.
del a[1]
print(a)


# key로 value 얻기
# 존재하지 않는 key를 요청할 경우 오류 발생
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])


# key
# 중복된 key는 존재할 수 없음
# 리스트는 key로 사용할 수 없음


########## 딕셔너리 관련 함수 ##########

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

# a.keys() : key만을 모아 dict_keys 객체를 리턴한다.
print(a.keys())


# a.values() : value만 얻는다.
print(a.values())


# 반복문으로 dict_keys에 있는 객체를 하나씩 반환한다.
for k in a.keys():
    print(k)


# 리스트로 dict_keys를 반환한다.
print(list(a.keys()))


# items : key, value 쌍을 튜플로 묶은 값을 dict_items 객체로 리턴한다.
print(a.items())


# clear : key:value 쌍을 모두 지우기
print(a.clear())


# get : key로 value 얻기
# 존재하는 키 값으로 가져오려고 하는 경우 None을 리턴
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

print(a.get('name'))
print(a.get('nokey'))


# get(key, '디폴트값') :찾으려는 key가 없을 경우 미리 정해둔 디폴트 값을 대신 가져오게 하고싶을 때
print(a.get('nokey', 'foo'))


# 해당 key가 딕셔너리 안에 있는지 조사하기 - in
b = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

print('name2' in b)
print('phone' in b)
