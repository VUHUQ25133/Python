# Cho dãy số A[] gồm có N phần tử. Bạn được phép tăng, giảm một phần tử mỗi lần 1 đơn vị. 
# Nhiệm vụ của bạn là hãy sử dụng ít bước nhất có thể để chuyển dãy số đã cho về dạng dãy số ‘mái nhà’, 
#   với các tính chất sau :
#     Một phần tử lớn nhất là đỉnh (giả sử là phần tử thứ i)
#     Các phần tử bên trái và bên phải giảm dần đi 1 đơn vị, tức là với mọi j, A[j] = A[i] - |i-j|
#     Tất cả các phần tử A[j] đều phải lớn hơn 0.
# Input:
#     Dòng đầu tiên là số nguyên N (N ≤ 5000).
#     Dòng tiếp theo gồm N phần tử của dãy số (1 ≤ A[i] ≤ 5000).
# Output: In ra số bước ít nhất để có thể hoàn thành bài toán trên.

#     Input:          Input: 
#     5               6
#     4 5 6 2 2       4 5 6 5 4 3
#     Output:         Output:
#     3               0

# Giải thích test 1: Chuyển dãy số về 4 5 4 3 2

from sys import stdin
n=int(stdin.readline())
a = list(map(int, stdin.readline().split()))
ans = 10**18
for i in range(n) :
    change = 0
    b = a.copy()
    # for j in range(n):
    #     b[j] += abs(j - i) - i
    for j in range(i):
        b[j] += change
        change-=1
    for j in range(i,n) :
        b[j] += change
        change += 1
    b.sort()
    top = max(b[n//2], -change, 0) + i
    steps = 0
    for j in range(i):
        steps += abs(top - abs(i-j) - a[j])
    for j in range(i,n) :
        steps += abs(top - abs(i-j) - a[j])
    ans = min(ans, steps)
print(ans)
