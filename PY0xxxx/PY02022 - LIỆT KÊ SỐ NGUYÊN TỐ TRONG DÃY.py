# Cho dãy số nguyên dương A[] có N phần tử. 
# Hãy viết chương trình liệt kê các số nguyên tố khác nhau và số lần xuất hiện của số đó trong dãy ban đầu.
# Các số được liệt kê theo thứ tự xuất hiện.
# Input
# Dòng đầu ghi số N (không quá 500).
# Dòng sau ghi N số của dãy (không quá 6 chữ số).
# Output
# Ghi ra các số nguyên tố khác nhau trong dãy theo thứ tự xuất hiện và số lần xuất hiện. 
# Mỗi số liệt kê trên 1 dòng.
# Ví dụ
# Input                   
# 10
# 2 4 7 5 7 8 9 3 7 2
# Output
# 2 2
# 7 3
# 5 1
# 3 1

from imaplib import Int2AP
import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n >= 2


n = int(input())
a = [int(i) for i in input().split()]
m = {}
for i in a:
    if isPrime(i):
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
for i in m:
    print(str(i) + " " + str(m[i]))
