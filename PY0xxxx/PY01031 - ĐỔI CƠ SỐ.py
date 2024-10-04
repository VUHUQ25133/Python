# Cơ số từ 2 đến 36 được xây dựng từ 10 chữ số (0 đến 9) và 26 chữ cái Tiếng Anh in hoa (‘A’ đến ‘Z’).
# Hãy viết chương trình chuyển một số nguyên dương N trong cơ số 10 sang cơ số b. 
# Trong đó N không quá 100.000, 2 ≤ b ≤ 36.
# Input
# Dòng đầu ghi số bộ test, không quá 10.
# Mỗi bộ test ghi 2 số N và b.
# N là một số nguyên dương N trong cơ số 10, không quá 100.000.  2 ≤ b ≤ 36
# Output
# Với mỗi bộ test ghi ra kết quả đổi cơ số tương ứng.
# Ví dụ
# Input       Output
# 3
# 10 2        1010
# 2021 2      11111100101
# 31 16       1F


f = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
t = int(input())
for i in range(t):
    n, k = [int(x) for x in input().split()]
    s = ''
    while (n > 0):
        x = n % k
        s = f[x] + s
        n = int(n / k)
    print(s)