#무작위 수를 공백으로 기준하여 입력 받아 홀수와 짝수로 리스트에 나누어 담아 출력 하는
#문제 입니다.

# 방법 1
# num = list(map(int, input("정수 입력 : ").split()))
# anum = [] # 홀수
# bnum = [] # 짝수
#
#
# for e in num:
#     if e % 2 == 0:
#         bnum.append(e)
#     else:
#         anum.append(e)
# print(f"홀수 : {anum} ")
# print(f"짝수 : {bnum}")

# map : 전달 받은 값을 함수내부에서 가공해서 반환 (입력 개수와 반환 개수가 동일)
# filter : 전달 받은 값을 함수내부에서 조건에 일치하는 것만 골라서 반환

# 방법 2 (lamda 사용)
num = list(map(int, input("입력 : ").split()))
odd = list(filter(lambda e: e % 2 == 1, num))
even = list(filter(lambda e: e % 2 == 0, num))
print(f"홀수 : {odd}")
print(f"짝수 : {even}")





