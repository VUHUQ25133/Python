# Để thuận lợi trong quá trình lưu trữ và sử dụng, người ta đã chuyển toàn bộ thông tin từ sổ tay lên lưu trữ trên điện thoại.
# Dữ liệu trên điện thoại khi hiển thị đã được sắp xếp theo tên liên lạc. 
# Lưu ý, nếu tên trùng nhau thì sắp xếp theo họ đệm.
# Cho thông tin danh sách liên lạc được ghi chép như mẫu từ tập tin SOTAY.txt, hãy đưa ra dữ liệu hiển thị trên điện thoại vào tập tin DIENTHOAI.txt

# Input: Lịch sử ghi chép theo ngày, mỗi ngày có thể ghi chép nhiều thông tin liên lạc. 
# Họ tên tối đa 100 ký tự, số điện thoại có 10 chữ số.

# Ví dụ:
# SOTAY.txt
#     Ngay 15/1`1/2021
#     Nguyen Van A
#     0914141581
#     Nguyen Van B
#     0921241515
#     Ngay 16/11/2021
#     Tran Van C
#     093514114`1

# DIENTHOAI.txt
#     Nguyen Van A: 0914141581 15/11/2021
#     Nguyen Van B: 0921241515 15/11/2021
#     Tran Van C: 0935141141 16/11/2021

from sys import stdin
def cleanName(name: str):
    a = name.lower().split()
    for i in range(len(a)): a[i] = a[i][0].upper() + a[i][1:].lower()
    return ' '.join(a)
class info:
    def __init__(self, day, name, sdt) -> None:
        self.day = day
        a = name.split()
        self.first = a[-1]
        self.mid = a[:-1]
        self.name = name
        self.sdt = sdt
    def __str__(self) -> str:
        return self.name + ': ' + self.sdt + ' ' + self.day
try: fr = open('SOTAY.txt', 'r')
except: fr = stdin
lines = [x.strip() for x in fr if x.strip() != '']
a = []
day = lines[0].split()[1]
i = 1
while i<len(lines): 
    s1 = lines[i]
    i+=1
    if s1.count('/') > 0:
        day = s1.split()[1]
        continue
    s2 = lines[i]
    i+=1
    a.append(info(day, cleanName(s1), s2))
for i in sorted(a, key=lambda x: (x.first, x.mid)): print(i)
