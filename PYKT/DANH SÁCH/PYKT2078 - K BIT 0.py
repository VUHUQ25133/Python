# Nhiệm vụ của bạn là hãy xác định xem các số trong phạm vi từ 0 tới N
#      có bao nhiêu số mà biểu diễn nhị phân của nó có đúng K chữ số 0.
# VD:  N = 20, K = 3, ta có
#      8 = 1000
#     17 = 10001
#     18 = 10010
#     20 = 10100

# Input:
#     Dòng đầu tiên là số lượng bộ test T (T <= 20).
#     Mỗi test gồm hai số nguyên N và K (0<= N < 2^31, 1 <= K <= 31).
# Output: 
#     Với mỗi test, in ra số lượng các số thỏa mãn có K bit 0.

# Input:        Output
# 2
# 20 3          4
# 8 1           4

# input = open('d:/code/in.txt').readline
maxn = 33
dp = [[0]*33 for i in range(maxn)]    #dp[i][j] number of number has k bit 0 which has i + 1 bit (first bit = 1) 
for i in range(maxn): dp[i][0] = 1
for i in range(1, maxn):
    for j in range(1, maxn):
        if i < j: dp[i][j] = 0
        else: dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
for t in range(int(input())):
    N, k = map(int, input().split())
    if N == 0:
        print(1 if k == 1 else 0)
        continue
    s = f'{N:b}'
    n = len(s)
    ans, pre = 0, 0
    for i in range(1, n):
        if s[i] == '1' and k > pre: 
            ans += dp[n - i - 1][k - pre - 1]
        if s[i] == '0': pre += 1
    if pre == k: ans += 1
    for i in range(n-1): ans += dp[i][k]
    if k == 1: ans += 1
    print(ans)
