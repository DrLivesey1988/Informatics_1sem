N = int(input())
a = list(map(int, input().split()))
x = int(input())

cnt = 0

for i in range(len(a)):
    if x == a[i]:
        cnt += 1
print(cnt)