# Cho số nguyên dương N, giả sử ta đếm được K số nguyên dương nhỏ hơn N có tính chất nguyên tố cùng nhau với N. 
# Hãy kiểm tra xem K có phải là số nguyên tố hay không.

# Input
# Dòng đầu ghi số bộ test, không quá 10.
# Dòng thứ 2 ghi số N (1 < N < 10000)

# Output
# Với mỗi test ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ

# Input           Output
# 2
# 2               NO
# 3               YES

import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


for t in range(int(input())):
    n = int(input())
    k = 0
    for i in range(1, n):
        if math.gcd(n, i) == 1:
            k = k + 1
    if isPrime(k):
        print('YES')
    else:
        print('NO')


