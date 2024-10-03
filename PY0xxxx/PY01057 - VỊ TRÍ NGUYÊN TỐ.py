# Trong 10 chữ số thập phân thì có 4 chữ số nguyên tố là 2, 3, 5, 7.
# Một số nguyên dương được coi là thỏa mãn nguyên tố đúng vị trí nếu thỏa mãn cả hai điều kiện:
# Nếu i là nguyên tố thì vị trí thứ i cũng phải là chữ số nguyên tố.
# Ngược lại nếu i không phải là số nguyên tố thì vị trí thứ i không phải là chữ số nguyên tố. 
# Ví dụ:  số 14239567 thỏa mãn nguyên tố đúng vị trí vì 
#         các vị trí thứ 2, 3, 5, 7 là các chữ số nguyên tố, các vị trí khác không nguyên tố. 

# Viết chương trình kiểm tra một số nguyên dương không quá 500 chữ số có thỏa mãn tính chất trên hay không. 

# Input
# Dòng đầu ghi số bộ test, không quá 10.
# Mỗi bộ test viết trên một dòng số nguyên dương không quá 500 chữ số.

# Output
# Với mỗi test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

# Ví dụ
# Input           Output
# 2
# 14239567        YES
# 2314514535353   NO

import math

# chưa hiểu sao dùng hàm này lại WA
# def isPrime(n):
#     return n == 2 or n == 3 or n == 5 or n == 7


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1

def check(s):
    for i in range(len(s)):
        if (isPrime(i) and not isPrime(int(s[i]))) or (not isPrime(i) and isPrime(int(s[i]))):
            return 'NO'
    return 'YES'

for t in range(int(input())):
    print(check(input()))