# Mỗi team thi lập trình ICPC có 3 sinh viên đến từ cùng một trường đại học.
# Thông tin về một team gồm:
#     Mã team (tự động tăng, tính từ Team01)
#     Tên team: không quá 50 ký tự
#     Tên trường: không quá 150 ký tự
# Thông tin mỗi thí sinh gồm:
#     Mã thí sinh (tự động tăng, tính từ C001)
#     Họ và tên: không quá 50 ký tự.
#     Mã team
# Hãy nhập và in ra danh sách thí sinh thi lập trình được sắp xếp theo họ tên (thứ tự từ điển).

# Input
#     Dòng đầu ghi số team. Mỗi team ghi trên 2 dòng gồm tên team và tên trường.
#     Tiếp theo là một dòng ghi số thí sinh. Mỗi thí sinh ghi trên 2 dòng gồm họ tên và mã team.
# Output
#     Ghi ra danh sách đã sắp xếp theo họ tên thí sinh (thứ tự từ điển) gồm các thông tin:
#         Mã thí sinh
#         Họ và tên thí sinh
#         Tên team
#         Tên trường

# Input                               Output
#   2                                   C003 Giang Minh Tung BAV_MIS Banking Academy of Vietnam
#   BAV_MIS                             C001 Le Trung Toan BAV_MIS Banking Academy of Vietnam
#   Banking Academy of Vietnam          C004 Nguyen Hang Giang FTU Knights1 Foreign Trade University
#   FTU Knights1                        C005 Nguyen Thanh Nhan FTU Knights1 Foreign Trade University
#   Foreign Trade University            C002 Nguyen Trinh Quoc Long BAV_MIS Banking Academy of Vietnam
#   6                                   C006 Nguyen Viet Duc FTU Knights1 Foreign Trade University
#   Le Trung Toan
#   Team01
#   Nguyen Trinh Quoc Long
#   Team01
#   Giang Minh Tung
#   Team01
#   Nguyen Hang Giang
#   Team02
#   Nguyen Thanh Nhan
#   Team02
#   Nguyen Viet Duc
#   Team02

def cleanName(s):
    return ' '.join([(x[0].upper() + x[1:].lower()) for x in s.split()])
class ob:
    def __init__(self, i, name, school) -> None:
        self.code = f'Team{str(i).zfill(2)}'
        self.name = name
        self.school = school
class ob2:
    def __init__(self, i, name, o) -> None:
        self.code = f'C{str(i).zfill(3)}'
        self.name = name
        self.o = o
    def __str__(self) -> str:
        return self.code + '  ' + self.name + ' ' + self.o.name + ' ' + self.o.school
team = {}
for i in range(int(input())):
    o = ob(i+1, input(), input())
    team[o.code] = o
a = []
for i in range(int(input())): a.append(ob2(i+1, input(), team[input()]))
for i in sorted(a, key=lambda x: x.name): print(i)
