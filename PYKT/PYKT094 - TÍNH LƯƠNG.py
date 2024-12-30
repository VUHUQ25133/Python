# Công ty XYZ mỗi năm đều cập nhật hồ sơ và gán lại mã cho nhân viên (đúng 5 ký tự) theo quy tắc:
#     Ký tự đầu tiên là phân loại nhân viên, có 4 nhóm là A, B, C, D
#     Hai chữ số tiếp theo mô tả số năm công tác
#     Hai ký tự cuối là mã phòng ban.
# Dựa trên loại nhân viên và số năm công tác, hệ số nhân để tính lương được cho trong bảng sau:

#         Nhóm    1-3năm      4-8năm      9-15năm     >16năm
#         A       10          12          14          20
#         B       10          11          13          16
#         C       9           10          12          14
#         D       8           9           11          13

# Mỗi nhân viên theo hợp đồng sẽ có một giá trị lương cơ bản có thể rất khác nhau. 
# Lương tháng được tính bằng tích của lương cơ bản với số ngày công và hệ số nhân.
#     Cho trước danh sách phòng ban, gồm mã phòng và tên phòng. 
#     Cho trước các thông tin nhân viên gồm mã, tên, lương cơ bản (tính theo ngày, đơn vị nghìn VNĐ) và số ngày công. 
# Hãy tính toán và in ra bảng lương nhân viên trong tháng.

# Input
#     Dòng đầu ghi số phòng ban, mỗi phòng ban viết trên một dòng gồm mã phòng và tên phòng.
#     Tiếp theo là một dòng ghi số nhân viên, mỗi nhân viên ghi trên 4 dòng gồm mã, tên, lương cơ bản (tính theo ngày), số ngày công.
# Output
#     Lập bảng lương của nhân viên theo đúng thứ tự nhập.
#     Mỗi nhân viên cần ghi ra các thông tin sau đây trên một dòng:
#         Mã nhân viên
#         Tên nhân viên
#         Phòng ban
#         Lương tháng

#  Input                           Output
#     2                               C06HC Tran Binh Minh Hanh chinh 16250000
#     HC Hanh chinh                   D03KH Le Hoa Binh Ke hoach Dau tu 11328000
#     KH Ke hoach Dau tu
#     2
#     C06HC
#     Tran Binh Minh
#     65
#     25
#     D03KH
#     Le Hoa Binh
#     59
#     24

def cleanName(s):
    return ' '.join([(x[0].upper() + x[1:].lower()) for x in s.split()])
def x(s):
    y = int(s[1:3])
    if 1<=y and y<=3:
        if s[0]=='A': return 10
        elif s[0]=='B': return 10
        elif s[0]=='C': return 9
        return 8
    elif 4<=y and y<=8:
        if s[0]=='A': return 12
        elif s[0]=='B': return 11
        elif s[0]=='C': return 10
        return 9
    elif 9<=y and y<=15:
        if s[0]=='A': return 14
        elif s[0]=='B': return 13
        elif s[0]=='C': return 12
        return 11
    else: 
        if s[0]=='A': return 20
        elif s[0]=='B': return 16
        elif s[0]=='C': return 14
        return 13
class ob:
    def __init__(self, s) -> None:
        s = s.split()
        self.code = s[0]
        self.name = ' '.join(s[1:])
class ob2:
    def __init__(self, code, name, sday, days, o) -> None:
        self.code = code
        self.name = name
        self.sum = sday*days*x(code)*10**3
        self.o = o
    def __str__(self) -> str:
        return self.code + '  ' + self.name + ' ' + self.o.name + ' ' + str(self.sum)
m = {}
for i in range(int(input())):
    o = ob(input())
    m[o.code] = o
a = []
for i in range(int(input())): 
    code = input()
    a.append(ob2(code, input(), int(input()), int(input()), m[code[3:]]))
for i in a: print(i)
