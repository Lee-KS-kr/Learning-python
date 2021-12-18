#문자열 처리함수
python = "Python is Amazing"
print(python.lower()) #문자열 내 모든 문자를 소문자로 출력
print(python.upper()) #모든 문자를 대문자로 출력
print(python[0].isupper()) #문장 내 [n]번째 글자가 대문자인지 확인
print(len(python)) #전체 문자열의 길이를 반환
print(python.replace("Python" , "Java")) #문장 내 특정 단어를 찾아서 바꾸기

index = python.index("n") #python이라는 변수에서 어떤 문자가 어디 있는지 찾을 수 있음
print(index)
index = python.index("n" , index + 1) #앞에서 찾은 것 다음위치부터 찾기
print(index)

print(python.find("n"))
print(python.find("Java")) #내가 원하는 값이 포함되어있지 않은 경우 -1을 반환
# print(python.index("Java")) #index를 통해서 할 경우 오류가 생김.
print("hi") 
#find의 경우 -1을 반환하기 때문에 이 hi가 출력되지만, index의 경우 에러가 발생하여
#프로그램을 종료하기 때문에, 뒤에 함수가 있을 경우 출력되지 않음.

print(python.count("n")) #문자열 내에 내가 찾고자 하는 글자가 몇 번 등장하였는지 세어줌.
