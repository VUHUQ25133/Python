# Khai báo lớp Phân số gồm hai thuộc tính tử số và mẫu số. Các giá trị đều nguyên dương và không quá 18 chữ số.
# nhập vào hai phân số p và q. Tính tổng p + q, rút gọn và in ra kết quả.
# Input
# Có bốn số nguyên dương lần lượt là tử số và mẫu số của p rồi đến q.
# Output
# Ghi ra phân số tổng p + q ở dạng tối giản như trong ví dụ
# Ví dụ

# Input
# 123 456 12 34
# Output
# 1609/2584

from math import gcd

class PhanSo:

    def __init__(self, tu=None, mau=None):
        self.tu = tu
        self.mau = mau

    def __add__(self, other):
        c = PhanSo()
        c.mau = self.mau * other.mau
        c.tu = self.tu * other.mau + self.mau * other.tu
        c.rut_gon()
        return c

    def __str__(self):
        return f'{self.tu}/{self.mau}'

    def rut_gon(self):
        g = gcd(self.tu, self.mau)
        self.tu //= g
        self.mau //= g


list = [int(i) for i in input().split()]
a = PhanSo(list[0], list[1])
b = PhanSo(list[2], list[3])
c = a + b
print(c)
