# 가변인자를 이용한 함수 호출
# def profile(name, age, lan1, lan2, lan3, lan4, lan5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") 
# # 해당 문장이 끝나고 줄바꿈을 하지 않겠다는 뜻
#     print(lan1, lan2, lan3, lan4, lan5)
# profile("이경서", 29, "Python", "자바", "C", "C++", "C#")
# profile("이지연", 31, "Kotlin", "Swift","","","")
# 이렇게 되면 한명이 갯수가 늘었을 때 함수정의 자체를 바꾸고 모두 변경해야 하는 일이 생김.

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") 
    for lang in language :
        print(lang, end=" ")
    print()

profile("이경서", 29, "Python", "자바", "C", "C++", "C#", "JavaScript")
profile("이지연", 31, "Kotlin", "Swift")
# 가변인자를 *로 선언하는 것으로 인자 갯수가 다른 것들을 하나의 매개변수로 활용 가능
