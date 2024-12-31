# Cho ma trận A cỡ N*M chỉ bao gồm các số nguyên dương.
# Một số được coi là số may mắn nếu giá trị của nó đúng bằng khoảng cách giữa số lớn nhất và số nhỏ nhất của ma trận.
# Trong test ví dụ dưới đây, số lớn nhất là 77, số nhỏ nhất là 10. Giá trị may mắn là 67.
# Hãy tìm xem trong ma trận có tồn tại số may mắn hay không. Nếu có thì ở các vị trí nào?
# Input
#     Dòng đầu ghi hai số N và M (1 < N, M < 50)
#     Tiếp theo là N dòng ghi các giá trị của ma trận, không có số nào lớn hơn 10000.
# Output
#     Ghi ra giá trị bằng số may mắn nếu tìm được. 
#     Sau đó lần lượt là các vị trí tìm thấy, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). 
#     Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.
#     Nếu không tìm thấy giá trị bằng số may mắn nào thì ghi ra NOT FOUND
# Ví dụ
# Input               Output
# 6 4
# 23 21 77 10         67
# 13 13 22 14         Vi tri [2][1]
# 28 67 28 23         Vi tri [3][3]
# 29 77 11 67
# 16 51 24 21
# 13 25 77 77

n, m = [int(x) for x in input().split()]
a = [[0]] * n
Max, Min, ok, k = 0, 10**6, 0, 0
for i in range(n):
    a[i] = [int(x) for x in input().split()]
    Max = max(Max, max(a[i]))
    Min = min(Min, min(a[i]))
for i in range(n):
    for j in range(m):
        if a[i][j] == Max - Min:
            if k == 0:
                ok = 1
                print(Max - Min)
                k = 1
            print('Vi tri [', i, '][', j, ']', sep='')
if ok == 0:
    print('NOT FOUND')
