# Nhóm sinh viên PTIT cùng nhau đăng ký 3 môn học trong Học kỳ hè năm 2021 theo đúng thứ tự:
#     Môn 1: Lập trình hướng đối tượng: 3 tín chỉ
#     Môn 2: Ngôn ngữ lập trình C++: 3 tín chỉ
#     Môn 3: Tin học cơ sở 2: 2 tín chỉ
# Người ta muốn xếp hạng thứ tự các sinh viên trong danh sách theo điểm trung bình giảm dần. 
# Biết rằng điểm trung bình tính đến 2 số phần thập phân và nếu điểm bằng nhau thì thứ hạng cũng bằng nhau.

# Input
#     Dòng đầu ghi số sinh viên (không quá 20).
#     Mỗi sinh viên ghi trên 4 dòng gồm:
#         Họ tên: có thể chưa được chuẩn hóa
#         Điểm môn 1
#         Điểm môn 2
#         Điểm môn 3
#     Các giá trị điểm là số nguyên và đảm bảo trong phạm vi từ 0 đến 10.
# Output
#     Ghi ra danh sách sinh viên đã tính điểm và sắp xếp theo xếp hạng từ cao nhất đến thấp nhất, gồm các thông tin:
#         Mã sinh viên (tự động tăng theo thứ tự nhập, tính từ SV01)
#         Họ tên đã chuẩn hóa
#         Điểm trung bình với đúng 2 số phần thập phân
#         Xếp hạng
#     Chú ý: 2 sinh viên có điểm trung bình bằng nhau thì xếp hạng bằng nhau, 
#             và nếu có 2 sinh viên hạng là X thì sinh viên tiếp theo trong danh sách có hạng X+2.
# Trong trường hợp xếp hạng bằng nhau thì cần sắp xếp theo mã sinh viên tăng dần.

# Ví dụ
# Input                           Output
# 2                               SV01 Ha Thi Kieu Anh 6.63 1
#  ha Thi kieu     anh            SV02 Pham Thi Hao 6.38 2
# 7
# 6
# 7
# Pham    THI  HAO
# 6
# 7
# 6

class Student:
    def __init__(self, id, name, score1, score2, score3):
        self.id = self.setId(id)
        self.name = self.setName(name)
        self.score = self.setScore(float(score1), float(score2), float(score3))
        self.rank = None

    def setId(self, id):
        return 'SV{0:0>2}'.format(id)

    def setName(self, name):
        name = name.lower().split()
        for i in range(len(name)):
            name[i] = name[i][0].upper() + name[i][1:]
        return ' '.join(name)

    def setScore(self, score1, score2, score3):
        return '{:.2f}'.format((score1*3 + score2*3 + score3*2)/8+0.001)

    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.name, self.score, self.rank)


n = int(input())
students = [Student(i+1, input(), input(), input(), input()) for i in range(n)]
students.sort(key=lambda ele: (-float(ele.score), ele.id))

students[0].rank = 1
for i in range(1, n):
    if students[i].score == students[i-1].score:
        students[i].rank = students[i-1].rank
    else:
        students[i].rank = i+1

print(*students, sep='\n')