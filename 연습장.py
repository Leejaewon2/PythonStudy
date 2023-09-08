# 1. 정해진 형식으로 시간을 입력 받아서 출력하기
# 입력 형식 : 22:5:5 => 오후 10시 05분
# hour, min, sec = map(int, input("시간 입력 : ").split(":"))
# if hour > 12 :
#     hour -= 12
#     print(f"오후{hour:02}시 {min:02}분 {sec:02}초 입니다.")
# else:
#     print(f"오전{hour:02}시 {min:02}분 {sec:02}초 입니다.")


# 2번 3개의 정수를 입력 받아 최대값과 최소값 구하기
# a, b, c = map(int, input("정수 입력 : ").split(" "))
#
# max_num = max(a, b, c)
# min_num = min(a, b, c)
#
# print(f"최대값 : {max_num}")
# print(f"최소값 : {min_num}")

# 3번 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기
# from datetime import datetime
# curr_year = datetime.today().year

#주민번호 입력
# jumin = input("주민번호를 입력하세요 : ") #961203-1013329
# year = jumin[:2]
# month = jumin[2:4]
# day = jumin[4:6]
# gender = jumin[7]

# 주민등록번호로 성별 조건식
# if gender == "1" or gender == "3":
#     gender_str = "남성"
# else:
#     gender_str = "여성"
# 주민등록번호로 나이 조건식
# if gender == "1" or gender == "2":
#     age = curr_year - 1900 - int(year)
# else:
#     age = curr_year - 2000 - int(year)

#주민등록번호로 생년월일 출력
# print(f"""
# 저의 생년월일은 {year:02}년{month}월{day}일 입니다.
# 제 성별은 : {gender_str}입니다.
# 제 나이는 : {age}입니다.
# """)

# 4번 갯수가 정해지지 않은 여러개의 정수를 입력 받아 합계와 평균 구하기
#리스트 사용

# 구구단 만들기

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{i}x{j} : {i * j}")
#     print()

# A+B-3






# n개의 합 구하기
n = int(input("정수 : "))
sum = 0
for i in range(1, n + 1):
    sum += i
    print(sum)




