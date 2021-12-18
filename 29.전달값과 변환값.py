def open_account():
    print("새로운 계좌가 개설되었습니다.") #함수에서 실행 할 내용


def deposit(balance, money): # 입금
    print("입금이 완료되었습니다.\n잔액은 {}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다.\n잔액은 {}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("잔액이 부족합니다.\n잔액은 {}원 입니다.".format(balance))
        return balance

def with_night(balance, money):
    com = 100 #수수료
    return com, balance - money - com

balance = 0 
balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
com, balance = with_night(balance, 500)
print("수수료는 {0} 원이며, 잔액은 {1} 원 입니다.".format(com, balance))