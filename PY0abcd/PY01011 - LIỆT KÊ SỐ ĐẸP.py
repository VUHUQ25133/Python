# Cho số nguyên dương N, hãy liệt kê các số thuận nghịch nhỏ hơn N thỏa mãn điều kiện:

# Chỉ có các chữ số 0,2,4,6,8
# Số chữ số của N chia cho 2 dư 1

# Input
# Dòng đầu ghi số bộ test (không quá 10). Mỗi test viết một số N (22 < N <106)

# Output
# Ghi kết quả của mỗi test trên một dòng, mỗi số cách nhau đúng một khoảng trống.

# Ví dụ

# Input               Output
# 2
# 30                  22
# 100                 22 44 66 88

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