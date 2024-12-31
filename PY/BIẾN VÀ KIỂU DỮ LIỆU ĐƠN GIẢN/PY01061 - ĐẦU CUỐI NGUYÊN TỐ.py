# Cho số nguyên dương N có ít nhất 4 chữ số và không quá 500 chữ số.
# Một số được gọi là số đầu cuối nguyên tố nếu thỏa mãn cả hai điều kiện:
# Ba chữ số đầu ghép lại được một số nguyên tố
# Ba chữ số cuối ghép lại được một số nguyên tố
# Viết chương trình kiểm tra xem N có phải là đầu cuối nguyên tố hay không?

# Input
# Dòng đầu ghi số bộ test (không quá 20).
# Mỗi bộ test viết trên một dòng số N, ít nhất 4 chữ số và không quá 500 chữ số.

# Output
# Với mỗi test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ
# Input               Output
# 3
# 12743               YES
# 7337                YES
# 12345678901234      NO

import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n >= 2


for t in range(int(input())):
    s = input()
    print('YES' if isPrime(int(s[0:3])) and isPrime(int(s[-3:])) else 'NO')