# Hệ cơ số 3 chỉ biểu diễn các số sử dụng ba chữ số là 0, 1, 2.
# Nhập vào dãy biểu diễn không quá 18 ký tự, 
# hãy kiểm tra xem dãy biểu diễn nào là đúng với hệ cơ số 3.

# Input
# Dòng đầu là số bộ test, mỗi dòng tiếp theo ghi một dãy biểu diễn cần kiểm tra.

# Output
# Nếu đúng in ra YES, nếu sai in ra NO.

# Ví dụ
# Input       Output
# 3
# 1214AB      NO
# 10210221    YES
# 22222222    YES

def check(s):
    for i in s:
        if s < '0' or i > '2':
            return 'NO'
    return 'YES'


for t in range(int(input())):
    print(check(input()))