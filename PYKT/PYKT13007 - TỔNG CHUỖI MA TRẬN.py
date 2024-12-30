# Yêu cầu: Cho ma trận A kích thước n x n và số nguyên dương k, 
#     hãy tính +...+ B = A + A^2 +...+ A^k.
# Input:
#     Dòng đầu chứa hai số nguyên n và k (1 ≤ n ≤ 20, 1 ≤ k ≤ 10^9).
#     Dòng tiếp theo, mỗi dòng chứa n số nguyên biểu diễn ma trận A.
# Output:
#     In ra n dòng, mỗi dòng n số mô tả ma trận B, vì giá trị mỗi phần tử của ma trận B có thể rất lớn, 
#     do đó chỉ cần đưa ra chữ số cuối cùng của từng phần tử của ma trận B.

#     Input:  Output:
#     2 3     2 4
#     0 1     4 6
#     1 1

n, k = map(int, input().split())

z = [[0]*n for i in range(n)]

def add(x, y):
    r = [i.copy() for i in z]
    for i in range(n):
        for j in range(n):
            r[i][j] = (x[i][j] + y[i][j])%10
    return r

def mul(x, y):
    r = [i.copy() for i in z]
    for i in range(n):
        for j in range(n):
            for k in range(n): r[i][j] += x[i][k]*y[k][j]
            r[i][j]%=10
    return r

I = [[0]*n for i in range(n)]

for i in range(n): I[i][i] = 1

def pow(A, B):
    if B==0: return I
    if B&1: return mul(A, pow(A, B-1))
    p = pow(A, B>>1)
    return mul(p, p)

def cal(A, K):
    if K == 0: return I
    if K == 1: return A
    if K&1: return add(cal(A, K-1), pow(A, K))
    return mul(cal(A, K>>1), add(I, pow(A, K>>1)))

a = []
for i in range(n): a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n): a[i][j]%=10
B = cal(a, k)
for i in B:
    for j in i: print(j, end=' ')
    print()
