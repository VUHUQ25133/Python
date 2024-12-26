# Ngân hàng thông báo lãi suất là X % mỗi năm.
# Với số tiền gửi vào là N. Sau mỗi năm, tiền lãi sẽ được cộng dồn.
# Hỏi sau bao nhiêu năm thì số tiền đạt được ít nhất là M.

# Input
# Dòng đầu ghi số bộ test.
# Mỗi test viết 3 số thực (kiểu double) N, X và M. Trong đó 0<N<M<100000.

# Output
# Ghi ra số năm tính được.

# Ví dụ

# Input                   Output
# 2
# 200.00 6.5 300          7
# 500 4 1000.00           18

import math

for t in range(int(input())):
    n, x, m = [float(i) for i in input().split()]
    # công thức tính lãi kép: m = n * (1 + x%) ^ res
    res = math.log(m / n, 1 + x / 100)
    print(math.ceil(res))