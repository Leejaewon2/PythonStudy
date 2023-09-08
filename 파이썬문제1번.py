# 1. 정해진 형식으로 시간을 입력 받아서 출력하기
# 입력 형식 : 22:5:5 => 오후 10시 05분
import datetime

# hour, min, sec = map(int, input("시간 입력 : ").split(":"))
# if hour > 12:
#     hour -= 12
#     print(f"오후{hour:02}시{min:02}분{sec:02}초")
# else:
#     print(f"오전{hour:02}시{min:02}분{sec:02}초")

# 2번 3개의 정수를 입력 받아 최대값과 최소값 구하기

# num1, num2, num3 = map(int, input("정수를 입력하세요 : ").split(" "))
# max_num = max(num1, num2, num3)
# min_num = min(num1, num2, num3)
#
# print(f"최대값 : {max_num}")
# print(f"최소값 : {min_num}")
#
# if num2 > max_num:
#     max_num = num2
# elif num2 < min_num:
#     min_num = num2
#
# # num3와 비교
# if num3 > max_num:
#     max_num = num3
# elif num3 < min_num:
#     min_num = num3

# 3번 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기

from datetime import datetime
curr_year = datetime.today().year
jumin = input("주민등록번호 : ")
year = jumin[:2]
month = jumin[2:4]
day = jumin[4:6]
gender = jumin[7]

# 주민등록번호로 성별,나이 조건식
if gender == "1" or gender == "2":
    age = curr_year - 1900 - year
else:
    age = curr_year - 2000 - year
if gender == "1" or gender == "3":
    gender_str = "남성"
else:
    gender_str = "여성"


#주민등록번호로 생년월일 출력
print(f"생년월일 : {year:02}년{month:02}월 {day:02}일")
print(f"성별 : {gender_str}")
print(f"나이 : {age}")

# 4번 갯수가 정해지지 않은 여러개의 정수를 입력 받아 합계와 평균 구하기
#리스트 사용
score = list(map(int,input("정수 : ").split()))
print(f"총점 : {sum(score)}")
print(f"평균 : {sum(score)/len(score)}")













































