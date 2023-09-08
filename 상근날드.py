# 1번 : 상근날드
# 햄버거는 총 3종류 상덕버거, 중덕버거, 하덕버거가 있고, 음료는 콜라와 사이다 두종류
# menu_list = list(map(int, input("입력 : ").split()))
# min_berger = min(menu_list[:3])
# min_drink = min(menu_list[3:5])
# print(f"가장 싼 세트 메뉴 가격은 : {(min_berger + min_drink) - 50}입니다.")

# 2번 : 저항
# 입력 : 3개의 저항값 입력
# 저항에 대한 색상 : "black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"
# 첫번째 색상은 10의 자리수, 두번째 수는 1의자리수, 세번째 자리수는 곱해야 하는 수(1,10,100,...)
# color1, color2, color3 = map(input("색 입력 : ").split())
# color = "black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"
# f_name = color.index(input()) # input으로 입력 받은 문자열이 color 튜플내의 인덱스로 반환
# s_name = color.index(input())
# t_name = color.index(input())
# print(int((f_name)+str(s_name)) * (10** t_name))

# 3번 : PC방 알바
# 1 ~ 100번 까지의 컴퓨터가 있음
# 손님은 자신이 앉고 싶어하는 자리를 선택하고자 합니다. 이미 예약된 자리는 선택할 수 없으므로
# 거절해야 하며, 거절횟수를 구하시오.
# seat_num = list(map(int, input().split()))
# pc = [0] * 100 # 0으로 초기화된 100개의 리스트 생성, 파이썬에서는 배열이 없으므로 편법을 써서 100개의 리스트를 저렇게 만들어야 함.
# cnt = 0
# for e in seat_num: # 향상된 for문이므로 e값을 고객이 앉고 싶어하는 좌석 번호
#     if pc[e - 1] != 0: cnt += 1
#     else: pc[e - 1] = 1
# print(cnt)

# 4번 : Knuth-Morris-Pratt => KMP, Mirko-Slavko => MS
upper_str = ""
for e in input(): # 입력 받는 개수만큼 자동 순회
    if e.isupper() : upper_str += e
print(upper_str)












