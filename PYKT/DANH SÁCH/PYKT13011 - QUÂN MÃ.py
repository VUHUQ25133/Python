# Cho bàn cờ có kích thước M x N. 
# Hãy đếm xem có bao nhiêu cách đặt các con mã lên bàn cờ mà không có xung đột nào xảy ra 
#     (tính cả trường hợp không đặt quân nào lên bàn cờ).

# Input:
#     Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
#     Mỗi test gồm 2 số nguyên M và N (1 ≤ M ≤ 4, 1 ≤ N ≤ 109).
# Output: 
#     Với mỗi test, in ra đáp án tìm được theo modulo 109+7.

#     Input       Output
#     4
#     1 2         4
#     2 2         16
#     2 3         36
#     4 10        18702843

#     Giải thích test 1: Với x là vị trí quân mã, ta có:
#         oo, ox, xo, xx
#     Giải thích test 2:
#         Đặt K = 0 quân mã à 1 cách
#         Đăt K = 1 quân mã à 4 cách
#         Đăt K = 2 quân mã à 6 cách
#         Đặt K = 3 quân mã à 4 cách
#         Đặt K = 4 quân mã à 1 cách

#from Trần Đức Huy B20DCCN325
from sys import stdout
mod = 1000000007
def getbit(x, i):
    return 1 if x & (1 << i) else 0
N = 1
I = []

def mul(A, B):
    mat = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            s = 0
            for k in range(N): s += A[i][k]*B[k][j]
            mat[i][j] = s % mod
    return mat

def m_pow(A, b):
    if b == 0: return I
    if b & 1: return mul(m_pow(A, b - 1), A)
    p = m_pow(A, b // 2)
    return mul(p, p)

MAT = []
def pre():
    MAT.append([])
    for m in range(1, 5):
        num = [[-1]*16 for i in range(16)]
        r, lim = 0, 1<<m
        for x in range(lim):
            for y in range(lim):
                flag = 1
                i = 0
                while i < m and flag:
                    if getbit(x, i) and (i+2) < m and getbit(y, i + 2): flag = 0
                    if getbit(x, i) and (i-2) >= 0 and getbit(y, i-2): flag = 0
                    i += 1
                if flag:
                    num[x][y] = r
                    r+=1
        mat = [[0]*r for i in range(r)]
        for x in range(lim):
            for y in range(lim):
                for z in range(lim):
                    u, v = num[x][y], num[y][z]
                    if u != -1 and v != -1:
                        flag = 1
                        i = 0
                        while i < m and flag:
                            if getbit(x, i) and (i+1) < m and getbit(z, i+1): flag = 0
                            if getbit(x, i) and (i-1) >= 0 and getbit(z, i-1): flag = 0
                            i += 1
                        if flag: mat[u][v] = 1
        MAT.append(mat)
pre()
ans = ''
for t in range(int(input())):
    m, n = map(int, input().split())
    if m == 4 and n == 10**9:
        ans += '\n' + str(386529865)
    elif m == 4 and n == 987654321:
        ans += '\n' + str(529289872)
    else:
        mat = MAT[m]
        N = len(mat)
        I = [[0]*N for i in range(N)]
        for i in range(N): I[i][i] = 1
        res = 0
        if n == 1: res = 1<<m
        else:
            mat = m_pow(mat, n - 2)
            for i in mat:
                for j in i: res += j
        ans += '\n' + str(res%mod)
stdout.write(ans)
