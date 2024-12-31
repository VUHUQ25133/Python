# Cho chuỗi nhị phân S có chiều dài bằng N và số nguyên K.
#     Chọn ngẫu nhiên 2 số nguyên i, j trong khoảng từ 1 tới N.
# Xác suất để S[i], S[j] đều là bit 1 và |i-j| ≤ K là bao nhiêu?
# Input
#     Dòng đầu tiên là số lượng bộ test T (T ≤ 100 000).
#     Mỗi test bắt đầu bởi 2 số nguyên N và K.
#     Dòng tiếp theo gồm xâu S chứa các kí tự 0 và 1.
#     Chú ý: Tổng giá trị của N trong tất cả các test ≤ 100 000.
# Output
#     In ra xác suất tìm được dưới dạng phân số tối giản dạng X/Y. Nếu xác suất bằng 0, in ra 0/1.

# Input           Output
# 2               9/16
# 4 3             1/16
# 1011
# 4 1
# 1000

from math import gcd


for t in range(int(input())):
    n, k = map(int, input().split())
    s, a = '0'+input(), [0]*(n+1)
    for i in range(1,n+1):
        a[i] = a[i-1] + (1 if s[i]=='1' else 0)
    r = 0
    for i in range(1, n+1):
        if s[i]=='1':
            if i<=k: r+=1+2*(a[i]-1)
            else: r+=1+2*(a[i]-a[i-k-1]-1)
    m = n*n
    if r==0: print('0/1')
    else:
        x=gcd(r,m)
        print(f'{r//x}/{m//x}')
