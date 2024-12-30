# Hệ thống quản lý lịch thi học kỳ cho nhiều Môn học, mỗi môn học có các thông tin: Mã môn học, tên môn học
# Lịch thi học kỳ bao gồm nhiều thông tin gồm: Mã ca thi, Mã môn học, Ngày thi, Giờ thi, Nhóm thi. 
# Mã ca thi được đánh số từ T001, T002 và tự động tăng dần.

# Cho danh sách các ca thi, mỗi môn học có nhiều ca thi, 
# hãy thực hiện sắp xếp danh sách các ca thi theo thứ tự ưu tiên như sau: 
#     ngày tăng dần, giờ tăng dần, mã môn học tăng dần.
# Input:
#     Dòng đầu tiên cho 2 số N, M lần lượt là số môn học và số ca thi.
#     N * 2 dòng tiếp theo là thông tin mã môn học và tên môn học.
#     M dòng còn lại mỗi dòng là thông tin lịch thi bao gồm Mã môn học, ngày thi (dd/mm/yyyy) giờ thi (hh:mm) và nhóm thi (dạng xâu ký có 2 ký tự bất kỳ).
# Output:
#     Lịch thi đã sắp xếp như mẫu, mỗi lịch thi trên một dòng

#     Input                               Output
#     2 10                                T001 INT1155 Tin hoc co so 2 25/11/2021 08:00 01
#     INT1155                             T006 INT1339 Ngon ngu lap trinh C++ 25/11/2021 08:00 01
#     Tin hoc co so 2                     T007 INT1339 Ngon ngu lap trinh C++ 25/11/2021 08:00 02
#     INT1339                             T004 INT1155 Tin hoc co so 2 25/11/2021 13:30 04
#     Ngon ngu lap trinh C++              T005 INT1155 Tin hoc co so 2 25/11/2021 15:00 05
#     INT1155 25/11/2021 08:00 01         T002 INT1155 Tin hoc co so 2 04/12/2021 08:00 02
#     INT1155 04/12/2021 08:00 02         T003 INT1155 Tin hoc co so 2 04/12/2021 13:30 03
#     INT1155 04/12/2021 13:30 03         T008 INT1339 Ngon ngu lap trinh C++ 04/12/2021 13:30 03
#     INT1155 25/11/2021 13:30 04         T009 INT1339 Ngon ngu lap trinh C++ 04/12/2021 13:30 04
#     INT1155 25/11/2021 15:00 05         T010 INT1339 Ngon ngu lap trinh C++ 04/12/2021 15:00 05
#     INT1339 25/11/2021 08:00 01
#     INT1339 25/11/2021 08:00 02
#     INT1339 04/12/2021 13:30 03
#     INT1339 04/12/2021 13:30 04
#     INT1339 04/12/2021 15:00 05

from datetime import date, datetime
class ob:
    def __init__(self, code, name) -> None:
        self.code = code
        self.name = name
class ob2(ob):
    def __init__(self, i, o, arr) -> None:
        self.code = f'T{str(i).zfill(3)}'
        self.ocode = o.code
        self.name = o.name
        self.date = datetime.strptime(arr[1], '%d/%m/%Y')
        self.strdate = arr[1]
        self.h = datetime.strptime(arr[2], '%H:%M')
        self.strh = arr[2]
        self.group = arr[3]
    def __str__(self) -> str:
        return self.code + ' ' + self.ocode + ' ' + self.name + ' ' + self.strdate + ' ' + self.strh + ' ' + self.group
n, m = map(int, input().split())
a, arr = {}, []
for i in range(n):
    s = input()
    a[s] = ob(s, input())
for i in range(m):
    line = input().split()
    arr.append(ob2(i+1, a[line[0]], line))
for i in sorted(arr, key=lambda x: (x.date, x.h, x.ocode)): print(i)
