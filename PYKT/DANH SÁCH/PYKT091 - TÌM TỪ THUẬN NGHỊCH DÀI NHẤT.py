# Cho dữ liệu vào dạng file văn bản.
# Hãy tìm ra từ thỏa mãn tính chất thuận nghịch và có độ dài lớn nhất trong file đó. 
# Đếm xem từ đó xuất hiện bao nhiêu lần.
# Nếu có nhiều từ cùng có độ dài lớn nhất thì in ra tất cả các từ đó theo thứ tự xuất hiện trong file ban đầu.

# Input:  File văn bản VANBAN.in Không quá 1000 từ.
# Output: Ghi ra trên màn hình một dòng từ thuận nghịch có độ dài lớn nhất và số lần xuất hiện của nó. 
#         Nếu có nhiều từ cùng có độ dài lớn nhất thì các từ được liệt kê theo thứ tự xuất hiện ban đầu.

#     VANBAN.in                                   Output
#     AAA BAABA HDHDH ACBSD SRGTDH DDDDS          HDHDH 3
#     DUAHD AAA AD DA HDHDH AAA AAA AAA AAA
#     DDDAS HDHDH HDH AAA AAA AAA AAA AAA
#     AAA AAA AAA
#     DHKFKH DHDHDD HDHDHD DDDHHH HHHDDD
#     TDTD

f = open('VANBAN.in', 'r')
class pair:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def len(self): return len(self.s)
def check(s):
    for i in range(len(s)>>1):
        if s[i] != s[len(s)-1-i]: return False
    return True
a = f.read().split()
m = {}
for i in range(len(a)):
    if check(a[i]):
        if m.get(a[i]) is None:
            x = pair(1, i)
            m[a[i]] = x
        else: m[a[i]].x += 1
a = sorted(m, key=lambda x: (-len(x), m[x].y))
for i in a: 
    if len(i) == len(a[0]): print(i, m[i].x)
