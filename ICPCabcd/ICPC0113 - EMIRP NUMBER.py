# Một số nguyên dương K được gọi là Emirp Number nếu K là số nguyên tố, 
#     đảo các chữ số của K cũng là một số nguyên tố nhưng không phải chính nó (không đối xứng). 
#     Ví dụ số 11 không phải là số Emirp Number. 
# Cho số tự nhiên N, nhiệm vụ của bạn là hãy liệt kê tất cả các số Emirp Number nhỏ hơn N.

# Input:
#     Dòng đầu tiên đưa vào T là số lượng bộ test.
#     Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
#     T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤1e6;
# Output:
#     Đưa ra kết quả mỗi test theo từng dòng.
#     Chú ý: ghi theo các cặp số thỏa mãn từ nhỏ đến lớn, xem ví dụ để hiểu hơn về cách hiển thị kết quả. 
# Ví dụ:
# Input:  Output:

# 2
# 40      13 31
# 100     13 31 17 71 37 73 79 97

from math import sqrt

def emirp(n):
    if n == 2 or n == 3:
        return True
    if n < 5 or n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(sqrt(n)+1), 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

for __ in range(int(input())):
    used = []
    n = int(input())
    for i in range(13, n):
        num = str(i)
        if int(num[::-1]) < n and num != num[::-1] and emirp(int(num)) and emirp(int(num[::-1])) and num not in used:
            print(i, num[::-1], end=' ')
            used += [num, num[::-1]]
    print()
