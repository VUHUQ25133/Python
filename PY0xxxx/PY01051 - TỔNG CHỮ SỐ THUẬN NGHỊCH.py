# Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
# Hãy kiểm tra xem tổng các chữ số của N có phải là một số thuận nghịch hay không.
# Một số chỉ được coi là thuận nghịch nếu nhiều hơn 1 chữ số và số đảo của nó đúng bằng nó.

# Input
# Dòng đầu ghi số bộ test (không quá 20).
# Mỗi test ghi số N (không quá 500 chữ số)

# Output
# Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ
# Input                   Output
# 2
# 12341                   YES
# 22222222222222222222    NO

for t in range(int(input())):
    S = str(sum(int(i) for i in input()))
    print('YES' if len(S) > 1 and S == S[::-1] else 'NO')


