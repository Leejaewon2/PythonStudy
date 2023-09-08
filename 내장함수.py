# 내장함수 : 파이썬이 기본적으로 제공, import가 필요 없음


# 큰값 작은값 찾기
# print(max(1,2,3,4,5,6,7,50,8,90,100,777,534,517,83))
# print(min(1,2,3,4,5,6,7,50,8,90,100,777,534,517,83))

# 총 합 구하기
# print(sum([1,2,3,4,5,6,7,50,8,90,100,777,534,517,83])) # 리스트의 총 합
# print(sum((1,2,3,4,5,6,7,50,8,90,100,777,534,517,83))) # 튜플에 대한 총 합
# num = list(map(int, input("정수값 입력 : ").split()))
# print(f"입력 받은 수의 총 합 : {sum(num)}")
# print(f"입력 받은 수의 평균 : {sum(num)/len(num)}")

# 몫과 나머지 구하기
# print(f"몫과 나머지 {divmod(10, 4)}") # 튜플의 동작 원리, 두개의 반환값으로 받음



# 여러개의 값을 한번에 입력 받아 리스트로 만들기
# 최대값, 최대값, 합계, 평균, 합계에 대한 몫과 나머지
# num = list(map(int, input("정수 입력 : ").split()))
# print(f"최대값 : {max(num)}")
# print(f"최소값 : {min(num)}")
# print(f"합계 : {sum(num)}")
# print(f"평균 : {sum(num)/len(num)}")
# print(f"합계에 대한 몫과 나머지 : {divmod(sum(num),5)}")



# 정렬 조건
my_list = [1,2,3,4,45,56,7,777,88,99,100]
# 오름 차순 정렬
print(sorted(my_list))
# 내림 차순 정렬
print(sorted(my_list, reverse=True))



