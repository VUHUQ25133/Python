# Theo quy định mới, điểm tuyển sinh vào trường đại học XYZ
# sau khi tính tổng sẽ được cộng ưu tiên:
#     Thí sinh khu vực 1 ưu tiên 1.5 điểm
#     Thí sinh khu vực 2 ưu tiên 1 điểm
#     Thí sinh khu vực 3 không ưu tiên
#     Thí sinh dân tộc Kinh không ưu tiên
#     Thí sinh các dân tộc khác ưu tiên 1.5 điểm
# Hãy tính tổng điểm đã ưu tiên và xác định tình trạng trúng tuyển. 
# Biết điểm chuẩn của trường năm nay là 20.5 điểm.
# Input
#     Dòng đầu ghi số thí sinh.
#     Mỗi thí sinh ghi trên 4 dòng gồm:
#         Họ tên: có thể chưa chuẩn hóa
#         Điểm thi: giá trị số thực không quá 30
#         Dân tộc
#         Khu vực
# Output
#     Ghi ra danh sách đã sắp xếp theo tổng điểm (đã tính ưu tiên) giảm dần, 
#     nếu tổng điểm bằng nhau thì sắp xếp theo mã thí sinh tăng dần. 
#     Các thông tin cần liệt kê gồm:
#         Mã thí sinh (tính theo thứ tự nhập từ TS01)
#         Họ tên đã chuẩn hóa
#         Tổng điểm với đúng 1 chữ số phần thập phân
#         Trạng thái: Do hoặc Truot

#     Input                   Output
#     2                       TS01 Nguyen Hong Ngat 23.5 Do
#     Nguyen  hong ngat       TS02 Chu Thi Minh 15.5 Truot
#     22
#     Kinh
#     1
#     Chu thi MINh
#     14
#     Dao
#     3

def dt(s):
    if s.lower()=='kinh': return 0
    return 1.5
def sup(s):
    if s=='1': return 1.5
    if s=='2': return 1
    return 0
def cleanName(s):
    return ' '.join([(x[0].upper() + x[1:].lower()) for x in s.split()])
class ob:
    def __init__(self, i, name, sum, p, kv) -> None:
        self.code = f'TS{str(i).zfill(2)}'
        self.name = cleanName(name)
        self.sum = sum + sup(kv) + dt(p)
        if self.sum >= 20.5: self.type = 'Do'
        else: self.type = 'Truot'
    def __str__(self) -> str:
        return self.code + ' ' + self.name + ' ' + f'{self.sum:.1f}' + ' ' + self.type
a = []
for i in range(int(input())): a.append(ob(i+1, input(), float(input()), input(), input()))
for i in sorted(a, key=lambda x: -x.sum): print(i)
