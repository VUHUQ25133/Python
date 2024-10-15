# Cho một phép toán có dạng a + b = c với a,b,c chỉ là các số nguyên dương có một chữ số.
# Hãy kiểm tra xem phép toán đó có đúng hay không.

# Input
# Chỉ có một dòng ghi ra phép toán (gồm đúng 9 ký tự)

# Output
# Ghi ra YES nếu phép toán đó đúng. Ghi ra NO nếu sai.

# Ví dụ

# 1 + 2 = 3
# YES

# 2 + 2 = 5
# NO

s = input()
a, b, c = int(s[0]), int(s[4]), int(s[8])

if a + b == c:
    print("YES")
else:
    print("NO")