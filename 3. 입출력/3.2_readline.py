########## 파일을 읽는 여러가지 방법 ##########
# readline() : 파일을 한줄씩 읽는다.

# 파일의 첫번째 줄을 읽어 출력한다.
f = open("/Users/kkyo/2023/study/python/python_basic/3. 입출력/새파일.txt", 'r')
line  = f.readline()
print(line)

f.close()


# 전체 파일을 읽는다.
d = open("/Users/kkyo/2023/study/python/python_basic/3. 입출력/새파일.txt", 'r')
while True:
    line = d.readline()
    if not line: break
    print(line)

d.close()