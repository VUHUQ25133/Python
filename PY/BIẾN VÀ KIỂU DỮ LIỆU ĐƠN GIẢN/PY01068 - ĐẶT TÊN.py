# Hãy liệt kê tất cả danh sách các tổ hợp K cái tên khác nhau có thể được tạo ra theo thứ tự từ điển.
# Input
# Dòng đầu ghi 2 số N và K.
# Tiếp theo là 1 dòng ghi N cái tên, mỗi cái tên có độ dài không quá 15 và cách nhau một khoảng trống. 
# Tất cả đều là ký tự in hoa.

# Output
# Ghi ra tất cả các tổ hợp tên có thể được lựa chọn theo thứ tự từ điển.
# Tức là các tên trong mỗi tổ hợp liệt kê theo thứ tự từ điển 
# và các tổ hợp cũng được liệt kê theo thứ tự từ điển.

# Ví dụ

# Input
# 6 2
# DONG TAY NAM BAC TAY BAC

# Output
# BAC DONG
# BAC NAM
# BAC TAY
# DONG NAM
# DONG TAY
# NAM TAY

n, k = [int(x) for x in input().split()]
m = {}
a = input().split()
for i in a : m[i] = 1
a, d = [''], [0]
for i in sorted(list(m)) :
    d.append(len(a))
    a.append(i)
n = len(a) - 1
while True :
    ok = 0
    for i in range(k) :
        print(a[d[i + 1]], end = ' ')
    print()
    for i in range(k, 0, -1) :
        if d[i] != n - k + i :
            ok = 1
            d[i] += 1
            for j in range(i + 1, k + 1) : d[j] = d[j - 1] + 1
            break
    if ok == 0 : break