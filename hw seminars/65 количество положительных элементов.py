N = int(input())
a = list(map(int, input().split()))

print([a[-1]] + a[:-1])