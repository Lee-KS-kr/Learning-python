# def profile(name, age, mainlan):
#     print("이름 : {0}\n나이 : {1}\n주 사용 언어 : {2}"\
#         .format(name, age, mainlan)) # 역슬러시로 줄바꿈 가능

# profile("이지연", 30, "파이썬")
# profile("이수연", 28, "자바")

# 같은 학교 같은 학년 같은 수업
def profile(name, age=17, mainlan="파이썬"):
     print("이름 : {0}\n나이 : {1}\n주 사용 언어 : {2}"\
         .format(name, age, mainlan)) # 역슬러시로 줄바꿈 가능

profile("이경서")
profile("조은강")