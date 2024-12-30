# Tí và Tèo được cô giáo cử đi mua quà để thưởng cho các thành viên trong lớp. 
#     Lớp học có tất cả M bạn học sinh, vì vậy hai bạn phải mua M món quà.
# Tại cửa hàng quà lưu niệm có tất cả N món quà, món thứ i có giá bán bằng c[i].
#     Tuy nhiên, có A món quà mà Tí thích, và B món quà mà Tèo thích. 
# Hai bạn tranh nhau một hồi, cuối cùng họ quyết định chọn một danh sách quà sao cho 
#     có ít nhất K món đồ mà cả 2 bạn cùng thích.
# Các bạn hãy xác định xem số tiền ít nhất cần phải chi trả để Tí và Tèo có thể mua được đủ số quà 
#     và thỏa mãn điều kiện của hai bạn hay không?

# Input:
#     Dòng đầu tiên là N, M, K (1 ≤ N ≤ 100 000, 1 ≤ M, K ≤ N).
#     Dòng tiếp theo gồm N số nguyên lần lượt là giá bán c[i] của món quà thứ i (1 ≤ c[i] ≤ 10^9).
#     Dòng tiếp gồm số nguyên A, theo sau A số nguyên x[i], lần lượt là số thứ tự các món quà mà Tí thích.
#     Dòng tiếp gồm số nguyên B, theo sau B số nguyên y[i], lần lượt là số thứ tự các món quà mà Tèo thích.
#         (1 ≤ x[i], y[i] ≤ N).
# Output: In ra một số nguyên là đáp án tìm được. Nếu không có phương án nào thỏa mãn, in ra -1.
#     Input:          Input:              Input:
#     4 3 2           4 3 2               4 2 2
#     3 2 2 1         3 2 2 1             3 2 2 1
#     2               2                   2
#     1 2             1 2                 1 2
#     2               3                   3
#     1 3             4 1 3               4 1 3
#     Output:         Output:             Output:
#     7               6                   -1
# Giải thích test 1: Mua quà 1, 2 và 3.

inf = 10**18
def solve():
    n, m, k = map(int, input().split())
    c = [0] + list(map(int, input().split()))
    A = int(input())
    x = list(map(int, input().split()))
    x = [i for i in x if i > 0 and i <= n]
    A = len(x)
    B = int(input())
    y = list(map(int, input().split()))
    y = [i for i in y if i > 0 and i <= n]
    B = len(y)

    if m < k or k > n or n < m or k > A or k > B: return print(-1)
    
    I = sorted(set(x).intersection(y),key=lambda x: c[x])
    X = sorted(x, key=lambda x: c[x])
    Y = sorted(y, key=lambda x: c[x])

    #converting code from thanhchaus2
    bool1, bool2 = {}, {}
    for i in I: bool1[i] = True

    take = max(0, 2*k - m)
    if take > len(I): return print(-1)

    total = 0
    for i in range(take):
        if bool2.get(I[i]): continue
        total += c[I[i]]
        bool2[I[i]] = True
        c[I[i]] = -1
        k -= 1
        m -= 1

    x1, x2 = k, k

    for i in range(len(X)):
        if x1 <= 0: break
        if bool2.get(X[i]): continue
        else:    
            total += c[X[i]]
            bool2[X[i]] = True
            if bool1.get(X[i]): x2-=1
            c[X[i]] = -inf
            x1 -= 1
            m -= 1
    for i in range(len(Y)):
        if x2 <= 0: break
        if bool2.get(Y[i]): continue
        else:
            total += c[Y[i]]
            bool2[Y[i]] = True
            c[Y[i]] = -inf
            x2 -= 1
            m -= 1

    if x1 > 0 or x2 > 0: return(print(-1))
    adj = []
    for i in range(1, n+1): adj.append((c[i], i))
    adj.sort()
    for i in range(1, n+1):
        if m <= 0: break
        if bool2.get(adj[i][1]): continue
        total += adj[i][0]
        bool2[adj[i][1]] = True
        m -= 1

    print(-1 if m > 0 else total)

solve()
