# Cho số nguyên dương N, đếm số cách chia các số từ 1 đến 2N thành N nhóm, 
# mỗi nhóm gồm 2 số mà hiệu hai số trong một nhóm bằng hiệu hai số trong nhóm khác.

#     Input
#         Dòng đầu tiên chứa số lượng bộ test T.
#         Mỗi test gồm 1 số nguyên dương N.
#         Giới hạn:
#             Subtask 1 (50%): T, N <= 10000
#             Subtask 2 (50%): T <= 10^5, N <= 10^6.
#     Output:
#         Với mỗi test, hãy in ra đáp án tìm được trên một dòng.
# Example:
# Input           Output
# 2
# 1               1
# 2               2

# Giải thích test 2: Có 2 cách chia nhóm là
# (1, 2) và (3, 4)
# (1, 3) và (2, 4)

from sys import stdin
maxn = 10**6
U = [0]*(maxn + 1)
for i in range(2, 1000):
    if U[i] == 0:
        for u in range(i, 1+ maxn // i): U[u * i] = i

for t in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n < 1:
        print(0)
        continue
    ans = 1
    while(U[n]):
        u = U[n]
        cnt = 0
        while n % u == 0:
            cnt += 1
            n //= u
        ans *= (cnt+1)
    if n > 1: ans *= 2
    print(ans)
