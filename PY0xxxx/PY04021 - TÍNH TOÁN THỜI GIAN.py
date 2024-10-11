# Quán Game mùa này vắng khách nên chủ quán quyết định tính tiền chi tiết đến từng phút. 
# Dựa trên dữ liệu giờ vào và giờ ra, hãy tính thời gian chơi game của các Game thủ nhé.
# Input
# Dòng đầu của dữ liệu vào ghi số lượng game thủ trong ngày (không quá 20).
# Thông tin về một game thủ đến chơi game được ghi lại trên 4 dòng lần lượt là:
#     Mã người chơi (xâu ký tự độ dài không quá 10, không có khoảng trống)
#     Tên người chơi (xâu ký tự độ dài không quá 100, có thể có khoảng trống).
#     Giờ vào (định dạng hh:mm)
#     Giờ ra (định dạng hh:mm)
# Output
# Ghi ra danh sách game thủ đã được sắp xếp theo thời gian chơi game giảm dần.
# Ví dụ
# Input               Output
# 3                   06T  Hoang Van Nam 2 gio 30 phut
# 01T                 01T  Nguyen Van An 1 gio 30 phut
# Nguyen Van An       02I  Tran Hoa Binh 0 gio 55 phut
# 09:00
# 10:30
# 06T
# Hoang Van Nam
# 15:30
# 18:00
# 02I
# Tran Hoa Binh
# 09:05
# 10:00

class Gamer:
    def __init__(self, id, name, timeIn, timeOut):
        self.id = id
        self.name = name
        self.timeIn = timeIn
        self.timeOut = timeOut
        self.calculateTime()

    def calculateTime(self):
        i = int(self.timeIn[0:2]) * 60 + int(self.timeIn[3:])
        o = int(self.timeOut[0:2]) * 60 + int(self.timeOut[3:])
        self.time = o - i

    def timeStr(self):
        return '{} gio {} phut'.format(self.time // 60, self.time % 60)

    def __str__(self):
        return '{} {} {}'.format(self.id, self.name, self.timeStr())


list = []
for i in range(int(input())):
    list.append(Gamer(input(), input(), input(), input()))

list.sort(key=lambda e: (-e.time))
print(*list, sep='\n')
