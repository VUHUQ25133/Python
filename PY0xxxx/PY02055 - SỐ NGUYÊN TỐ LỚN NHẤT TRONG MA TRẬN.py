# Cho ma trận A cỡ N*M chỉ bao gồm các số nguyên dương.
# Hãy tìm số nguyên tố lớn nhất trong ma trận và các vị trí có giá trị bằng số nguyên tố lớn nhất đó.
# Input
#     Dòng đầu ghi hai số N và M (1 < N, M < 50)
#     Tiếp theo là N dòng ghi các giá trị của ma trận, không có số nào lớn hơn 1000.
# Output
#     Ghi ra giá trị của số nguyên tố lớn nhất. 
#     Sau đó lần lượt là các vị trí của số nguyên tố lớn nhất, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). 
#     Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.
#     Nếu không tìm thấy số nguyên tố nào thì ghi ra NOT FOUND
# Ví dụ
# Input               Output
# 6 4
# 23 21 26 10         Vi tri [2][1]
# 13 13 22 14         Vi tri [3][0]
# 28 29 28 23         Vi tri [5][3]
# 29 19 11 19
# 16 26 24 21
# 13 25 21 29
# 29

from math import sqrt

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n >= 2

n, m = map(int, input().split())
a = [[0] * m]*n
res = -1

for i in range(n):
    a[i] = [int(i) for i in input().split()]
    for j in a[i]:
        if isPrime(j) and j > res:
            res = j

if res == -1:
    print('NOT FOUND')
else:
    print(res)
    for i in range(n):
        for j in range(m):
            if a[i][j] == res:
                print('Vi tri [{}][{}]'.format(i, j))
