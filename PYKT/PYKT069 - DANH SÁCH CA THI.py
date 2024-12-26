# Học viện Hoàng gia tổ chức thi thời kỳ giãn cách theo các hình thức thi linh hoạt, phù hợp với từng môn học.
# Mỗi ca thi gồm các thông tin:
#     Mã ca thi: tự động tăng, tính từ C001
#     Ngày thi: đúng định dạng dd/mm/yyyy
#     Giờ thi: theo đúng định dạng hh:mm
#     Phòng thi: một dãy chữ số đại diện cho ID phòng online, không quá 12 chữ số
# Hãy nhập danh sách các ca thi và sắp xếp theo thời gian thi (từ sớm nhất đến muộn nhất). Nếu hai ca thi cùng giờ thì sắp xếp theo mã ca thi tăng dần.

# Input: file văn bản CATHI.in
#     Dòng đầu ghi số ca thi. Mỗi ca thi ghi trên 3 dòng gồm Ngày, Giờ và ID phòng thi.
# Output
#     Ghi ra danh sách các ca thi theo thứ tự thời gian, nếu cùng giờ thì sắp xếp theo mã ca thi.
# Ví dụ
#     Input           Output
#     2
#     09/01/2022      C002 09/01/2022 10:00 70279
#     15:30
#     70172
#     09/01/2022      C001 09/01/2022 15:30 70172
#     10:00
#     70279

from datetime import datetime
class ca:
    def __init__(self, i, date, time, room) -> None:
        self.code = 'C' + str(i).zfill(3)
        self.date = date
        self.time = time
        self.room = room
        self.dtime = datetime.strptime(date + ' ' + time, '%d/%m/%Y %H:%M')
    def __str__(self) -> str:
        return self.code + ' ' + self.date + ' ' + self.time + ' ' + self.room
a = []
f = open('CATHI.in', 'r')
for i in range(int(f.readline())): a.append(ca(i+1, f.readline().strip(), f.readline().strip(), f.readline().strip()))
a.sort(key=lambda x: (x.dtime, x.code))
for i in a: print(i)
