# Chúng ta đều biết chỉ có 4 chữ số nguyên tố là 2, 3, 5, 7. 
# Hãy liệt kê tất cả các số có ít nhất 4 chữ số nhưng không quá N chữ số và thỏa mãn tất cả các điều kiện sau:
# Chỉ có các chữ số 2, 3, 5, 7
# Có đầy đủ 4 chữ số 2, 3, 5, 7
# Không phải là số chẵn.
# Input
# Chỉ có 1 dòng ghi số N (3 < N < 10)
# Output
# Ghi ra lần lượt các số thỏa mãn theo thứ tự tăng dần, mỗi số trên một dòng
# Ví dụ
# Input
# 4
# Output
# 2357
# 2375
# 2537
# 2573
# 2735
# 2753
# 3257
# 3275
# 3527
# 3725
# 5237
# 5273
# 5327
# 5723
# 7235
# 7253
# 7325
# 7523

n = 0
b = ['2', '3', '5', '7']
c = []

def check(s) :
    if s[-1] == '2' : return False
    check = [0] * 4
    for i in s :
        for j in range(4) :
            if i == b[j] : check[j] = 1
    if sum(check) == 4 : return True
    return False

def Try(k, s) :
    if k >= 4 :
        if check(s) : c.append(s)
    if k == n :
        return
    for i in range(4) :
        Try(k+1, s+b[i])

n = int(input())
Try(0, '')
c = sorted(c, key = lambda x : len(x))
for i in c :
    print(i)