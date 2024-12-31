# Học viện Hoàng gia tổ chức thi thời kỳ giãn cách theo các hình thức thi linh hoạt, phù hợp với từng môn học.
# Thông tin về mỗi môn học gồm:
#     Mã môn: xâu ký tự không có khoảng trống, không quá 15 ký tự
#     Tên môn: xâu ký tự không có thể có  khoảng trống, không quá 100 ký tự
#     Hình thức thi: xâu ký tự không có thể có  khoảng trống, không quá 100 ký tự
# Hãy nhập danh sách và in danh sách sắp xếp theo mã môn.
# Input
#     Dòng đầu ghi số môn học. Mỗi môn ghi trên 3 dòng lần lượt là mã môn, tên môn, hình thức thi.
# Output
#     Ghi ra danh sách đã sắp xếp theo mã môn, thứ tự từ điển.
# Ví dụ
# Input                               Output
# 2
# MUL1320                             BAS1203 Giai tich 1 Thi viet + Van dap truc tuyen
# Nhap mon da phuong tien             MUL1320 Nhap mon da phuong tien Bai tap lon + Van dap truc tuyen
# Bai tap lon + Van dap truc tuyen
# BAS1203                             
# Giai tich 1
# Thi viet + Van dap truc tuyen

class Subject:
    def __init__(self, id, name, exam):
        self.id = id
        self.name = name
        self.exam = exam

    def __str__(self):
        return '{} {} {}'.format(self.id, self.name, self.exam)


list = []
for i in range(int(input())):
    list.append(Subject(input(), input(), input()))

list.sort(key=lambda e: e.id)
print(*list, sep='\n')
