# Mảng a ban đầu có n số nguyên. Bạn có thể thực hiện thao tác sau nhiều lần:
#     **Chọn số 2 số x và y bất kỳ trong mảng và thêm "2x - y" vào mảng.
# Với 1 số nguyên k, hãy kiểm tra xem bạn có thể tạo ra được số k hay không.

# Input:
#     Dòng đầu tiên chứa số bộ test t (t ≤ 20). Mỗi test có định dạng như sau:
#         - Dòng đầu tiên chứa 2 số nguyên n và k (2 ≤ n ≤ 105, -109 ≤ k ≤ 109)
#         - Dòng tiếp theo chứa n số nguyên ban đầu (-109 ≤ ai ≤ 109)
# Output:
#     Với mỗi test, in ra “YES” nếu có thể và “NO” trong trường hợp còn lại.

#     Input                       Output
#     6                           YES
#     2 1                         YES
#     1 2                         NO
#     3 0                         YES
#     2 3 7                       YES
#     2 -1                        NO
#     31415926 27182818
#     2 1000000000000000000
#     1 1000000000000000000
#     2 -1000000000000000000
#     -1000000000000000000 123
#     6 80
#     -5 -20 13 -14 -2 -11


def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)
from sys import stdin

for t in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    g = 0
    for i in range(1,n):
        g = gcd(g, a[i]-a[0])
    if g!= 0 and (k-a[0])%g==0: print('YES')
    else: print('NO')
