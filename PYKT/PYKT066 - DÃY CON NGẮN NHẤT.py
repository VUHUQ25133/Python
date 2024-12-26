# Cho dãy số A[] có N phần tử. 
# Nhiệm vụ của bạn là tìm dãy con liên tiếp có độ dài nhỏ nhất, 
# sao cho Ước số chung lớn nhất của tất cả các phần tử trong dãy đúng bằng K.
# Input
#     Dòng đầu tiên là số lượng bộ test T (T <= 10).
#     Mỗi test bắt đầu bằng 2 số nguyên N và K.
#     Dòng tiếp theo gồm N số nguyên A[i] .
#     Giới hạn: 1 <= N <= 1000; 1 <= A[i], K <= 10^9
# Output
#     Với mỗi test, hãy in ra đáp án trên một dòng. Nếu không tìm được dãy con nào, in ra -1.
# Ví dụ:
#     Input                       Output
#     3
#     8 3
#     6 9 7 10 12 24 36 27        2
#     4 3
#     2 4 6 8                     -1
#     4 6
#     1 2 3 6                     1

from math import gcd

def check(a, l, r, len):
    for i in range(l, r-len+2):
        x = a[i]
        for j in range(i+1, i+len): x = gcd(x, a[j])
        if x==1: return True
    return False

def find_min(a, l, r):
    oke = False
    L, R = 0, r-l+2
    while L < R:
        len = (L+R) >> 1
        if check(a, l, r, len):
            oke = True
            R = len
        else: L = len + 1
    return (oke, L)

def solve(e, I):
    n, k = e[I:I+2]
    I+=2
    a = e[I:I+n]
    I+=n
    if k <= 0: return I
    for i in range(n):
        if a[i] % k == 0:
            a[i]//=k
            if a[i] == 1:
                print(1)
                return I
        else: a[i] = -1
    l, r, ans, oke = 0, 0, 10**9, False
    while l < n and r < n:
        while l < n and a[l] == -1: l+=1
        if l == n: break
        r=l
        while r<n-1 and a[r+1] != -1: r+=1
        res = find_min(a, l, r)
        if res[0] == True:
            oke = True
            ans = min(ans, res[1])
        l = r + 1
    if oke: print(ans)
    else: print(-1)
    return I

T = int(input())
e = []
while True:
    try: e.extend(map(int, input().split()))
    except: break
I = 0
for t in range(T): I = solve(e, I)
    
