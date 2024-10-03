# Một số nguyên dương được gọi là ưu thế nguyên tố nếu thỏa mãn cả hai điều kiện:
# Số chữ số của nó là một số nguyên tố
# Số lượng chữ số nguyên tố nhiều hơn số lượng chữ số không nguyên tố
# Viết chương trình kiểm tra một số nguyên có thỏa mãn ưu thế nguyên tố hay không.

# Input
# Dòng đầu ghi số bộ test, không quá 20.
# Mỗi bộ test ghi số nguyên dương N, ít nhất 3 chữ số nhưng không quá 500 chữ số
# Output
# Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ
# Input               Output
# 3
# 1234567             YES
# 22334455667         YES
# 23400300489898989   NO

import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1


for t in range(int(input())):
    a = list(int(i) for i in input())
    l, nt = len(a), 0
    for i in a:
        nt += isPrime(i)
    print('YES' if (isPrime(l) and nt > l - nt) else 'NO')