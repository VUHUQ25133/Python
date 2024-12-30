# 3 số a, b, c được gọi là một bộ số Pytago nếu như a2 + b2 = c2.
# Cho số nguyên N, nhiệm vụ của bạn là hãy đếm bộ số (a, b, c) 
#     thỏa mãn 1 ≤ a,b,c ≤ N-1, a ≤ b và a^2 + b^2 = c^2 (mod N).
# Input:
#     Một số nguyên dương N (2 ≤ N ≤ 500 000).    
# Output: 
#     In ra một số nguyên là số bộ 3 số tìm được.

# Input:      7                       15
# Output:     18                      64


def exp(p, e):
    P = 1
    for i in range(e): P*=p
    return P
def exp(p, e):
    if e == 0: return 1
    if e&1: return exp(p, e - 1) * p
    P = exp(p, e // 2)
    return P*P

def powsols(p, e):
    P = exp(p, e)
    res = 0
    qr = [0]*P
    for i in range(P): qr[i*i%P] += 1
    for i in range(P): res += qr[i]*qr[(i+1)%P]
    sq = 0
    for i in range(0, P, p):
        sq = i*i%P
        res += qr[(sq+1)%P]
    res *= P//p*(p-1)
    if e > 1: res += powsols(p, e-2)*p*p*p 
    else: res += 1
    return res

def zeros(n):
    res = 1 + 3*qr[0]
    for i in range(n):
        res += qr[i]*(2*qr[i] + qr[(n-i)%n])
    return res

def diag(n):
    res = 0
    for i in range(1, n):
        res += qr[2*i*i%n]
    return res

n = int(input())
qr = [0]*n
N = n
res = 1
p = 2
while p*p <= n:
    if n%p == 0:
        e = 0
        while n%p == 0: 
            e+=1
            n//=p
        res*=powsols(p, e)
    p+=1
if n!=1: res*=powsols(n, 1)
qr = [0]*N
for i in range(1, N):
    qr[i*i%N] += 1
res -= zeros(N)
res += diag(N)
print(res // 2)
