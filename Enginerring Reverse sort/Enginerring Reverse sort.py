import sys, os
if not os.environ.get("ONLINE_JUDGE"):
    sys.stdin=open('in_eng.txt', 'r')
    sys.stdout=open('out_eng.txt', 'w')
import time
start_time = time.time()

T = int(input())

def construct(N,C,M):
    if(N==1):
        return str(M)

    else:
        if((C-1) >= N-2 and (C-1) <= N*(N-1)/2 -1):


            return str(M) + " " + construct(N-1,C-1, M+1)
        else:
            delta = int(C- N*(N-1)/2 +1)
            y = construct(N-1, C-delta, M+1)

            smallarr = y.split(" ")
            newarr = [str(M)]
            newarr.extend(smallarr)

            ans = " ".join(newarr[:delta][::-1]+newarr[delta:])
            return ans




for case in range(1, T+1):
    N, C = list(map(int,input().strip().split()))

    if C < N-1 or C > N*(N+1)/2 -1:
        print("Case #" + str(case) + ": IMPOSSIBLE")

    else:
        A= construct(N,C,1) 
        print("Case #" + str(case) + ": " + A)