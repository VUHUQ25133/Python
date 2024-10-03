# Cho hai số nguyên dương a và b. Hãy kiểm tra xem ước số chung lớn nhất của hai số này có tổng chữ số là nguyên tố hay không.
# Ví dụ a = 42, b = 28, ước số chung lớn nhất = 14. Tổng chữ số của ước số chung là 1+4=5 là một số nguyên tố.

# Input
# Dòng đầu ghi số bộ test. Mỗi test ghi trên một dòng hai số nguyên dương a,b (không quá 6 chữ số)

# Output
# Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

# Ví dụ

# Input           Output
# 3
# 28 42           YES
# 123 18          YES
# 550 55          NO

import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return n > 1


for t in range(int(input())):
    a, b = [int(i) for i in input().split()]
    if isPrime(sum(int(i) for i in str(math.gcd(a, b)))):
        print('YES')
    else:
        print('NO')
