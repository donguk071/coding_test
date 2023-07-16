import sys

a , b = map(int,input().split())

test = []
real = []


test = [list(map(int, sys.stdin.readline().split())) for _ in range(a)]
real = [list(map(int, sys.stdin.readline().split())) for _ in range(b)]


max_diff = []

while True:
    if test == [] or real == []:
        break
    
    diff = real[0][0] - test[0][0] #길이차이 계산   

    if diff > 0 :  #실제 측정거리가 더욱 긴 경우
        max_diff.append(real[0][1] - test[0][1]) #계속 pop 해주기 떄문에 그냥 이렇게 비교해도 문제없음
        test.pop(0) #test는 다 소모했으므로 버리기
        real[0][0] = diff #남는 차이로 업데이트
    
    elif diff < 0 :  #실제 측정거리가 더욱 긴 경우
        max_diff.append(real[0][1] - test[0][1]) #계속 pop 해주기 떄문에 그냥 이렇게 비교해도 문제없음
        real.pop(0) #test는 다 소모했으므로 버리기
        test[0][0] = diff #남는 차이로 업데이트
    else:
        max_diff.append(real[0][1] - test[0][1]) #계속 pop 해주기 떄문에 그냥 이렇게 비교해도 문제없음
        real.pop(0) 
        test.pop(0)

if max(max_diff) >= 0:
    print(max(max_diff))   
        
else :
    print(0)