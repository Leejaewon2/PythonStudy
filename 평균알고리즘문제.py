# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다.
# 당신은 그들에게 슬픈 진실을 알려줘야 한다.

#입력
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
# 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
#각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

# c = int(input("테스트 케이스의 개수 입력 : "))
#
# for e in range(c):
#     n = list(map(int, input("학생의 수와 점수를 입력하세요 : ").split()))
#     student_count = n[0]
#     student_score = n[1:]
#     average = sum(student_score) / student_count
#     above_average_count = sum(1 for e in student_score if e > average)
#     ratio = (above_average_count / student_count) * 100
#     print(f"비율 : {ratio:.3f}% 입니다.")

#강사님 버전

def over_rate(): # 각 케이스에서 평균이 넘는 비율 구하기
    ls = list(map(int, input().split())) # 공백 기준으로부터 입력값을 받아 정수형 리스트를 만듬
    average = sum(ls[1:]) / len(ls[1:]) # 리스트에서 맨앞의 요소는 인원수 이므로 제외, 총합 / 인원수
    cnt = 0 # 평균이 넘는 % 를 구하기 위해서는 인원에 대한 카운트가 필요
    for i in range(1, len(ls)): # 맨앞의 요소는 인원수 이므로 제외함
        if ls[i] > average : cnt += 1
    return cnt / (len(ls) - 1) * 100 # 백분율 표기로 변경

n = int(input()) # 총 테스트 횟수
rst = [] # 각 케이스에 대한 결과값을 받기 위한 리스트
for i in range(n): # 총 테스트 횟수 만큼 반복 수행
    rst.append(over_rate())

for e in rst:
    print(f"{e:.3f}%")









