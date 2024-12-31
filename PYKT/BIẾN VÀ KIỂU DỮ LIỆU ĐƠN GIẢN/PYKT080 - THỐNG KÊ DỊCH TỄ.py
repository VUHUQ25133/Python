# Trước diễn biến phức tạp của dịch bệnh COVID...
# Thông tin về bệnh nhân được biểu diễn trên ma trận. 
# Bạn hãy thực hiện thống kê nhanh các trường hợp có nguy cơ lây nhiễm. 
# Nguyên tắc tính là đếm các trường hợp xung quanh bệnh nhân đã tiếp xúc (8 ô xung quanh).

# Input:
#     Dòng đầu tiên là 2 số M, N là các số nguyên <= 100, 
#         cho biết kích thước của ma trận.
#     Tiếp theo là ma trận M x N, các số nguyên A[i][j] có giá trị < 10. 
#         Vị trí của mỗi bệnh nhân được đánh số -1. 
#     Các ô mang giá trị >= 0 thể hiện số trường hợp có nguy cơ lây nhiễm (không tính các bệnh nhân).
# Output: Tổng số các ca có nguy cơ lây nhiễm trên toàn thành phố.

#     Input:          Output:
#     4 4             8
#     1 1 0 1
#     2 -1 4 5
#     0 0 0 0
#     1 0 2 1

n, m = map(int, input().split())
s, a = 0, []
for i in range(n): a.append(list(map(int, input().split())))
mark = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0: continue
                    if 0 <= x + i and x + i < n and \
                       0 <= j + y and j + y < m and mark[i+x][j+y] == 0:
                        s+=a[i+x][j+y]
                        mark[i+x][j+y]=1
print(s)
