# Một số nguyên dương N được gọi là Perfect Prime nếu N là số nguyên tố; 
#     đảo ngược các chữ số của N cũng là một số nguyên tố; 
#     tổng các chữ số của N là một số nguyên tố và mỗi chữ số của N cũng là một số nguyên tố. 
# Cho số nguyên dương N, hãy kiểm tra N có phải là Perfect Prime hay không? 
#     Đưa ra “Yes” nếu N là Perfect Prime, ngược lại đưa ra “No”.
# Input:
#     Dòng đầu tiên đưa vào T là số lượng bộ test.
#     Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
#     T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤1E7;
# Output:
#     Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input:  Output:
# 3
# 13      No
# 753     No
# 757     Yes

import math

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def deff(str):
    for i in str:
        if not isprime(int(i)):
            return 'No'
    s = sum([int(i) for i in str])
    num1, num2 = str, str[::-1]
    if not isprime(s) or not isprime(int(num1)) or not isprime(int(num2)):
        return 'No'
    return 'Yes'

for case in range(int(input())):
    print(deff(input()))
