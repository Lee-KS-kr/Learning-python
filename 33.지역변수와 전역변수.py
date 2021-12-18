# 지역 변수는 함수 내에서만 사용할 수 있는 것. 함수가 호출 될 때 만들어졌다가 함수 호출이 끝나면 사라지는 것.
# 전역 변수는 모든 공간 내 프로그램 내에서 사용할 수 있는 것.

gun = 10

# def checkpoint(soldiers): # 경계 근무
#     gun = 20 # 지역변수 지정 (함수 내에 gun이 없어서 에러가 생겨남)
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint(soldiers): # 경계 근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계근무
# print("남은 총 : {0}".format(gun))

# 전역변수를 많이 쓰게 되면 코드 관리가 어려워지기 때문에 권장사항은 아님.
# 가급적 함수의 전달값(파라미터)로 계산을 하고 반환값으로 사용하는 방법
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun)) 
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))