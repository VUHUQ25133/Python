# Tiền nước hàng tháng của thành phố ABC được tính theo đơn giá trong bảng sau:

# | Số M^3  |Đơn giá|Phụ phí|
# |---------|-------|-------|
# |Từ  0-50 |  100  |  2%   |
# |Từ 51-100|  150  |  3%   |
# |Trên 100 |  200  |  5%   |

# Trong đó, phụ phí được hiểu là số tiền tính thêm (theo phần trăm) trên tổng số tiền nước tiêu thụ.
# Cho danh sách khách hàng và chỉ số đồng hộ. Hãy sắp xếp danh sách hóa đơn theo tổng số tiền giảm dần.
# Input
# Dòng đầu ghi số khách hàng (không quá 20).
# Mỗi khách hàng viết trên 3 dòng gồm:
#     Tên khách hàng (xâu ký tự độ dài không quá 50)
#     Chỉ số cũ
#     Chỉ số mới
# Trong đó chỉ số mới lớn hơn hoặc bằng chỉ số cũ, cả hai đều không quá 4 chữ số.
# Output
# Ghi ra danh sách khách hàng đã sắp xếp theo tổng tiền giảm dần gồm các thông tin
#     Mã khách hàng (tự động gán tăng dần theo thứ tự nhập, bắt đầu từ KH01)
#     Tên khách hàng
#     Tổng số tiền (được làm tròn ở dạng số nguyên)
# Ví dụ
# Input                       Output
# 3
# Le Thi Thanh                KH03 Ha Hue Anh 34545
# 468                           
# 500
# Le Duc Cong                 KH02 Le Duc Cong 8240
# 160
# 230
# Ha Hue Anh                  KH01 Le Thi Thanh 3264
# 410
# 612

class Bill:
    def __init__(self, id, name, lastNum, currentNum):
        self.id = 'KH{:02d}'.format(id)
        self.name = name
        self.lastNum = lastNum
        self.currentNum = currentNum
        self.calculate()

    def calculate(self):
        cnt = self.currentNum - self.lastNum

        if cnt <= 50:
            self.total = cnt * 100
            self.total *= 1.02
        elif cnt <= 100:
            self.total = 50 * 100 + (cnt-50) * 150
            self.total *= 1.03
        else:
            self.total = 50 * 100 + 50 * 150 + (cnt - 100) * 200
            self.total *= 1.05

        self.total = round(self.total)

    def __str__(self):
        return '{} {} {}'.format(self.id, self.name, self.total)


list = []
for i in range(int(input())):
    name = input()
    last = int(input())
    current = int(input())
    list.append(Bill(i + 1, name, last, current))

list.sort(key=lambda e: (-e.total))
print(*list, sep='\n')

