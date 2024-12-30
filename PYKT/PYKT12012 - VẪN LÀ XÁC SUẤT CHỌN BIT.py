# Chọn ngẫu nhiên một số X trong đoạn [A, B], sau đó chọn ngẫu nhiên một bit của X. 
#   Xác suất để bit chọn được là bit 1 bằng bao nhiêu?
# Input
#     Dòng đầu tiên là số lượng bộ test T (T ≤ 200).
#     Mỗi test gồm 2 số nguyên A và B (1 ≤ A ≤ B ≤ 10^10).
# Output
#     In ra đáp án tìm được với độ chính xác 5 chữ số sau dấu phảy.

#     Input           Output
#     3               
#     2 4             0.61111
#     3 5             0.66667
#     20 40           0.55556

# Giải thích test 1: (10) (11) (100)
# Xác suất để chọn được bit 1 là : 1/3 x (1/2 + 1 + 1/3) = 11/18.

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)
def C(n, k):
    if k > n: return 0
    if k > n-k: k = n-k
    tu, mau = 1, 1
    for i in range(1, k+1):
        tu *= (n-k+i)
        mau *= i
        g = gcd(tu, mau)
        tu //= g
        mau //= g
    return tu // mau

def count(i, j, x): #number of integer which hav i bit and j + 1 bit 1 and <= xs
    s = bin(x)[2:]
    if i > len(s): return 0
    if i < len(s): return(C(i-1, j))
    ans = 0
    rm = j
    for k in range(1, i):
        if rm < 0: break
        if s[k] == '1':
            ans += C(i-k-1, rm)
            rm -= 1
    if rm >= 0 and s.count('1') == j + 1: ans += 1
    return ans
def solve(a, b):
    n = len(b)
    s = [[0]*(n+1) for i in range(n+1)]
    for i in range(len(a), n+1):
        for j in range(i):
            s[i][j] = count(i, j, int(b, 2)) - count(i, j, int(a, 2) - 1)
    ans = 0
    for i in range(len(a), n+1):
        sum = 0
        for j in range(i):
            sum += s[i][j] * (j+1)
        ans += sum / i
    print(f'{(ans/(int(b, 2) - int(a, 2) + 1)):.5f}')
for t in range(int(input())):
    a, b = map(int, input().split())
    solve(bin(a)[2:], bin(b)[2:])
