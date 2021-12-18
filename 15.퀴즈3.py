# Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                         (nav)       (5)             (1)         (!)

# 예) 생성된 비밀번호 : nav51!

#내가 풀어 본 방식
# url = "http://mabinogi.com"
# rul = url[7:]
# # print(url)
# url = url[:8]
# # print(url)
# # print(url[:3])
# # print(len(url))
# # print(url.count("e"))
# url3 = url[:3]
# nu = len(url)
# e = url.count("e")
# print(f"생성된 비밀번호 : {url3}{nu}{e}!")

#선생님 해답풀이
url = "http://mabinogi.com"
my_url = url.replace("http://", "") #규칙1
# print(my_url)
my_url = my_url[:my_url.index(".")] #규칙2
# print(my_url)
password = my_url[:3] + str(len(my_url)) + str(my_url.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다".format(url, password))

url = "http://google.com"
my_url = url.replace("http://", "") #규칙1
# print(my_url)
my_url = my_url[:my_url.index(".")] #규칙2
# print(my_url)
password = my_url[:3] + str(len(my_url)) + str(my_url.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다".format(url, password))

url = "http://youtube.com"
my_url = url.replace("http://", "") #규칙1
# print(my_url)
my_url = my_url[:my_url.index(".")] #규칙2
# print(my_url)
password = my_url[:3] + str(len(my_url)) + str(my_url.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다".format(url, password))