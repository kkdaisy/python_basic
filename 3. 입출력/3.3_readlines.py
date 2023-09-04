# readlines(): 파일의 모든 줄을 읽어서 각각의 줄을 요소로 가지는 리스트를 리턴한다.

f = open("/Users/kkyo/2023/study/python/python_basic/3. 입출력/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()  # 줄 끝의 줄 바꿈 문자(\n)를 제거 한다.
    print(line)

f.close()

