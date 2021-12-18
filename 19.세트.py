# 집합 (set)
# 중복 안됨, 순서 없음
my_set= {1,2,3,3,3}
print(my_set) #중복이 허용되지 않기 때문에 중복되는 뒤의 값들은 무시됨

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 출력하기
print(java & python)
print(java.intersection(python))

#합집합 출력하기
print(java | python)
print(java.union(python))

#차집합 출력하기
print(java - python)
print(java.difference(python))

#추가하기
python.add("김태호")
print(python)

#빼기
java.remove("김태호")
print(java)