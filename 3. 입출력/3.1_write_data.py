f = open("/Users/kkyo/2023/study/python/python_basic/3. 입출력/새파일.txt", 'w')
for i in range (1, 11):
    data = "%d번째 줄입니다. \n" %i
    f.write(data)

f.close()