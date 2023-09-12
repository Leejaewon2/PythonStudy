# 각 사이트 비밀번호 만들기
# 규칙1 : http://naver.com 앞의 http:// 잘라내기
# 규칙2 : 처음 만나는 점 이후 제거
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자에 포함된 'o'갯수 + 글자에 포함된 'k'의 갯수 + "!" + 자신의 이니셜
# file_name = "password.txt"
# fd = open(file_name, "wt")
#
#
# while True :
#     url = input("사이트 : ")
#     if url == 'exit' : break
#     my_str = url.replace("http://", "")
#     my_str = my_str[:my_str.index(".")]  # 슬라이싱 : 처음부터 "." 인덱스 미만
#     password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("k")) + "!" + "ljw"
#     print("비밀번호 : " + password)
#     fd.write(password + "\n")
# fd.close()

import pickle

# 객체를 직렬화하여 파일에 저장하기
# data = {"name" : "곰돌이사육사", "age": 22, "addr" : "서울시 강남구 역삼동"}
# with open("data.pickle", "wb")as file:
#     pickle.dump(data, file)

# 파일에서 객체를 역직렬화하여 복원하기
# with open("data.pickle", "rb")as file:
#     restored_data = pickle.load(file)
#
# print(restored_data)
