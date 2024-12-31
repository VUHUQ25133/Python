# Trong toán học, cặp số (a,b) được gọi là nguyên tố cùng nhau nếu ước số chung lớn nhất của a và b bằng 1.
# Cho số nguyên dương N không quá 9 chữ số. 
# Hãy kiểm tra xem N và số đảo của N có phải là một cặp số nguyên tố cùng nhau hay không.

# Input
# Dòng đầu ghi số bộ test, không quá 20.
# Mỗi bộ test ghi trên một dòng số nguyên dương N, không quá 9 chữ số.

# Output
# Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ

# Input   Output
# 2
# 123     NO
# 997     YES

def check(a, b):
    a, b = int(a), int(b)
    while b != 0:
        x = a % b
        a = b
        b = x
    if a == 1:
        return 'YES'
    else:
        return 'NO'


for t in range(int(input())):
    n = input()
    print(check(n, n[::-1]))

