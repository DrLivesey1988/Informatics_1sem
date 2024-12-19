x = int(input())
y = int(input())
a = int(input())
b = int(input())


if x == a or y == b or abs(a-x) == abs(b-y):
    print('YES')
else:
    print('NO')