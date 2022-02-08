import sys,math,cmath,time
start_time=time.time()
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s=input()
    return(s[:len(s)-1])
def invr():
    return(map(int,input().split()))
def solve():
    n=inp()
    a=[]
    for i in range(n):
        s=inlt()
        a.append(s)
    trace=0
    for i in range(n):
        trace=trace +a[i][i]
    r=[[0] * n for i in range(n)]
    rc=0
    for i in range(n):
        for j in range(n):
            r[i][a[i][j]-1]+=1
        if 0 in r[i]:
            rc=rc+1
    c=[[0] * n for i in range(n)]
    cc=0
    for i in range(n):
        for j in range(n):
            c[i][a[j][i]-1]+=1
        if 0 in c[i]:
            cc=cc+1
    print("Case #" + str(tt+1) + ":" ,trace,rc,cc)
j_k= __debug__
if not j_k:
    sys.stdin=open('input.txt','r')
    sys.stdout=open('output.txt','w')
else:
    input = sys.stdin.readline
t=1
t=inp()
for tt in range(t):
    solve()
if not j_k:
    print("Time elapsed:",time.time()-start_time,"seconds")
sys.stdout.close()
