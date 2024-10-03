# Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
# Hãy kiểm tra xem N có chia hết cho 3 hay không.

# Input
# Dòng đầu ghi số bộ test (không quá 20).
# Mỗi test ghi số N (không quá 500 chữ số)

# Output
# Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ
# Input                   Output
# 2
# 12341                   NO
# 123456789123456789      YES

for t in range(int(input())):
    n = int(input())
    print('YES' if n % 3 == 0 else 'NO')