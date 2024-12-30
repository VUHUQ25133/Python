# Thành phố X mới xây dựng xong 2 khu đô thị mới và bắt đầu kế hoạch di chuyển dân cư. 
# Có tổng cộng N người đăng kí chuyển đến khu đô thị mới, trong khi sức chứa của khu đô thị 1 và 2 chỉ là lần lượt C và D.
# Chỉ số A[i] thể hiện mức độ giàu có của người thứ i. 
# Ban quản lý dự án muốn sự giàu có ở 2 khu đô thị này là lớn nhất có thể. 
# Chỉ số đánh giá được tính bằng tổng trung bình chỉ số giàu có của cư dân ở 2 khu độ thị mới 
#     (trung bình của khu đô thị 1 + trung bình khu đô thị 2).
# Các bạn hãy tính xem khi sắp xếp tối ưu, chỉ số đánh giá này có giá trị lớn nhất bằng bao nhiêu?
# Input:
#       Dòng đầu tiên là số lượng bộ test T (T ≤ 10).
#       Mỗi test bắt đầu bằng số nguyên N, C và D (1 ≤ N, C, D ≤ 100 000, C + D ≤ N).
#       Dòng tiếp theo gồm N số nguyên A[i] (1≤ A[i] ≤ 100 000).
# Output: 
#       Với mỗi test in ra đáp án trên một dòng, độ chính xác là 6 chữ số sau dấu phảy.

#     Input               Output
#     2
#     2 1 1               6.000000
#     1 5
#     4 2 1               6.500000
#     1 4 2 3


# Giải thích test 2:  Phương án tối ưu là chọn 2 người số 3, 4 tới khu đô thị 1, và người số 2 tới khu đô thị còn lại. 
#                     Ta có (a[3]+a[4])/2 + a[2] = (3+2)/2 + 4 = 6.5.

for t in range(int(input())):
    n, c, d = map(int, input().split())
    c, d = sorted([c, d])
    a = sorted(map(int, input().split()), reverse=True)
    s1, s2 = 0, 0
    for i in a[:c]: s1+=i
    for i in a[c:c+d]: s2+=i
    print(f'{(s1/c+s2/d):.6f}')
