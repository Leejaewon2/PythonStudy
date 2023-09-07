# 회원정보를 입력 받아서 출력 하는 예제 진행
#
# - 이름 입력
# - 나이 입력 : 1 ~ 199까지 입력 받고 잘못된 값이 오면 재 입력 요청을 한다.
# - 성별 입력 : 영문자 (memp 남성) (F와 f는 여성)으로 입력 받고 나머지는 재 입력
# 요청을 한다.
# - 직업 입력 : 1(학생), 2(회사원), 3(주부), 4(무직)으로 입력 받고 나머지는 재 입력
# 요청 한다.
# - 결과는 마지막에 한번에 출력 한다.



name = input("이름을 입력하세요 : ")


# 나이 조건식
while True:
    age = int(input("나이를 입력하세요 : "))
    if 0 < age < 200:
        break
    else: print("나이를 잘못 입력하셨습니다.")


# 성별 조건식
while True:
    gender = input("성별을 입력하세요 : ")
    if gender == "m" or gender == "M":
        break
    elif gender == "f" or gender == "F":
        break
    else:
        print("다시 입력하세요.")


# 직업 조건식
while True:
    jobs = int(input("직업 입력 : [1] 학생, [2] 회사원, [3] 주부, [4] 무직 : "))
    if jobs == 1:
        jobs = "학생"
        print("학생 입니다.")
        break
    elif jobs == 2:
        jobs = "회사원"
        print("회사원 입니다.")
        break
    elif jobs == 3:
        jobs = "주부"
        print("주부 입니다.")
        break
    elif jobs == 4:
        jobs = "무직"
        print("무직 입니다.")
        break
    else:
        print("다시 입력하세요.")

print(f"제 이름은 : {name} 입니다.")
print(f"제 나이는 : {age} 입니다.")
print(f"제 성별은 : {gender} 입니다.")
print(f"제 직업은 : {jobs} 입니다.")




