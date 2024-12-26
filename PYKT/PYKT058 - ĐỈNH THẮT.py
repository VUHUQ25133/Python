# Cho đồ thị có hướng liên thông G có N đỉnh và M cạnh. 
# Với một cặp đỉnh (u,v), đỉnh thắt của cặp đỉnh này được định nghĩa là một đỉnh mà tất cả đường đi từ u tới v đều đi qua nó.
# Hãy đếm số đỉnh thắt với cặp đỉnh (u,v).
# Input
# Dòng đầu ghi số bộ test, không quá 100.
# Mỗi bộ test bắt đầu với một dòng ghi 4 số N, M, u, v (0< N <= 100; 1 < M <=1000; 1 <= u,v <= N).
# Tiếp theo là M dòng ghi các cạnh của đồ thị
# Output
# Với mỗi bộ test, ghi ra số đỉnh thắt của cặp đỉnh (u,v)
# Ví dụ
# Input       Output
# 2
# 5 7 1 3     2
# 1 2
# 2 4
# 2 5
# 3 1
# 3 2
# 4 3
# 5 4
# 4 5 1 4     0
# 1 2
# 1 3
# 2 3
# 2 4
# 3 4

def check(ke, u, v, e, n):
    q, un = [u], [0]*(n+1)
    un[u] = 1
    while len(q) > 0:
        x = q.pop()
        if x == v:
            return False
        for i in ke[x]:
            if un[i] == 0 and i != e:
                q.append(i)
                un[i] = 1
    return True


for t in range(int(input())):
    n, m, u, v = map(int, input().split())
    ke = {x: [] for x in range(1, n+1)}
    for i in range(m):
        x, y = map(int, input().split())
        ke[x].append(y)
    cnt = 0
    for i in range(n+1):
        if i != u and i != v:
            if check(ke, u, v, i, n):
                cnt += 1
    print(cnt)