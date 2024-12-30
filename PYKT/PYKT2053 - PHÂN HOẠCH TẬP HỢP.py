# Cho dãy số A[] có N phần tử. Bạn cần đếm số cách phân hoạch A thành 3 tập hợp con, 
# sao cho tổng các phần tử trong mỗi tập hợp con là bằng nhau.
# Input:
#     Dòng đầu tiên là số lượng bộ test (T ≤ 10).
#         Mỗi test bắt đầu bởi số nguyên N (N ≤ 15)
#         Dòng tiếp theo gồm N số nguyên dương A[i] (1 ≤ A[i] ≤ 106).
# Output: 
#     Với mỗi test, in ra đáp án tìm được trên một dòng.

# Input:                Output
# 2
# 5                     6  
# 10 20 25 5 30         0
# 3
# 1 2 3

# Giải thích test 1:
# 11223
# 11332
# 22113
# 22331
# 33112
# 33221

from sys import stdin
un, a = [], []
r = [0]
def Try(pre, sum, ind, p, n):
    if sum > p: return
    if ind == 2: 
        r[0] += 1
        return
    if sum == p: return Try(0, 0, ind + 1, p, n)
    for i in range(pre, n):
        if un[i]: 
            un[i] = 0
            Try(i + 1, sum + a[i], ind, p, n)
            un[i] = 1
    return

for t in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()))
    SUM = sum(a)
    if SUM % 3 != 0:
        print(0)
        continue
    un = [1]*n
    r=[0]
    Try(0, 0, 0, SUM // 3, n)
    print(r[0])
