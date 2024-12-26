# Hệ thống máy tính mới chuyển sang sử dụng hệ đếm tam phân với ba chữ số 0, 1, 2.
# Do vốn đã quen với hệ đếm nhị phân nên Nam chỉ quan tâm đến các số tam phân thỏa mãn chữ số 2 chiếm ưu thế, 
# tức là số lượng chữ số 2 chiếm nhiều hơn 50% số chữ số của số đó.
# Hãy giúp Nam liệt kê N số tam phân mà số 2 chiếm ưu thế đầu tiên (theo thứ tự từ nhỏ đến lớn).
# Input
# Dòng đầu ghi số bộ test (không quá 20)
# Mỗi bộ test ghi số nguyên dương N (không quá 1000)
# Output
# Với mỗi test, viết trên một dòng N số tam phân ưu thế 2, các số cách nhau một khoảng trống.
# Ví dụ
# Input           Output
# 2
# 5               2 22 122 202 212
# 10              2 22 122 202 212 220 221 222 1222 2022

a = []
b = ['0', '1', '2']
def check(s) :
    d = 0
    for i in s:
        if i == '2' : d += 1
    if d > len(s) / 2: return 1
    return 0

def gen(s) :
    if check(s) : a.append(s)
    if len(s) < 10 :
        for i in b :
            gen(s + i)
            
gen('1')
gen('2')
a = sorted([int(x) for x in a])
t = int(input())
for k in range(t) :
    n = int(input())
    for i in range(n) : print(a[i], end = ' ')
    print()

