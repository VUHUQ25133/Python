# Cho đồ thị có hướng liên thông G có N đỉnh và M cạnh. 
# Với một cặp đỉnh (u,v), đỉnh thắt của cặp đỉnh này được định nghĩa là một đỉnh mà tất cả đường đi từ u tới v đều đi qua nó.
# Hãy đếm số đỉnh thắt với cặp đỉnh (u,v).
# Input
#     Dòng đầu ghi số bộ test, không quá 100.
#     Mỗi bộ test bắt đầu với một dòng ghi 4 số N, M, u, v (0< N <= 100; 1 < M <=1000; 1 <= u,v <= N).
#     Tiếp theo là M dòng ghi các cạnh của đồ thị
# Output
#     Với mỗi bộ test, ghi ra số đỉnh thắt của cặp đỉnh (u,v)
# Ví dụ
# Input           Output
# 2
# 5 7 1 3         2
# 1 2
# 2 4
# 2 5
# 3 1
# 3 2
# 4 3
# 5 4
# 4 5 1 4         0
# 1 2
# 1 3
# 2 3
# 2 4
# 3 4

def check(n, k, u, v, ke) :
    q, a = [u], [0] * (n + 1)
    a[u] = 1
    while len(q) > 0 :
        x = q.pop()
        if x == v : return False
        for i in ke[x] :
            if a[i] == 0 and i != k :
                q.append(i)
                a[i] = 1
    return True 

for t in range(int(input())) :
    n, m, u, v = [int(x) for x in input().split()]
    ke = []
    for i in range(n + 1) : ke.append([])
    for i in range(m) :
        x, y = [int(x) for x in input().split()]
        ke[x].append(y)
    ans = 0
    for i in range(1, n + 1) :
        if i != u and i != v :
            if check(n, i, u, v, ke) : ans += 1
    print(ans)