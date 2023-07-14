k, p, n = map(int, input().split())

result = k 
for i in range(n):
    a = result % 1000000007
    b = p % 1000000007 
    result = (a * b) % 1000000007

# a x b mod m = ((a mod m) x (b mode m)) mod m 이라는 신기한 공식을 사용하면된다

print(result)
