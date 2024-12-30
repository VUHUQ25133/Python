# Giải hệ phương trình Ax = B trong đó 
#     ma trận A có kích thước n x n, x và B là các vector cột có n phần tử:

#     a(1,1)x(1) + a(1,2)x(2) +...+ a(1,n)x(n) = b(1)
#     ............................................
#     a(n,1)x(1) + a(n,2)x(2) +...+ a(n,n)x(n) = b(n)
# Input:
#     Dòng đầu tiên là số lượng bộ test T (T ≤ 10).
#         Mỗi test bắt đầu bởi số nguyên N (2 ≤ N ≤ 20).
#         N dòng tiếp theo, mỗi dòng gồm N phần tử mô tả ma trận A.
#         Dòng cuối gồm N số nguyên, mô tả vector B.
#         Các hệ số có giá trị tuyệt đối không vượt quá 1000.
# Output: 
#     Với mỗi test in ra đáp án tìm được trên một dòng, in ra 3 chữ số sau dấu phảy. 
#     Nếu hệ vô nghiệm hoặc có vô số nghiệm, in ra -1.

#     Input       Output
#     3
#     3           -9.333 9.667 0.000
#     1 2 5       -1
#     4 5 6       -1
#     7 8 9
#     10 11 12
#     2
#     1 1
#     2 2
#     2 4
#     2
#     1 2
#     1 2
#     3 4


def zero(a: list, n):
    for i in range(n):
        if a[i] != 0: return False
    return True
def cmp(a: list):
    cnt = 0
    for i in range(len(a)-1):
        if a[i]!=0: break
        cnt+=1
    return 1
def solve(a, n):
    for i in range(n):
        if zero(a[i], n): return -1
        a.sort(key=cmp)
        if a[i][i] == 0: continue
        x = a[i][i]
        for j in range(i, n+1): a[i][j]/=x
        for j in range(i+1, n):
            y = a[j][i]
            for k in range(i, n+1): a[j][k] -= y*a[i][k]
    ans = [0]*n
    for i in reversed(range(n)):
        s = 0
        for j in range(i+1, n): s += ans[j]*a[i][j]
        ans[i] = (a[i][-1]-s)/a[i][i]
    return ans
        
for t in range(int(input())):
    n = int(input())
    a = []
    for i in range(n): a.append(list(map(int, input().split())))
    b = list(map(int, input().split()))
    for i in range(n): a[i].append(b[i])
    ans = solve(a, n)
    if ans == -1: print(-1)
    else:
        for i in ans: print(f'{i:.3f}', end=' ')
        print()
