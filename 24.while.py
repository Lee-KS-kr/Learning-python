# 또 다른 반복문

# cust = "토르"
# index = 5
# while (조건):

# while index >= 1:
#     print("{0} 고객님, 커피가 준비 되었습니다. \n{1}번 남았어요.".format(cust, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기 처분 되었습니다.")

# cust = "아이언맨"
# index = 1
# while True:
#     print("{0} 고객님, 커피가 준비 되었습니다. 호출 {1}회 입니다.".format(cust, index))
#     index += 1
# 무한 루프

cust = "스파이더맨"
person = "Unknown"
while person != cust :
    print("{0} 고객님, 커피가 준비 되었습니다.".format(cust))
    person = input("닉네임이 어떻게 되세요?\n>")
# 내가 원하는 값이 입력될 때 까지 반복.
