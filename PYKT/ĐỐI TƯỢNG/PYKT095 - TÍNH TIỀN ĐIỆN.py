# Các hộ gia đình trong thành phố X được chia thành 3 loại A, B, C với định mức sử dụng điện như sau:
#     Loại A: Định mức 100 kWh
#     Loại B: Định mức 500 kWh
#     Loại C: Định mức 200 kWh
# Hãy tính toán số tiền phải thanh toán theo quy tắc:
# Tính tiền trong định mức:
#     Nếu số điện (Số cuối - Số đầu) nhỏ hơn định mức thì bằng số điện * 450                 
#     Nếu số điện lớn hơn hoặc bằng định mức thì bằng định mức *450                                             
# Tiền vượt định mức                                                                                  
#     Nếu số điện lớn hơn định mức thì bằng (số điện - định mức) *1000                                      
#     Ngược lại thì bằng 0
#     Thuế VAT = 5% số tiền vượt định mức.
# Chú ý: tiền thuế VAT cũng là số nguyên dương nên có thể lấy số tiền vượt định mức chia phần nguyên cho 20.
# Số tiền phải nộp = Tiền trong định mức + Tiền vượt định mức + Thuế VAT

# Input
#     Dòng đầu ghi số khách hàng (không quá 50).
#     Mỗi khách hàng ghi trên 2 dòng:
#     Họ tên: có thể chưa chuẩn hóa
#     Loại hộ gia đình, chỉ số đầu, chỉ số cuối. Mỗi thông tin cách nhau một khoảng trống.
# Output
#     Ghi ra danh sách đã sắp xếp theo tổng số tiền phải trả giảm dần gồm các thông tin:
#         Mã khách hàng: tính từ KH01 theo thứ tự nhập
#         Họ tên đã chuẩn hóa
#         Tiền trong định mức
#         Tiền vượt định mức
#         Thuế VAT
#         Tổng số tiền phải nộp.
#     Dữ liệu đảm bảo không có hai hộ gia đình nào có cùng số tiền nộp bằng nhau.
# Ví dụ
# Input                       Output
# 2                           KH01 Nguyen Hong Ngat 35100 0 0 35100
#  nGuyEn Hong Ngat           KH02 Chu Thi Minh 18000 0 0 18000
# C 200 278
#  Chu thi    minh
# A 120 160


class Bill:
    def __init__(self, id, name, type, start, end):
        self.id = id
        self.name = name
        self.type = type
        self.start = start
        self.end = end

        self.setLimit()
        self.calculate()

    def setLimit(self):
        if type == 'A':
            self.limit = 100
        elif type == 'B':
            self.limit = 500
        elif type == 'C':
            self.limit = 200

    def calculate(self):
        if self.end - self.start < self.limit:
            self.inLimit = (self.end - self.start) * 450
            self.overLimit = 0
            self.vat = 0
        else:
            self.inLimit = self.limit * 450
            self.overLimit = (self.end - self.start - self.limit) * 1000
            self.vat = self.overLimit // 20
        self.total = self.inLimit + self.overLimit + self.vat

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.id, self.name, self.inLimit, self.overLimit, self.vat, self.total)


list = []
for i in range(int(input())):
    id = 'KH0{}'.format(i + 1)
    name = ' '.join(input().split()).title()
    arr = input().split()
    type = str(arr[0])
    start, end = int(arr[1]), int(arr[2])
    list.append(Bill(id, name, type, start, end))

list.sort(key=lambda e: -e.total)
print(*list, sep='\n')
