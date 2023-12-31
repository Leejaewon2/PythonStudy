# 2. 피타고라스 정리 (중급에 있음)
# 피타고라스의 정리 : 직각삼각형에서 빗변을 제외한 나머지 두 변의 길이를
# 각각 제곱해 더하면 빗변의 길이의 제곱과 같다.
# 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다.
# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

# 입력
# 6 8 10
# 10 8 6
# 25 52 60
# 5 12 13
# 0 0 0

# 출력
#right
#right
#wrong
#right


rst = [] # 결과를 출력하기 위한 빈 리스트
while True:
    li = list(map(int, input().split()))
    li.sort()
    if li[0] == 0 and li[1] == 0 and li[2] == 0: break
    elif li[2] ** 2 == li[1] ** 2 + li[0] ** 2:
        rst.append("right")
    else:
        rst.append("wrong")
for e in rst: print(e)