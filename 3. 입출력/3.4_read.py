# read() : 파일 내용 전체를 문자열로 리턴한다.

f = open("/Users/kkyo/2023/study/python/python_basic/3. 입출력/새파일.txt", 'r')
data = f.read()
print(data)

f.close()


