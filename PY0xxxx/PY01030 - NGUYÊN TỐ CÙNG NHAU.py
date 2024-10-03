# Một cặp số nguyên dương (a,b) được gọi là nguyên tố cùng nhau nếu a và b có ước chung lớn nhất bằng 1.
# Cho hai số nguyên dương N và K trong đó 10 < N < 10000; 1 < K < 6.
# Hãy liệt kê các số có K chữ số thỏa mãn nguyên tố cùng nhau với N.

# Input
# Chỉ có một dòng ghi hai số N và K

# Output
# Ghi ra lần lượt các số thỏa mãn theo thứ tự từ nhỏ đến lớn. Mỗi dòng ghi 10 số.

# Ví dụ

# Input
# 123 2
# Output
# 10 11 13 14 16 17 19 20 22 23
# 25 26 28 29 31 32 34 35 37 38
# 40 43 44 46 47 49 50 52 53 55
# 56 58 59 61 62 64 65 67 68 70
# 71 73 74 76 77 79 80 83 85 86
# 88 89 91 92 94 95 97 98

import math


n, k = [int(i) for i in input().split()]
lower, upper = 10**(k - 1), 10**k
count = 0
for i in range(lower, upper):
    if math.gcd(n, i) == 1:
        print(i, end=' ')
        count += 1
        if count % 10 == 0:
            print()