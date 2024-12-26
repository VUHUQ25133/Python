# Trường THPT ACB tuyển giáo viên mới cho ba môn Toán, Lý, Hóa. 
# Theo yêu cầu mới, bài thi tuyển gồm 2 nội dung: Tin học và Chuyên môn. Điểm thi Tin học sẽ được nhân đôi khi tính tổng điểm.
# Mỗi GV có thể có điểm ưu tiên được xét theo mã như trong bảng sau:
                # Điểm ưu tiên:
                    # |Mã ưu tiên|Điểm|
                    # |   1      | 2.0|
                    # |   2      | 1.5|
                    # |   3      | 1.0|
                    # |   4      | 0.0|
# Mã xét tuyển gồm 2 thành phần. 
# Chữ cái đầu tiên ứng với môn học: A là Toán, B là Lý và C là Hóa; tiếp theo là 1 chữ số thể hiện mã ưu tiên.
# Tổng điểm sau khi cộng điểm ưu tiên nếu từ 18 trở lên sẽ được xét TRÚNG TUYỂN, nhỏ hơn sẽ bị LOẠI.

# Viết chương trình nhập danh sách điểm thi và sắp xếp GV theo thứ tự tổng điểm giảm dần. 
# Mã GV dự thi được tự động gán theo thứ tự bắt đầu từ 01.

# Input
#     Dòng đầu thi số giáo viên đăng ký thi tuyển (không quá 20).
#     Mỗi GV được viết trên 4 dòng gồm:
#         Tên GV (xâu ký tự độ dài không quá 50)
#         Mã xét tuyển
#         Điểm tin học (số thực trong phạm vi 0 đến 10)
#         Điểm chuyên môn (số thực trong phạm vi 0 đến 10)
# Output
#     Ghi ra danh sách đã sắp xếp.
#     Thông tin mỗi GV gồm: Mã GV, Tên, Môn học, Tổng điểm (1 chữ số phần thập phân), Kết quả. 
#     Mỗi thông tin cách nhau một khoảng trống.

# Ví dụ
    # Input                       Output
    # 3
    # Le Van Binh                 GV03 Hoang Thi Tam HOA 21.5 TRUNG TUYEN
    # A1                          GV01 Le Van Binh TOAN 19.0 TRUNG TUYEN
    # 7.0                         GV02 Tran Van Toan LY 16.0 LOAI   
    # 3.0
    # Tran Van Toan
    # B3
    # 4.0
    # 7.0
    # Hoang Thi Tam
    # C2
    # 7.0
    # 6.0

def sub(s):
    if s[0]=='A': return 'TOAN'
    if s[0]=='B': return 'LY'
    return 'HOA'
def sup(s):
    if s[1]=='1': return 2
    if s[1]=='2': return 1.5
    if s[1]=='3': return 1
    return 0
class ob:
    def __init__(self, i, name, code, t, c) -> None:
        self.code = f'GV{str(i).zfill(2)}'
        self.name = name
        self.sub = sub(code)
        self.sum = sup(code) + t*2 + c
        if self.sum >= 18: self.type = 'TRUNG TUYEN'
        else: self.type = 'LOAI'
    def __str__(self) -> str:
        return self.code + ' ' + self.name + ' ' + self.sub + ' ' + f'{self.sum:.1f}' + ' ' + self.type
a = []
for i in range(int(input())): a.append(ob(i+1, input(), input(), float(input()), float(input())))
for i in sorted(a, key=lambda x: -x.sum): print(i)