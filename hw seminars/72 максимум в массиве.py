N = int(input())
a = list(map(int, input().split()))

max = float('-inf')

for i in range(len(a)):
    if a[i] > max:
        max = a[i]
print(max)