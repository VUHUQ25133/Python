# Với 8 hình tròn có kích thước bằng nhau, người ta có thể xếp 8 hình tròn này vào một hình vuông.
# Bài toán đặt ra là cho trước kích thước hình vuông, hãy tính độ dài bán kích lớn nhất có thể của 8 hình tròn bằng nhau có thể xếp vào hình vuông đó.
# Input
#     Chỉ có một số thực với 4 số phần thập phân cho biết diện tích hình vuông ban đầu.
# Output
#     Ghi ra độ dài bán kính lớn nhất có thể của hình tròn, tính chính xác đến 4 số sau dấu phẩy.
# Ví dụ
#     Input           Output
#     0.3438          0.1000

#     1.3753          0.2000

from math import sqrt
print (f'{ (sqrt (float (input())) * (1 + sqrt(2) - sqrt(3)) / 4) :.4f}')