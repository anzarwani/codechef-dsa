t = int(input())
case = 0
while case < t:
    n,c = map(int, input().split())
    arr = list(map(int, input().split()))

    if c >= sum(arr):
        print('Yes')
    else:
        print('No')
    case += 1