# Khai báo lớp Point (điểm trong không gian hai chiều) với hai thuộc tính là tọa độ x và tọa độ y (số thực).
# nhập vào hai điểm p1, p2 và tính khoảng cách hai điểm đó. 
# Input
#     Dòng đầu ghi số bộ test, không quá 20.
#     Mỗi bộ test có 4 số thực lần lượt là tọa độ của 2 điểm A và B, giá trị tuyệt đối không quá 1000.            
# Output
#     Với mỗi bộ test, viết ra khoảng cách giữa 2 điểm với 4 chữ số phần thập phân. 
# Ví dụ
# Input           Output
# 2
# 0 0 0 5         5.0000
# 0 199 5 6       193.0648

# Bài tập này yêu cầu sử dụng hàm main cho sẵn như sau:
# ```
# if __name__ == '__main__':
#     t = int(input())
#     while t > 0:
#         arr = input().split()
#         p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
#         p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
#         print(p1.distance(p2))
#         t -= 1
# ```

from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return '{:.4f}'.format(sqrt((pow(self.x - other.x, 2) + pow(self.y - other.y, 2))))

def Decimal(x):
    return float(x)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
