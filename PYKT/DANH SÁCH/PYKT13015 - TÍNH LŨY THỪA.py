# Cho các số nguyên a, b, c, d và M.
# Hãy tính giá trị biểu thức (a^b)^(c^d) theo modulo M.
# Input:
#     Dòng đầu tiên là số lượng bộ test T (T ≤ 10000).
#     Mỗi test gồm 5 số nguyên a, b, c, d, M (0 ≤ a, b, c, d ≤ 1e9, 1 ≤ M ≤ 1e7).
# Output: 
# Với mỗi test in ra đáp án tìm được trên 1 dòng.

#     Input:              Output:
#     2
#     3 1 2 2 1000        81
#     2 1 2 2 14          2

# Giải thích test 1: 3^4 = 81.

from math import gcd, sqrt
from sys import stdin, stdout
# input = open('d:/code/in.txt').readline
input = stdin.readline
N = 10**7
M = int(sqrt(N))
NT = [1]*(M+1)
for i in range(2, int(sqrt(M)+1)):
    if NT[i]:
        for u in range(i, M//i+1): NT[i*u]=0
nt = [x for x in range(2, M) if NT[x]]

def PHI(n):
    k = n
    for i in nt:
        if n%i==0: 
            k-=k//i 
            while n%i==0: n//=i 
    if n>1: k-=k//n 
    return k

def pow(a, b, m):
    if b==0: return 1
    if b&1: return a*pow(a,b-1,m)%m 
    p = pow(a,b>>1,m)
    return p*p%m

def modpow(p, b, c, d, m, t):
    M = m
    cp = 0
    while m%p == 0 and cp<b:
        cp+=1
        m//=p
    exp = (b*pow(c, d, t)%t - cp%t+t)%t 
    return pow(p, cp, M)*pow(p, exp, m)

for t in range(int(input())):
    a, b, c, d, M = map(int, input().split())
    a%=M 
    x = PHI(M)
    X = PHI(x)
    b%=x
    c%=x 
    d%=X
    if d == 0:
        c = 1
        d = 1
    if b == 0 or c == 0:
        print(1)
        continue
    if a == 0:
        print(0)
        continue
    ans = 1
    u = []
    for i in nt: 
        if a%i==0:
            cp = 0
            while a%i==0:
                a//=i
                cp += 1
            u.append((i, cp))
    if a>1: u.append((a,1))
    for i in u: ans = ans*modpow(i[0], i[1], c, d, M, x)%M
    ans = pow(ans, b, M)
    stdout.write(f'{str(ans)}\n')  
