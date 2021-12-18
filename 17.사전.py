#사전 {key:value}

# cabinet = {3:"유재석", 100:"김태호"}
# # print(cabinet[3])
# # print(cabinet[100])
# # print(cabinet.get(3))
# # # print(cabinet[5]) #사전에 없는 키를 입력시 오류가 발생하며 프로그램 종료
# # print(cabinet.get(5)) #get을 이용시는 none이 반환됨
# # print(cabinet.get(5, "사용 가능")) #default는 none, 그 뒤 문자 지정시 지정문자 반환

# #사전 자료형 안에 특정 값이 있는지 확인하기
# print(3 in cabinet) #True
# print(5 in cabinet) #False

cabinet = {"A-3":"Cat", "B-100":"Dog"}
print(cabinet["A-3"])

#새 손님
print(cabinet)
cabinet["A-3"] = "Lion"
cabinet["C-20"] = "Tiger"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key들과 value들을 함께 출력
print(cabinet.items())

#영업 종료
cabinet.clear()
print(cabinet)
