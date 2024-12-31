# Một hôm nọ, Tom khám phá ra một loại bánh mới nên mời n người bạn đến nhà để thử tay nghề của mình. 
# Do (...), Tom đã làm ra n chiếc bánh với tỉ lệ nguyên liệu khác nhau. 
# Nhưng Tom biết chắc chắn rằng để chiếc bánh thứ i ngon hoàn hảo thì cần phải nướng ti phút. 
# Tuy nhiên vì số lượng bánh lớn nên Tom đã quyết định sẽ cho hết cả n chiếc bánh vào trong lò nướng. 
# Ở mỗi phút, Tom chỉ có thể đưa 1 và chỉ 1 chiếc bánh ra khỏi lò nướng. 
# Giả sử thời điểm lấy chiếc bánh thứ i ra là xi thì độ tệ của chiếc bánh sẽ bằng trị tuyệt đối của (ti - xi). 
# Tom muốn tổng độ tệ của n chiếc bánh là ít nhất có thể. 

# Input:
#     Dòng đầu tiên gồm 1 số t là số lượng bộ test t (1 ≤ t ≤  200)
#     Mỗi bộ test sẽ có dạng như sau:
#     Dòng đầu tiên gồm số n - số lượng bánh ( 1≤ n ≤  200)
#     Dòng thứ 2 gồm n số nguyên t1, t2,..., tn (1 ≤ ti ≤  n) 
#         là thời gian mà chiếc bánh thứ i cần nướng để đạt được độ ngon hoàn hảo.
#     Tổng của n ở tất cả các bộ test ≤ 200.
# Output:
#     Với mỗi bộ test, in ra kết quả bài toán ứng với bộ test đó trên 1 dòng.

#     Input                       Output
#     2
#     6                           4
#     4 2 4 4 5 2
#     7                           12
#     7 7 7 7 7 7 7

# Giải thích test 1:
#         Phút 1: Lấy chiếc bánh thứ 2 (có ti = 2) ra. Độ tệ = abs(2 - 1) = 1
#         Phút 2: Lấy chiếc bánh thứ 6 (có ti = 2) ra. Độ tệ = abs(2 - 2) = 0
#         Phút 3: Lấy chiếc bánh thứ 1 (có ti = 4) ra. Độ tệ = abs(4 - 3) = 1
#         Phút 4: Lấy chiếc bánh thứ 4 (có ti = 4) ra. Độ tệ = abs(4 - 4) = 0
#         Phút 5: Lấy chiếc bánh thứ 3 (có ti = 4) ra. Độ tệ = abs(4 - 5) = 1
#         Phút 6: Lấy chiếc bánh thứ 5 (có ti = 5) ra. Độ tệ = abs(5 - 6) = 1
#     Như vậy, tổng độ tệ của n chiếc bánh = 4, và đây cũng là kết quả tốt nhất có thể có được (đương nhiên có nhiều hơn 1 cách lấy các chiếc bánh ra khỏi lò, thứ tự trên chỉ là 1 trong số đó).

from sys import stdin
for t in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = [0] + sorted(map(int, stdin.readline().split()))
    #dp[i][j] minimum of cake 1 -> i when cooking end at j
    dp = [[0] * (300) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(i, 300):
            if j <= a[i]: dp[i][j] = dp[i-1][j-1] + abs(a[i] - j)
            else:
                if a[i] >= i: dp[i][j] = min(dp[i-1][a[i] - 1], dp[i-1][j-1] + abs(a[i] - j))
                else: dp[i][j] = dp[i-1][j-1] + abs(a[i] - j)
    print(min(dp[-1][n:]))
