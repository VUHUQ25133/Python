# Dãy số Fibonacci được định nghĩa theo công thức như sau:
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2 với n>2
# Cho hai số nguyên dương a và b (1 < a < b < 93). Viết chương trình liệt kê các số Fibonacci từ a đến b.
# Input
# Dòng đầu ghi số bộ test, không quá 10.
# Mỗi bộ test viết trên một dòng hai số a và b.
# Output
# Ghi ra kết quả của mỗi test trên một dòng, mỗi số cách nhau một khoảng trống.
# Ví dụ
# Input
# 1
# 1 10
# Output
# 1 1 2 3 5 8 13 21 34 55

f = [1] * 93
for i in range(3, 93):
    f[i] = f[i - 1] + f[i - 2]

for t in range(int(input())):
    a, b = [int(i) for i in input().split()]
    for i in range(a, b + 1):
        print(f[i], end=' ')
    print()
