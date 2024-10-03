# Cho dãy số A[] có N phần tử. 
# Hãy liệt kê tất cả các tổ hợp chập K của tập các phần tử khác nhau trong A[]. 
# Các tổ hợp cần liệt kê theo thứ tự từ điển

# Input
# Dòng đầu ghi hai số N và K.
# Dòng thứ 2 ghi N số của mảng A[]. Các giá trị không quá 1000.
# Dữ liệu đảm bảo số phần tử khác nhau của A[] không quá 20 và K không quá 10.

# Output
# Ghi ra lần lượt các tổ hợp tìm được, mỗi tổ hợp trên một dòng.

# Ví dụ

# Input
# 8 3
# 2 4 4 3 5 1 3 4
# Output
# 1 2 3
# 1 2 4
# 1 2 5
# 1 3 4
# 1 3 5
# 1 4 5
# 2 3 4
# 2 3 5
# 2 4 5
# 3 4 5

def Try(i, l):
    global n, k
    if len(l) == k:
        print(*l)
        return
    for j in range(i, n):
        Try(j + 1, l + [list[j]])


n, k = [int(i) for i in input().split()]
list = sorted(list({int(i) for i in input().split()}))
n = len(list)


Try(0, [])