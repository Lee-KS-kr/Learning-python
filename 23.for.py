# 반복문

# print("대기번호 : 1")

# for waiting in [0,1,2,3,4]]: #0,1,2,3,4
#     print("대기번호 : {0}".format(waiting))
# 리스트 내의 값들을 하나씩 돌아가면서 넣은 후에 for문이 끝남.

## randrange()
# for waiting in range(1,6): 
#     print("대기번호 : {0}".format(waiting))

starbucks = ["아이언맨", "토르", "스파이더맨"]
for customer in starbucks:
    print("{0} 고객님, 커피가 준비되었습니다.".format(customer))
