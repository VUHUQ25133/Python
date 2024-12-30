# Tìm số nguyên x nhỏ nhất sao cho a^x = b modulo M.

# Input:
#     Dòng đầu tiên là số lượng bộ test T (1 ≤ T ≤ 10).
#     Mỗi test gồm 3 số nguyên a, b, M (2 ≤ M ≤ 1010, 1 ≤ a, b, ≤ M).
#     Input đảm bảo gcd(a, M) = 1.
# Output: 
#     Với mỗi test in ra số nguyên x nhỏ nhất tìm được. Nếu không có đáp án, in ra -1.

#     Input:                  Output:
#     4                       3
#     3 2 5                   4
#     2 5 11                  -1
#     3 2 100                 7452
#     53849 260761 306148

import math

def solve(a : int, b : int, m : int):
    a %= m
    b %= m
    n = int(math.sqrt(m) + 1)

    an = 1
    for i in range(n):
        an = (an * a) % m
    
    vals = {}

    q = 0
    curr = b
    while q <= n:
        vals[curr] = q
        curr = (curr * a) % m
        q += 1
    
    p = 1
    curr = 1
    while p <= n:
        curr = (curr * an) % m
        if curr in vals:
            ans = n * p - vals[curr]
            return ans
        p += 1
    
    return -1

N = int(input())

while N > 0:
    N -= 1
    a, b, m = list(map(int, input().split()))

    print(solve(a, b, m))
