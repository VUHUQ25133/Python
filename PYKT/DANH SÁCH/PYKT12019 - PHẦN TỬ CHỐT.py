# Cho dãy số A[] gồm có N phần tử. 
# Phần tử A[i] được gọi là phần tử Pivot (hay phần tử chốt) nếu như nó phân hoạch dãy số thành 2 phần:
#     Các phần tử bên trái có giá trị nhỏ hơn hoặc bằng A[i],
#     Các phần tử bên phải có giá trị lớn hơn A[i].
#         Với dãy số A[] = {2, 1, 3, 4, 6, 5, 7}, có 3 phần tử chốt là 3, 4, 7. 
#             Với phần tử 3, ta có phân hoạch {2, 1}, 3 và {4, 6, 5, 7} thỏa mãn các tính chất nêu trên. 
#             Với phần tử 7, tập hợp các phần tử bên phải là một tập rỗng nên cũng thõa mãn yêu cầu.
# Việc xác định được phần tử chốt đóng vai trò quan trọng trong thuật toán Quicksort. 
# Các bạn hãy xác định xem dãy số đã cho có bao nhiêu phần tử chốt?
# Input:
#     Dòng đầu tiên là số lượng bộ test (T ≤ 10).
#     Dòng test bắt đầu bởi số nguyên N (1 ≤ N ≤ 100 000) là số lượng phần tử của dãy số.
#     Dòng tiếp theo gồm N phần tử A[i] (0 ≤ A[i] ≤ 109).
# Output: 
#     In ra đáp án là số lượng phần tử chốt tìm được.
# Ví dụ:
#     Input           Output
#     3               1
#     3               3
#     1 1 1           3
#     3
#     1 2 3
#     7
#     2 1 3 4 6 5 7

e = 10**12
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    arr = [[-1, e] for i in range(n)]
    maxr = e
    for i in range(n-1,-1,-1):
        arr[i][1] = maxr
        maxr = min(maxr, a[i])
    maxl = -1
    for i in range(n):
        arr[i][0] = maxl
        maxl = max(maxl, a[i])
    cnt = 0
    for i in range(n):
        if arr[i][0]<=a[i] and arr[i][1]>a[i]: cnt+=1
    print(cnt)
