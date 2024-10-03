# Một bộ ba số (a, b, c) được gọi là bộ ba nguyên tố cùng nhau nếu a < b < c 
# và các cặp (a,b), (b,c), (a,c) đều nguyên tố cùng nhau.
# Cho hai số nguyên dương L và R (10 < L < R < 200).
# Hãy viết chương trình liệt kê các bộ ba số nguyên tố cùng nhau trong đoạn [L, R].

# Input
# Chỉ có 2 số L và R

# Output
# Ghi ra các bộ ba số nguyên tố cùng nhau, mỗi bộ ba trên một dòng theo định dạng như trong ví dụ.
# Các bộ ba được liệt kê theo thứ tự từ điển tăng dần.

# Ví dụ
# Input
# 15 20
# Output
# (15, 16, 17)
# (15, 16, 19)
# (15, 17, 19)
# (16, 17, 19)
# (17, 18, 19)
# (17, 19, 20)

import math

a, b = [int(i) for i in input().split()]
for i in range(a, b + 1):
    for j in range(i + 1, b + 1):
        for k in range(j + 1, b + 1):
            if math.gcd(i, j) == 1 and math.gcd(j, k) == 1 and math.gcd(i, k) == 1:
                print("(" + str(i) + ", " + str(j) + ", " + str(k) + ")")