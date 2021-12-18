# #문자열 포맷

# print("a" + "b")
# print("a", "b")
# #지금까지는 이렇게 해 왔음.

# #방법1
# print("나는 %d살입니다." % 29) 
# # %의 뒤에 있는 값을 d의 위치에 넣겠다는 의미. 정수여야만 함.
# print("나는 %s을 좋아해요." % "파이썬") 
# # % 뒤에 있는 문자열(스트링) 값을 s의 위치에 넣겠다는 의미.
# print("Apple은 %c로 시작해요" % "A")
# # %c 캐릭터. 한 글자만 받겠다는 의미
# # %s 는 정수, 문자열, 하나의 글자 모두 받을 수 있음
# print("나는 %s살입니다." % 29) 
# print("나는 %s색과 %s색을 좋아해요" % ("검정", "파랑"))

#방법2
# print("나는 {}살입니다.".format(29)) 
# #format뒤 괄호 속 값을 중괄호에 집어넣게 됨
# print("나는 {}색과 {}색을 좋아해요".format("검정", "파랑"))
# print("나는 {1}색과 {0}색을 좋아해요".format("검정", "파랑"))
# #숫자의 배치를 변환하거나, format 속 인수의 갯수를 늘리는 것으로 바리에이션이 가능!

#방법3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 29, color = "보라"))
# #마치 변수 선언하듯이
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "보라",age = 29))

#방법4 (python 버전 3.6이상부터 가능)
#변수를 선언하고, f로 print를 시작하는 것으로 변수를 넣을 수 있음.
age = 29
color = "보라"
print(f"나는 {age}살이며, {color}색을 좋아해요.")