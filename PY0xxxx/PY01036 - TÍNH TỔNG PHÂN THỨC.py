# Nhập số nguyên dương N (1 < N < 10000).

# Viết chương trình tính tổng:
# S = 1 + 1/3 + 1/5 + … + 1/N nếu N lẻ
# S = 1/2 + 1/4 + 1/6 + … + 1/N nếu N chẵn
# Kết quả được in ra với 6 chữ số phần thập phân.

# Input
# Dòng đầu ghi số bộ test, không quá 10.
# Mỗi test ghi một số N

# Output
# Với mỗi bộ test, ghi ra kết quả trên một dòng.

# Ví dụ
# Input       Output
# 2
# 10          1.141667
# 15          2.021800

for t in range(int(input())):
    n = int(input())
    sum = 0
    for i in range(2 - n % 2, n + 1, 2):
        sum += 1/i
    print('{:.6f}'.format(sum))
