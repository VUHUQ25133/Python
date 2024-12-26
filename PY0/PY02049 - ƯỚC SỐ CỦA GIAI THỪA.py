# Cho số tự nhiên N và số nguyên tố P. Nhiệm vụ của bạn là tìm số x lớn nhất để N! chia hết cho p^x. 
# Ví dụ với N=7, p=3 thì x=2 là số lớn nhất để 7! Chia hết cho 32. 
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T.
# Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test là cặp số N, p được viết cách nhau một vài khoảng trống.
# T, N, p thỏa mãn ràng buộc : 1≤T≤100; 1≤N≤105; 2≤p≤5000;
# Output:
# Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input:      Output:
# 3
# 62  7       9
# 76  2       73
# 3  5        0

for t in range(int(input())):
    N, p = [int(i) for i in input().split()]
    x = 0
    for i in range(2, N + 1):
        num = i
        while num % p == 0:
            num /= p
            x += 1
    print(x)
