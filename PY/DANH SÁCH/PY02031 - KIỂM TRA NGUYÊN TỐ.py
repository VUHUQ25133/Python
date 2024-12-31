# Cho ma trận A[] cỡ N*M chỉ bao gồm các số nguyên dương không quá 1000. 
# Hãy kiểm tra các số trong ma trận, nếu giá trị nào là số nguyên tố thì thay thế bằng số 1, không phải thì thay thế bằng số 0.
# Input
# Dòng đầu ghi 2 số N và M là kích thước ma trận (1 < N,M < 20)
# N dòng tiếp theo mỗi dòng có M số mô tả ma trận
# Output
# Ghi ra ma trận kết quả
# Ví dụ
# Input           Output
# 3 3
# 1 2 3           0 1 1
# 4 5 6           0 1 0
# 7 8 9           1 0 0

import math

def prime(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

n, m = [int(i) for i in input().split()]
for i in range(n):
    list = [prime(int(i)) for i in input().split()]
    print(*list)
