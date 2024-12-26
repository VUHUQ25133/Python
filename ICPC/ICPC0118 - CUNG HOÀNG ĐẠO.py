# Cung hoàng đạo của một người được xác định dựa trên ngày sinh bằng bảng dưới đây:

# |  Tên cung  |  Thời gian  |
# |------------|-------------|
# | Bạch Dương | 21/3 - 19/4 |
# |  Kim Ngưu  | 21/4 - 20/5 |
# |  Song Tử   | 21/5 - 20/6 |
# |  Cự Giải   | 21/6 - 22/7 |
# |   Sư Tử    | 23/7 - 22/8 |
# |   Xử Nữ    | 23/8 - 22/9 |
# | Thiên Bình | 23/9 - 22/10|
# | Thiên Yết  |23/10 - 22/11|
# |  Nhân Mã   |23/11 - 21/12|
# |   Ma Kết   | 22/12 - 19/1|
# |  Bảo Bình  | 20/1 - 18/2 |
# |  Song Ngư  | 19/2 - 20/3 |

# Nhiệm vụ của bạn là xác định cung hoàng đạo của một ngày sinh bất kỳ.
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T.
#     Những dòng kế tiếp đưa vào T bộ test. 
#     Mỗi bộ test gồm 2 số cách nhau bởi một khoảng trống d và m, trong đó d là ngày, m là tháng.
# Output:
# Đưa ra cung hoàng đạo dựa vào bảng đã cho tương ứng với ngày tháng nhập vào.

# Input       Output
# 2
# 5 5         Kim Nguu
# 30 7        Su Tu

t = int(input())
for i in range(t):
    d, m = [int(x) for x in input().split()]
    if m == 1:
        if d < 20:
            print("Ma Ket")
        else:
            print("Bao Binh")
    elif m == 2:
        if d < 19:
            print("Bao Binh")
        else:
            print("Song Ngu")
    elif m == 3:
        if d < 21:
            print("Song Ngu")
        else:
            print("Bach Duong")
    elif m == 4:
        if d < 20:
            print("Bach Duong")
        else:
            print("Kim Nguu")
    elif m == 5:
        if d < 21:
            print("Kim Nguu")
        else:
            print("Song Tu")
    elif m == 6:
        if d < 21:
            print("Song Tu")
        else:
            print("Cu Giai")
    elif m == 7:
        if d < 23:
            print("Cu Giai")
        else:
            print("Su Tu")
    elif m == 8:
        if d < 23:
            print("Su Tu")
        else:
            print("Xu Nu")
    elif m == 9:
        if d < 23:
            print("Xu Nu")
        else:
            print("Thien Binh")
    elif m == 10:
        if d < 23:
            print("Thien Binh")
        else:
            print("Thien Yet")
    elif m == 11:
        if d < 23:
            print("Thien Yet")
        else:
            print("Nhan Ma")
    else:
        if d < 22:
            print("Nhan Ma")
        else:
            print("Ma Ket")
