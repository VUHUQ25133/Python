# Cho mảng A[] gồm N số nguyên khác nhau. 
# Nhiệm vụ của bạn là đếm số lượng các bộ ba phần tử khác nhau có tổng là 0. 
# Ví dụ A[] = {0, -1, 2, -3, 1}, ta nhận được kết quả là 2 vì có hai bộ 3: (0, -1, 1) và (2, -3, 1).
# Input:
#     Dòng đầu tiên đưa vào T là số lượng bộ test.
#     Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là gồm hai dòng: 
#       dòng đầu tiên đưa vào N là số lượng phần tử của mảng A[]; 
#       dòng tiếp theo đưa vào các phần tử A[i] của mảng A[].
#     T, N, A[i] thỏa mãn ràng buộc : 1≤T≤100; 1≤ N≤1e3; -1e9≤ A[i] ≤1e9;
# Output:
#     Đưa ra kết quả mỗi test theo từng dòng.

# Ví dụ:
# Input:              Output:
# 2
# 5
# 0 -1 2 -3 1         2
# 5
# 1 -2  1  0  5       1

for t in range(int(input())):
    n = int(input())
    l = sorted([int(i) for i in input().split()])
    res = 0
    for i in range(n-2):
        left, right = i+1, n-1
        while left < right:
            tmp = l[i] + l[left] + l[right]
            if not tmp:
                res += 1
                left += 1
            elif tmp < 0:
                left += 1
            else:
                right -= 1
    print(res)
