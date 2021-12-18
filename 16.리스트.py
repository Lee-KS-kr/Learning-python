# #리스트 [] : 순서를 가지는 객체의 집함
# #지하철 칸별로 10명, 20명, 30명
# # subway1 = 10
# # subway2 = 20
# # subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway= ["유재석", "조세호", "박명수"]
# print(subway)

# #조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# #하하씨가 다음 정류장에서 탑승
# subway.append("하하") #append : 더하다, 맨 뒤에 붙음
# print(subway)

# #정형돈씨가 유재석 / 조세호 사이에 탑승
# subway.insert(1, "정형돈")
# print(subway)

# #지하철에 있는 사람을 한 명씩 내리게 함
# print(subway.pop()) #맨 뒤의 한명이 내림
# print(subway)

# #같은 이름의 사람이 몇 명 있는지 확인하기
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# #정렬도 가능
# num_list = [5,2,4,1,3]
# print(num_list)
# num_list.sort()
# print(num_list)

# #뒤집기도 가능
# num_list.reverse()
# print(num_list)

# #모두 지우기
# num_list.clear()
# print(num_list)

#다양한 자료형을 함께 사용 가능
mix_list = ["조세호", 20, True]
num_list = [5,2,4,1,3]
# print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)
