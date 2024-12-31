# Một số số nguyên dương có thể được biểu diễn thành tổng của các số nguyên dương liên tiếp.
# Ví dụ: 6 = 1 +2 + 3 hoặc 9 = 4 + 5 hoặc 9 = 2 + 3 + 4
# Cho số nguyên dương N không quá 9 chữ số. 
# Hãy đếm xem có bao nhiêu cách biểu diễn N thành tổng các số nguyên dương liên tiếp.

# Input
# Dòng đầu ghi số bộ test, không quá 20.
# Mỗi bộ test ghi một số nguyên dương N, không quá 9 chữ số.
# Output
# Ghi ra số cách tìm được.

# Ví dụ

# Input       Output
# 3
# 6           1
# 8           0
# 9           2

from math import sqrt

for t in range(int(input())):
    n = int(input())
    n *= 2
    res = 0
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            if(n/i - i + 1) % 2 == 0:
                res += 1
    print(res)