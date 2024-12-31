# Học viện Hoàng gia tổ chức thi thời kỳ giãn cách theo các hình thức thi linh hoạt, phù hợp với từng môn học.
# Thông tin về mỗi môn học gồm:
#     Mã môn: xâu ký tự không có khoảng trống, không quá 15 ký tự
#     Tên môn: xâu ký tự không có thể có  khoảng trống, không quá 100 ký tự
#     Hình thức thi: xâu ký tự không có thể có  khoảng trống, không quá 100 ký tự
# Mỗi ca thi gồm các thông tin:
#     Mã ca thi: tự động tăng, tính từ C001
#     Ngày thi: đúng định dạng dd/mm/yyyy
#     Giờ thi: theo đúng định dạng hh:mm
#     Phòng thi: một dãy chữ số đại diện cho ID phòng online, không quá 12 chữ số
# Lịch thi được xây dựng dựa trên mã môn và mã ca thi và mã nhóm lớp. 
# Theo quy định, nhóm lớp đơn giản là các giá trị chữ số, bắt đầu từ 01 và không quá 99. 
# Mỗi nhóm sẽ có số sinh viên tham gia ca thi đó.

# Hãy nhập lịch thi và sắp xếp lại theo thứ tự thời gian. Nếu cùng giờ thì sắp theo mã ca thi (thứ tự từ điển).

# Input: gồm 3 file văn bản.
#     MONTHI.in: Dòng đầu ghi số môn học. Mỗi môn ghi trên 3 dòng lần lượt là mã môn, tên môn, hình thức thi.
#     CATHI.in: Dòng đầu ghi số ca thi. Mỗi ca thi ghi trên 3 dòng gồm Ngày, Giờ và ID phòng thi.
#     LICHTHI.in: Dòng đầu ghi số lượng các dòng trong lịch thi.
# Mỗi dòng tiếp theo ghi 4 thông tin: mã ca thi, mã môn, mã nhóm, số sinh viên. Mỗi thông tin cách nhau một khoảng trống.

# Output: Ghi ra danh sách lịch thi đã sắp xếp theo yêu cầu, các thông tin cần liệt kê gồm:
#     Ngày thi
#     Giờ thi
#     ID Phòng thi
#     Tên môn
#     Nhóm
#     Số sinh viên
# Các thông tin liệt kê cách nhau đúng một khoảng trống

# Ví dụ
# Input
# MONTHI.in
#     2
#     MUL1320
#     Nhap mon da phuong tien
#     Bai tap lon + Van dap truc tuyen
#     BAS1203
#     Giai tich 1
#     Thi viet + Van dap truc tuyen
# CATHI.in
#     2
#     09/01/2022
#     15:30
#     70172
#     09/01/2022
#     10:00
#     70279
# LICHTHI.in
#     2
#     C001 MUL1320 01 46
#     C002 BAS1203 04 72
# Output
#     09/01/2022 10:00 70279 Giai tich 1 04 72
#     09/01/2022 15:30 70172 Nhap mon da phuong tien 01 46

from datetime import datetime
class MT:
    def __init__(self, code, name, method) -> None:
        self.code = code 
        self.name = name 
        self.method = method 
class CA:
    def __init__(self, i, date, time, room) -> None:
        self.code = 'C' + str(i).zfill(3)
        self.strdate = date
        self.strtime = time
        self.date = datetime.strptime(date + ' ' + time, '%d/%m/%Y %H:%M')
        self.room = room
class SCHE:
    def __init__(self, ca: CA, mt: MT, group, num) -> None:
        self.ca = ca
        self.mt = mt
        self.group = group
        self.num = num
    def __str__(self) -> str:
        return f'{self.ca.strdate} {self.ca.strtime} {self.ca.room} {self.mt.name} {self.group} {self.num}'
fmt = open('MONTHI.in')
fca = open('CATHI.in')
fsche = open('LICHTHI.in')
mmth, mca = {}, {}
n = int(fmt.readline().strip())
for i in range(n):
    x = MT(fmt.readline().strip(), fmt.readline().strip(), fmt.readline().strip())
    mmth[x.code] = x
m = int(fca.readline().strip())
for i in range(m):
    x = CA(i+1, fca.readline().strip(), fca.readline().strip(), fca.readline().strip())
    mca[x.code] = x
a = []
k = int(fsche.readline().strip())
for i in range(k):
    arr = fsche.readline().strip().split()
    x = SCHE(mca[arr[0]], mmth[arr[1]], arr[2], arr[3])
    a.append(x)
for i in sorted(a, key=lambda x: (x.ca.date, x.ca.code)): print(i)
