# Cho một lưới hình vuông kích thước N*N. 
# Trên một số ô của lưới người ta đặt các đồng xu (ký hiệu bằng chữ cái C (coin)). 
# Hãy đếm xem có thể lấy ra bao nhiêu cặp đồng xu ở cùng một hàng hoặc cùng một cột.
# Input
#     Dòng đầu tiên ghi số N (1 ≤ N ≤ 100)
#     N dòng tiếp theo mô tả trạng thái của lưới, chữ cái C ứng với vị trí có đồng x, dấu chấm tương ứng với ô trống)
# Output
#     Ghi ra số cặp đồng xu đếm được.
# Ví dụ
#     Input
#     4
#     CC..
#     C..C
#     .CC.
#     .CC.
#     Output
#     9

n, ans = int(input()), 0
a = []
for i in range(n): a.append(input())
for i in range(n):
    for j in range(n):
        if a[i][j] == 'C':
            for k in range(i+1, n): ans += 1 if a[k][j] == 'C' else 0
            for k in range(j+1, n): ans += 1 if a[i][k] == 'C' else 0
print(ans)