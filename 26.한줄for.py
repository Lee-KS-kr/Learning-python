# 한 줄로 끝내는 for문 활용하기
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함. -> 101 102 103 104

st = [1,2,3,4,5]
print(st)
st = [i+100 for i in st]
print(st)

# 학생 이름을 길이로 변환
sts = ["Ironman", "Groot", "Thor", "Spiderman"]
sts = [len(i) for i in sts]
print(sts)

# 학생 이름을 대문자로 변환
sts = ["Ironman", "Groot", "Thor", "Spiderman"]
sts = [i.upper() for i in sts]
print(sts)

