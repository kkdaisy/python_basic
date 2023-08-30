# 반복문

# 기본 구조
# for 변수 in 리스트(튜플, 문자열):
#     수행할_문장1
#     수행할_문장2

# 예시
test_list = ['one', "two", "three"]
for i in test_list:
    print(i)

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first+last)


# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다. 합격인지, 불합격인지 결과를 보여 주시오.
marks = [90, 25, 67, 45, 80]

number = 0
for i in marks:
    number = number + 1
    if i >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)


# for문과 continue 문
# 60점 이상인 사람에게는 축하 메시지를 보내고 나머지 사람에게는 아무런 메시지도 전하지 않는 프로그램
mark2 = [90, 25, 67, 45, 80]

# 내가 쓴거
num = 0
for j in mark2:
    num += 1
    if j >= 60:
        print("%d번 학생 축하합니다" % num)
    else:
        continue

# 다른 작성법
mark2 = [90, 25, 67, 45, 80]

num = 0
for j in mark2:
    num += 1
    if j < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % num)


marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))


########## range ##########
a = range(1, 11)  # 1부터 11 미만의 숫자를 포함

add = 0
for i in range(1, 11):
    add = add + i

print(add)

# for & range를 사용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')


########## 리스트 컴프리헨션 : 리스트 안에 for 문을 포함 ##########
# [표현식 for 항목 in 반복_가능_객체 if 조건문]


# 원래
b = [1, 2, 3, 4]
result = []
for num in b:
    result.append(num*3)
print(result)

# 리스트 컴프리헨션 사용
c = [1, 2, 3, 4]
result = [num * 3 for num in c]
print(result)

# 리스트 컴프리헨션으로 짝수에만 3을 곱해서 담기
d = [1, 2, 3, 4]
result = [num * 3 for num in d if num % 2 == 0]
print(result)
