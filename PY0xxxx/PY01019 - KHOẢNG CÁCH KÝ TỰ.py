# Nhập xâu s1, giả sử gọi xâu đảo là s2. 
# Hãy kiểm tra xem khoảng cách ký tự cạnh nhau trong hai xâu có thỏa mãn công thức sau hay không:
#                       |s1[i] – s1[i-1]| = |s2[i] – s2[i-1]|   với tất cả giá trị 0 < i < N

# Input
# Dòng đầu ghi số bộ test. Mỗi bộ test là một xâu ký tự độ dài không quá 100000. Không có khoảng trống.

# Output
# Ghi ra YES hoặc NO.

# Ví dụ

# Input       Output
# 2
# acxz        YES
# bcxz        NO

def check(a, b):
    for i in range(1, len(a)):
        if abs(ord(a[i]) - ord(a[i - 1])) != abs(ord(b[i]) - ord(b[i - 1])):
            return 'NO'
    return 'YES'


for t in range(int(input())):
    a = input()
    print(check(a, a[::-1]))

