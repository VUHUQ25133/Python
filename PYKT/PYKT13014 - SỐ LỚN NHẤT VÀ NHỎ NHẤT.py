# Cho N số nguyên dương A[]. 
# Mỗi lần, bạn chọn một tổ hợp gồm K số, 
#     như vậy, có tất cả C(K, N) cách chọn.
# Bài toán đặt ra là hãy tính 
#     tổng của sự chênh lệch giữa số lớn nhất và nhỏ nhất 
#         trong tổ hợp được chọn của tất cả C(K, N) lần.
# Input:
#     Dòng đầu tiên là số nguyên N và K (1 ≤ N ≤ 105, 1 ≤ K ≤ N).
#     Dòng tiếp theo gồm N số nguyên A[i] (0 ≤ A[i] ≤ 109).
# Output: 
#     In ra đáp án tìm được theo modulo 109+7.

#     Input:          Output:
#     4 2
#     10 20 30 40     100

# Giải thích test: Có tất cả 6 khả năng: 
#       (10, 20), (20, 30), (30, 40), (10, 30), (20, 40), (10, 40).
# Tổng cộng = 10 + 10 + 10 + 20 + 20 + 30 = 100.

n, k = map(int, input().split())
a = sorted(map(int, input().split()))
mod = 1000000007
def pow(a, b):
    if b==0: return 1
    if b&1: return pow(a, b-1)*a % mod
    p = pow(a, b>>1)
    return p*p % mod
def inv(i): return pow(i, mod-2)
G = [0]*(n+1)
G[0] = 1
for i in range(1,n+1): G[i] = i*G[i-1] % mod
def C(N, R): return G[N] * inv(G[R]) % mod * inv(G[N-R]) % mod
ans, s = 0, 0
for i in range(n-k+1):
    s = (s + a[n-i-1] - a[i]) % mod
    ans = (ans + C(n-2-i, k-2) * s) % mod
if k==1: print(0)
else: print(ans)
