# Cho số nguyên dương N có không quá 500 chữ số.
# Hãy kiểm tra xem 4 chữ số cuối cùng ghép lại có tạo thành một số nguyên tố hay không.
# Chú ý: các chữ số 0 ở đầu trong 4 chữ số cuối vẫn được chấp nhận

# Input
# Dòng đầu ghi số bộ test (không quá 20).
# Mỗi test viết trên một dòng số nguyên dương N, không quá 500 chữ số.

# Output
# Với mỗi bộ test ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ
# Input                       Output
# 3
# 12234323130097              YES
# 3443354654654654461123      YES
# 43543543434554659999        NO

import math

def check(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 'NO'
    return 'YES' if n > 1 else 'NO'


for t in range(int(input())):
    s = input()
    n = int(s[-4:])
    print(check(n))