# Cho mảng A[] gồm n số nguyên dương. 
# Gọi L, R là max và min các phần tử của A[]. 
# Nhiệm vụ của bạn là tìm số phần tử cần thiết cần thêm vào mảng để mảng có đầy đủ các số trong khoảng [L, R]. 
# Ví dụ A[] = {5, 7, 9, 3, 6, 2 } ta nhận được kết quả là 2 tương ứng với các số còn thiếu là 4, 8.

# Input:
#       Dòng đầu tiên đưa vào số lượng bộ test T.
#       Những dòng kế tiếp đưa vào T bộ test. Mỗi bộ test gồm hai dòng: dòng đầu tiên đưa vào n, tương ứng với số phần tử của mảng A[]; dòng tiếp theo là n số A[i].
#       T, n, A[i] thỏa mãn ràng buộc: 1≤ T ≤100; 1≤ n, A[i] ≤103.
# Output: Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:

#     Input:          Output:
#     2               1
#     5               0
#     4 5 3 8 6
#     3
#     2 1 3


for t in range(int(input())):
    n, a = int(input()), list(map(int, input().split()))
    Max, Min, total = max(a), min(a), 0
    if Max - Min <= 1: print(0)
    else:
        dic = {Max:1, Min:1}
        for i in a:
            if dic.get(i) is None:
                total+=1
                dic[i]=1
        print(Max - Min -1 -total)
