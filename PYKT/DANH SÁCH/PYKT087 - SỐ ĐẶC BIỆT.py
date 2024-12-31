# Với mỗi số nguyên dương N, số M được coi là số đặc biệt của N nếu 
# M được tạo ra bằng tổng các lũy thừa không âm khác nhau của N. 
#     Ví dụ N = 4 thì M = 17 là số đặc biệt vì 17 = 40 + 42.

# Viết chương trình nhập số N và số K. 
# Sau đó in ra số đặc biệt thứ K của N 
#     nếu sắp xếp các số đặc biệt của N theo thứ tự tăng dần.
# Kết quả có thể rất lớn, hãy in ra theo modulo 109 + 7.

# Input
#     Dòng đầu tiên chứa một số nguyên duy nhất t (1 ≤ t ≤ 1e4) - số lượng bộ test.
#     Dòng tiếp theo chứa hai số nguyên N và K (2 ≤ N ≤ 1e9; 1 ≤ k ≤ 1e9).
# Output
#     Với mỗi bộ test, ghi ra số đặc biệt thứ K của N theo modulo 109 + 7
# Ví dụ

# Input           Output
# 3
# 3 4             9
# 2 12            12
# 105 564         3595374

# Giải thích: Với N = 3 dãy số đặc biệt là [1, 3, 4, 9…]

mod = 1000000007
def pow(a: int, b: int):
    if b==1: return a
    if b&1: return pow(a, b-1)*a%mod
    p = pow(a, b>>1)
    return p*p%mod
def cal(n: int, k: int):
    if k<=1: return k
    ex = 0
    while (k>>ex)^1: ex+=1
    return pow(n, ex) + cal(n, k^(1<<ex))
for t in range(int(input())):
    n, k = map(int, input().split())
    print(cal(n, k)%mod)
