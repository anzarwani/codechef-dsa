t = int(input())
case = 0
while case < t:
    x,y,k,n = map(int, input().split())
    flag = False
    for i in range(n):
        p, c = map(int, input().split())

        if (x-y) <= p and k >= c:
            flag = True
            #print('yes')
            #break
    if flag:
        print('LuckyChef')
    else:
        print('Unluckychef')
    
    case += 1