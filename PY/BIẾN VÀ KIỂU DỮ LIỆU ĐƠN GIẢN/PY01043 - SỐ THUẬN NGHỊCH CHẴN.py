# Cho số nguyên dương N không quá 6 chữ số.
# Hãy liệt kê các số nhỏ hơn N thỏa mãn cả ba điều kiện:
# N là số thuận nghịch
# Tất cả các chữ số của N đều chẵn
# Số chữ số của N cũng là một số chẵn

# Input
# Dòng đầu ghi số bộ test (không quá 10). Mỗi test viết một số N (22 < N <106)

# Output
# Ghi kết quả của mỗi test trên một dòng, mỗi số cách nhau đúng một khoảng trống.

# Ví dụ
# Input   Output
# 2
# 30      22
# 100     22 44 66 88

def isValid(s):
    if len(s) % 2 == 1 or s != s[::-1]:
        return False
    for i in s:
        if int(i) % 2 == 1:
            return False
    return True


for t in range(int(input())):
    n = int(input())
    for i in range(22, n, 2):
        if isValid(str(i)):
            print(i, end=' ')
    print()
