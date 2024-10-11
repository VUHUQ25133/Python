# Khai báo lớp Matrix mô tả ma trận các số nguyên với các thuộc tính là kích thước ma trận và mảng hai chiều lưu các phần tử.
# Nhập ma trận a cấp n*m. Hãy viết chương trình tính tích của a với ma trận chuyển vị của a.    
# Input: Dòng đầu tiên ghi số bộ test.
#     Với mỗi bộ test:
#     Dòng đầu tiên ghi hai số n và m là bậc của ma trân a;
#     n dòng tiếp theo, mỗi dòng ghi m  số của một dòng trong ma trận. 
#     n và m đều nguyên dương và nhỏ hơn 50. Các giá trị trong ma trận không vượt quá 100. 
# Output: Với mỗi bộ test ghi ra ma trận tích tương ứng, mỗi số cách nhau đúng một khoảng trống. 
# Ví dụ
# Input
# 1
# 2  2
# 1  2
# 3  4
# Output
# 5 11
# 11 25

class Matrix:

    def __init__(self, n, m, mt):
        self.n = n
        self.m = m
        self.mt = mt

    def __mul__(self):
        res = []
        for i in range(self.n):
            res += [[0] * self.n]
            for j in range(self.n):
                for k in range(self.m):
                    res[i][j] += self.mt[i][k] * self.mt[j][k]
        return Matrix(self.n, self.m, res)

    def __str__(self):
        for i in self.mt:
            print(*i)
        return ''


for t in range(int(input())):
    n, m = [int(i) for i in input().split()]
    mt = []
    for i in range(n):
        mt.append([int(j) for j in input().split()])
    matrix = Matrix(n, m, mt)
    print(matrix.__mul__())
