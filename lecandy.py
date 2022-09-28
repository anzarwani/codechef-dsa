t = int(input())
case = 0
while case < t:
    n,c = input().split()
    n = int(n)
    c = int(c)
    arr = list(map(int, input().split()))

    for i in range(len(arr)):
        c -= arr[i]

    if c <= 0:
        print('No')
    else:
        print('Yes')
    case += 1



