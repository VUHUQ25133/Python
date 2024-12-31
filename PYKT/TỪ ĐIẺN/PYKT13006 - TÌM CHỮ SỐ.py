# Hãy tìm 3 chữ số đầu tiên trước dấu phẩy của số (3+sqrt(5))^n.
#     Ví dụ:
#         Với n = 5, (3+sqrt(5))^5 = 3935.73982… Đáp số là 935.
#         Với n = 2, (3+sqrt(5))^2 = 27.4164079… Đáp số là 027.
# Input:
#     Dòng đầu tiên là số lượng bộ test T (T ≤ 100).
#     Mỗi test gồm một số nguyên n (n ≤ 2 000 000 000).
# Output: 
#     Với mỗi test in ra STT và đáp án tìm được. In ra đủ 3 chữ số như test ví dụ (n = 2, in ra 027).

# Input       Output
# 2
# 5           Case #1: 935
# 2           Case #2: 027


mod = 1000
class pair:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return f'{self.x} {self.y}'
def mul(a, b):
    r = pair(0, 0)
    r.x = (a.x*b.x + 5*a.y*b.y)%mod
    r.y = (a.x*b.y + a.y*b.x)%mod
    return r
def pow(a, b):
    if b == 0: return pair(1, 0)
    if b&1: return mul(pow(a, b-1), a)
    p = pow(a, b>>1)
    return mul(p, p)
x = pair(3, 1)
for t in range(int(input())):
    print(f'Case #{t+1}: ',end='')
    print(str(pow(x, int(input())).x*2%mod - 1).zfill(3))
