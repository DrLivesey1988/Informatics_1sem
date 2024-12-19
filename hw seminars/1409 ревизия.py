N = int(input())
a = list(map(int, input().split()))

last = float('inf')
prelast = float('inf')

for i in range(len(a)):
    if a[i]< last:
        prelast = last
        last = a[i]
    elif a[i] < prelast:
        prelast = a[i]
print(last, prelast)