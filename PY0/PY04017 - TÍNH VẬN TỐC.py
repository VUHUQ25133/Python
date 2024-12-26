# Cuộc đua xe đạp bắt đầu từ 6h00 với độ dài quãng đường đua là 120 Km. 
# Các cua-rơ sẽ được ghi nhận thành tích dựa trên thời điểm đến đích. 
# Hãy xếp hạng theo thứ tự thành tích giảm dần.
# Input
#     Dòng đầu ghi số cua-rơ tham gia cuộc đua.
#     Mỗi cua-rơ ghi trên 3 dòng:
#         Họ tên (xâu ký tự độ dài không quá 50)
#         Đơn vị (xâu ký tự độ dài không quá 20)
#         Thời điểm đến đích theo định dạng h:mm
# Output
#     Ghi ra danh sách đã sắp xêp theo thành tích, tốt hơn xếp trước, kém hơn xếp sau.
#     Thông tin mỗi cua-rơ bao gồm:
#         Mã (là chữ cái đầu tiên của các từ trong tên đơn vị ghép với chữ cái đầu tiên các từ trong họ tên, xem ví dụ để hiểu rõ hơn)
#         Họ tên
#         Đơn vị
#         Vận tốc trung bình (đã làm tròn ra giá trị nguyên)
# Ví dụ
# Input                               Output
# 3                                   HBVNH Vu Ngoc Hoang Hoa Binh 51 Km/h
# Tran Vu Minh                        HNTVM Tran Vu Minh Ha Noi 48 Km/h
# Ha Noi                              AGPDT Pham Dinh Tan An
# 8:30
# Vu Ngoc Hoang
# Hoa Binh
# 8:20
# Pham Dinh Tan
# An Giang
# 8:45

from datetime import datetime
import math
class ob:
    def __init__(self, name, address, end) -> None:
        self.name = name
        self.address = address
        self.time = (datetime.strptime(end, '%H:%M') - datetime.strptime('6:00', '%H:%M')).seconds/3600
        self.v = 120/(self.time)
        self.code = ''
        for i in address.split(): self.code += i[0].upper()
        for i in name.split(): self.code += i[0].upper()
    def __str__(self) -> str:
        return self.code + ' ' + self.name + ' ' + self.address + ' ' + f'{round(self.v)} Km/h'
a = []
for i in range(int(input())): a.append(ob(input(), input(), input()))
for i in sorted(a, key=lambda x: x.time): print(i)