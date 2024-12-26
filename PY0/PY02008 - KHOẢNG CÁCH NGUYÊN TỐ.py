# Cho hai số nguyên N và X.
# Bắt đầu từ số X, hãy liệt kê N+1 số liên tiếp sao cho 
# khoảng cách giữa số trước và số sau lần lượt là các số trong dãy N số nguyên tố đầu tiên.
# Ví dụ N=5 và X=4. Vì 5 số nguyên tố đầu tiên là 2 3 5 7 11 nên ta có 6 số trong dãy cần liệt kê là: 4 6 9 14 21 32
# Input
# Chỉ có 1 dòng ghi 2 số N và X. (2 ≤ N ≤ 1000; 1 ≤ X ≤ 100)
# Output
# Ghi ra trên một dòng lần lượt N+1 số của dãy kết quả.
# Ví dụ
# Input
# 5 4
# Output
# 4 6 9 14 21 32

import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n >= 2

list = [0, 2]
k = 3
while (len(list) <= 1001):
    if (isPrime(k)):
        list += [k]
    k += 2

n, x = [int(i) for i in input().split()]
for i in range(n + 1):
    x += list[i]
    print(x, end=' ')
