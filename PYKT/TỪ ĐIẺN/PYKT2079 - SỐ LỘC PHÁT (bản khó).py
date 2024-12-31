# Theo quan niệm Á Đông, số 6 và 8 đọc là lục, bát, do vậy người ta hay liên tưởng tới lộc phát, là phát tài phát lộc.
# Nhiệm vụ của bạn là hãy xác định xem trong các số từ 1 => N và chia hết cho 8, tổng số lần xuất hiện chữ số 6 và 8 là bao nhiêu?
# Input:
#     Dòng đầu tiên là số lượng bộ test T (T <= 10^5).
#     Mỗi test gồm một số nguyên dương N (1 <= N <= 10^18)
# Output: Với mỗi test, in ra đáp án tìm được trên một dòng.

# Input     Output
# 4
# 10        1
# 18        2
# 33        2
# 56        4

# Giải thích test 4: Có 4 số thỏa mãn là 8, 16, 48, 56, tổng cộng có 4 chữ số thỏa mãn.

from sys import stdin
def pow(a, b):
    if b == 0: return 1
    if b & 1: return pow(a, b - 1)*a
    p = pow(a, b >> 1)
    return p*p
_ , __ = [0]*1001, [0]*19
for i in range(1, 1001): _[i] = _[i-1] + ((str(i).count('6') + str(i).count('8')) if i % 8 == 0 else 0)
total = _[-1]
__[1] = _[9]
__[2] = _[99]
__[3] = _[999]

for i in range(4, 19):
    __[i] = __[i-1] * 10 + 2 * pow(10, i - 4) * 125
    
for t in range(int(stdin.readline())):
    N = int(stdin.readline())
    ans = 0
    if N<=1000: ans = _[N]
    else: 
        n = str(N)
        M = len(n)
        ans += __[M-1]
        pre = 0 
        for i in range(M-3):
            const = pow(10, M-i-4)*125
            x = int(n[i])
            ans += x * __[M-i-1] 
            if i == 0: ans -= __[M-i-1]
            ans += pre * x * const
            if x > 6: ans += const
            if x > 8: ans += const
            if x == 6 or x == 8: pre += 1
        last = N%1000
        ans += _[last]
        ans += pre * (1 + last//8)
    print(ans)
