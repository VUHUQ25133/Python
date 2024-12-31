# Trên hệ thống phim của một website có các thông tin bộ phim bao gồm Mã phim, Tên phim, Ngày khởi chiếu, Số tập phim, Thể loại. 
# Mã phim được đánh số tự động từ P001, P002 và tự động tăng dần. 
# Thể loại phim bao gồm thông tin Mã thể loại và Tên thể loại. 
# Mã thể loại được đanh số tự động tăng dần từ TL001, TL002
# Cho danh sách các phim trên hệ thống, hãy thực hiện sắp xếp danh sách các bộ phim theo thứ tự 
# ưu tiên ngày khởi chiếu tăng dần, tên phim sắp xếp theo thứ tự từ điển, số tập phim giảm dần.
# Input:
#     Dòng đầu tiên cho 2 số N, M lần lượt là số lượng thể loại và số lượng bộ phim.
#     N dòng tiếp theo là thông tin tên thể loại. Mã thể loại tự động sinh theo thứ tự nhập vào
#     M dòng còn lại mỗi dòng là thông tin phim bao gồm Mã thể loại, ngày khởi chiếu (dd/mm/yyyy) tên phim và số tập phim (số nguyên tối đa 10000).
# Output:
#     Danh sách phim đã sắp xếp như mẫu, mỗi phim trên một dòng

# Ví dụ:
# Input           Output
# 2 3             P001 Hai huoc 25/11/2021 Phim so 1 10
# Hai huoc        P003 Tinh cam 25/11/2021 Phim so 3 5
# Tinh cam        P002 Hai huoc 04/12/2021 Phim so 2 15
# TL001
# 25/11/2021
# Phim so 1
# 10
# TL001
# 04/12/2021
# Phim so 2
# 15
# TL002
# 25/11/2021
# Phim so 3
# 5

class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Film:
    def __init__(self, id, category, date, name, count):
        self.id = id
        self.category = category
        self.date = date
        self.day = int(date[0:2])
        self.month = int(date[3:5])
        self.year = int(date[6:])
        self.name = name
        self.count = count

    def __str__(self):
        return '{} {} {} {} {}'.format(self.id, self.category.name, self.date, self.name, self.count)


n, m = [int(i) for i in input().split()]
cates = []
films = []

for i in range(n):
    cates.append(Category('TL{:03}'.format(i + 1), input()))

for i in range(m):
    tl = input()
    for category in cates:
        if tl == category.id:
            films.append(Film('P{:03}'.format(i + 1),
                         category, input(), input(), int(input())))

films.sort(key=lambda e: (e.year, e.month, e.day, e.name, -e.count))
print(*films, sep='\n')
