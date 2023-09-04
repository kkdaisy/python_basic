########## 파일에 새로운 내용 추가하기 ##########
# 'w' : 이미 존재하는 파일을 열면, 그 파일의 내용이 모두 사라짐
# 'a' : 원래 있던 값을 유지하면서 새로운 값을 추가
c = open("/Users/kkyo/2023/study/python/python_basic/3. 입출력/새파일.txt", 'a')
for i in range(11,20):
    data = "%d 번째 줄 입니다. \n" %i
    c.write(data)

c.close()