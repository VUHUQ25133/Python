# Cho một số nguyên dương không quá 500 chữ số.

# Hãy kiểm tra xem số đó có thỏa mãn đồng thời ba tính chất sau hay không?
# Vị trí chẵn là chữ số chẵn
# Vị trí lẻ là chữ số lẻ
# Tổng chữ số là một số nguyên tố.
# Input
# Dòng đầu ghi số bộ test (không quá 10)
# Mỗi bộ test ghi trên một dòng giá trị số nguyên (không quá 500 chữ số)
# Output
# Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ
# Input                       Output
# 2
# 2345678521                  YES
# 1212121212121212121212121   NO

import math

def check(s):
    for i in range(len(s)):
        if i % 2 != int(s[i]) % 2:
            return 'NO'

    n = sum(int(i) for i in s)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 'NO'
    return 'YES' if n > 1 else 'NO'

for t in range(int(input())):
    print(check(input()))