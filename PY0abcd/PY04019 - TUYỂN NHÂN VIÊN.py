# Doanh nghiệp X cần tuyển một số nhân viên mới. 
# Bài thi tuyển có hai phần: lý thuyết và thực hành. 
# Sau khi tính điểm trung bình, các thí sinh sẽ được xếp thành 4 loại:

#     Nếu điểm dưới 5 -> TRUOT
#     Nếu điểm lớn hơn hoặc bằng 5 nhưng nhỏ hơn 8 -> CAN NHAC
#     Nếu điểm từ 8 đến 9.5 -> DAT
#     Nếu điểm lớn hơn 9.5 -> XUAT SAC
# Điểm các bài thi lý thuyết và thực hành đều là số thực trong phạm vi từ 0 đến 10. 
# Tuy nhiên, khi nhập điểm các bài thi, cán bộ tuyển dụng có thể quên mất dấu '.' phân cách phần nguyên và phần thập phân. 
# Do đó nếu điểm ghi là 78 thì cần được hiểu là 7.8
# Hãy sắp xếp danh sách thí sinh đã được xếp loại theo điểm trung bình giảm dần.
# Input
# Dòng đầu ghi số thí sinh. Mỗi thí sinh ghi trên 3 dòng lần lượt là:
#     Họ và tên (xâu ký tự độ dài không quá 100)
#     Điểm lý thuyết
#     Điểm thực hành
# Mã thí sinh cần được tự động gán theo mẫu TS + số thứ tự (tính từ 01).
# Output
# Ghi ra danh sách thí sinh đã sắp xếp, mỗi thí sinh gồm 4 thông tin: mã thí sinh, họ tên, điểm trung bình (với 2 số phần thập phân) và xếp loại. Mỗi thông tin cách nhau một khoảng trống.
# Ví dụ

# Input                   Output
# 3                       TS01 Nguyen Thai Binh 6.00 CAN NHAC
# Nguyen Thai Binh        TS03 Phan Van Duc 5.60 CAN NHAC
# 45                      TS02 Le Cong Hoa 4.25 TRUOT
# 75
# Le Cong Hoa
# 4
# 4.5
# Phan Van Duc
# 56
# 56

class Staff:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score

    def getStatus(self):
        if self.score > 9.5:
            return 'XUAT SAC'
        if self.score >= 8:
            return 'DAT'
        if self.score >= 5:
            return 'CAN NHAC'
        return 'TRUOT'

    def __str__(self):
        return '{} {} {:.2f} {}'.format(self.id, self.name, self.score, self.getStatus())


list = []
for i in range(int(input())):
    id = 'TS0{}'.format(i + 1)
    name = input()
    lt, th = float(input()), float(input())
    lt /= 10 if lt > 10 else 1
    th /= 10 if th > 10 else 1
    list.append(Staff(id, name, (lt + th) / 2))


list.sort(key=lambda staff: -staff.score)
print(*list, sep='\n')
