# 1. 배수찾기 (초급에 있음)
# 첫째줄에 n이 주어짐, 다음줄 부터 값이 주어 짐
# 목록에 있는 수가 n의 배수인지 아닌지 판별
# 0을 입력하면 목록이 끝남

# 내가 푼거
# main_n = int(input("기준 정수 입력 : "))
# while True:
#     sub_n = list(map(int, input("판별할 정수 입력 : ")))
#
#     if main_n % sub_n == 0:
#         print(f"{sub_n} is a multiple of {main_n}")
#     elif main_n % sub_n != 0:
#         print(f"{sub_n} is NOT a multiple of {main_n}")
#     else:
#         sub_n == 0
#     break

# 강사님이 푼거
n = int(input()) # 문자열로 반환되기 때문에 정수타입으로 변환
ls = [] # 값을 저장 받기 위해서 비어있는 리스트 생성
while True : # 0 입력 되기 전 까지는 반복 수행
    x = (int(input())) # 목록의 수를 입력 받는다.
    if x == 0 : break  # 0이 입력되면 탈출
    ls.append(x)

for i in ls:
    if i % n == 0 : print(f"{i} is a multiple of {n}.")
    else : print(f"{i} is NOT a multiple of {n}.")









