# Cho mảng A[] gồm N số nguyên và số tự nhiên d.
# Hãy thực hiện quay mảng A[] với d phần tử từ phải qua trái. 
# Ví dụ A[] = {1, 2, 3, 4, 5}, d = 2 ta nhận được mảng A[] = {3, 4, 5, 1, 2}.
# Input:
#     Dòng đầu tiên đưa vào T là số lượng bộ test.
#     Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào N là số lượng phần tử của mảng A[] và số d; dòng tiếp theo đưa vào các phần tử A[i] của mảng A[].
#     T, N, d, A[i] thỏa mãn ràng buộc : 1≤T≤100; 1≤ d≤ N ≤1e7; 0≤ A[i] ≤1e9;
# Output: 
#     Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input:                      Output:
# 2
# 5 2
# 1 2 3 4 5                   3 4 5 1 2
# 10 3
# 2 4 6 8 10 12 14 16 18 20   8 10 12 14 16 18 20 2 4 6

for case in range(int(input())):
    n, index = [int(i) for i in input().split()]
    list = input().split()
    print(*(list[index:] + list[:index]))
