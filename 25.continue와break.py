# 반복문 내에서 사용 가능

ab = [2, 5] #결석
for st in range(1, 11):
    if st in ab:
        continue #해당 문장은 스킵하고 다음 반복으로 문장 실행
    print("{0}번, 책 읽어 봐.".format(st))
# 해당 반복을 진행.

ab = [2, 5]
nobook = [7]
for st in range(1, 11):
    if st in ab:
        continue
    elif st in nobook:
        print("오늘 수업 여기까지. {0}번 교무실 따라 와.".format(st))
        break
    print("{0}번, 책 읽어 봐.".format(st))
# break가 있으면 다음 순서가 있든없든 반복을 종료
