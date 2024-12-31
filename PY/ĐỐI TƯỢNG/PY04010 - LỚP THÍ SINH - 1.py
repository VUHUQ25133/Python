# Viết chương trình khai báo lớp Thí Sinh gồm các thông tin: Họ tên, Ngày sinh, Điểm môn 1, Điểm môn 2, Điểm môn 3 và Tổng điểm.
# Đọc thông tin 1 thí sinh từ bàn phím và in ra màn hình 3 thông tin: Họ tên, Ngày sinh, Tổng điểm.
# Input
# Gồm 5 dòng lần lượt, mỗi dòng ghi 1 thông tin: Họ tên, Ngày sinh, Điểm môn 1, Điểm môn 2, Điểm môn 3. 
# Họ tên không quá 50 chữ cái, Ngày sinh viết đúng chuẩn dd/mm/yyyy. Các giá trị điểm là số thực (float).
# Output
# Ghi ra Họ tên, Ngày sinh và Tổng điểm. Mỗi thông tin cách nhau một khoảng trống. Điểm được ghi ra với 1 số sau dấu phẩy.
# Ví dụ
# Input
# Nguyen Hoang Ha
# 11/10/2001
# 4.5
# 10.0
# 5.5
# Output
# Nguyen Hoang Ha 11/10/2001 20.0

class Student:

    def __init__(self, name, dob, marks):
        self.name = name
        self.dob = dob
        self.score = sum(marks)

    def __str__(self):
        return f'{self.name} {self.dob} {self.score}'


name = input()
dob = input()
marks = [float(input()), float(input()), float(input())]
print(Student(name, dob, marks))
