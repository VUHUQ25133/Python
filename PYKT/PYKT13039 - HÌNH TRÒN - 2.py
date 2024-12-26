# Bắt đầu từ một hình tròn lớn nội tiếp tam giác vuông,
# người ta thử vẽ thêm các hình tròn nhỏ hơn tiếp xúc với cạnh huyền, 
# cạnh góc vuông của tam giác và tiếp xúc với đường tròn lớn ban đầu.

# Tiếp tục theo cách như vậy người ta có thể vẽ vô hạn hình tròn nhỏ hơn nữa. 
# Khi số lượng hình tròn đã rất lớn (tiến đến vô hạn), người ta muốn tính xem 
#     diện tích được bao phủ bởi các hình tròn bằng bao nhiêu phần diện tích của tam giác vuông.
# Input
#     Chỉ có một dòng ghi hai cạnh góc vuông của tam giác vuông (là hai số nguyên dương khác nhau, không quá 105).
# Output
#     Ghi ra tỉ lệ diện tích của tất cả các hình tròn trên diện tích tam giác (tính chính xác đến 4 số sau dấu phẩy).
# Ví dụ
#     Input           Output
#     3 4             0.7171

#     12 16           0.7171

from math import sqrt, pow, pi
a, b = map(float, input().split())
c = sqrt(a*a+b*b)
r = (a+b-c)/2
x = sqrt(pow(b-r,2) + r*r)
k = (x-r)/(x+r)
p = 2*pi*pow(r,2)/(1-pow(k,2))/a/b
print(f'{p:.4f}')