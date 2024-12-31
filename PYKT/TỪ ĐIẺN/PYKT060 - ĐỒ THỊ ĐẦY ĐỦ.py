# Một đồ thị được coi là đầy đủ nếu tất cả các cặp đỉnh đều có cạnh nối trực tiếp đến nhau.
# Cho đồ thị vô hướng G với N đỉnh và M cạnh.
# Giả sử mỗi bước người ta lấy một đỉnh rồi xóa tất cả các cạnh nối với đỉnh đó, sau đó thiết lập cạnh tới tất cả các đỉnh mà trước đó chưa kết nối với nó.
# Hãy kiểm tra xem bằng cách này thì có thể đến một bước nào đó đồ thị trở thành đầy đủ hay không?
# Input
#     Dòng đầu ghi số đỉnh N (không quá 1000)
#     Dòng thứ 2 ghi số M là số cạnh (M < N*(N-1)/2)
#     Tiếp theo là M dòng, mỗi dòng ghi một cạnh của đồ thị.
# Output
#     Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra
# Ví dụ
#     Input       Output
#     3
#     2           NO
#     1 2
#     2 3

#     4
#     2           YES
#     1 3
#     2 4


n, m = int(input()), int(input())
zone = []
ke = [[0]*(n+1) for i in range(n+1)]
par = [-1]*(n+1)

for i in range(m):
    x, y = map(int, input().split())
    ke[x][y] = ke[y][x] = 1
    p = par[x] if par[y] == -1 else par[y]
    if p == -1:
        zone.append(set([x, y]))
        par[x] = par[y] = len(zone) - 1
    else:
        zone[p].add(x)
        zone[p].add(y)
        par[x] = par[y] = p

def check():
    for z in zone:
        for x in z:
            for y in z:
                if x!=y:
                    if ke[x][y] == 0 or ke[y][x] == 0: return False

    return True
if check(): print('YES')
else: print('NO')
