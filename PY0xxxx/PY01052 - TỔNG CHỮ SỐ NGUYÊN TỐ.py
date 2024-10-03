# Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
# Hãy kiểm tra xem tổng các chữ số của N có phải là một số nguyên tố hay không.

# Input
# Dòng đầu ghi số bộ test (không quá 20).
# Mỗi test ghi số N (không quá 500 chữ số)

# Output
# Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ
# Input                   Output
# 2
# 12341                   YES
# 22222222222222222222    NO

import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1

for t in range(int(input())):
    S = sum(int(i) for i in input())
    print('YES' if isPrime(S) else 'NO')
