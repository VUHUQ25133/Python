# Cho xâu nhị phân X[] có độ dài n. 
# Nhiệm vụ của bạn là hãy đổi xâu nhị phân thành một số ở hệ cơ số b, trong đó b chỉ là một trong các số 2, 4, 8, 16. 
# Ví dụ xâu X =”10010100010010101” và b = 8 ta có kết quả là 224225 là số ở hệ cơ số 8.
# Input:
#     Dòng đầu tiên đưa vào T là số lượng bộ test.
#     Những dòng tiếp theo, mỗi dòng đưa vào T test. 
#     Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào b là cơ số của hệ đếm; dòng tiếp theo đưa vào xâu nhị phân có độ dài n.
#     T, n, X[] thỏa mãn ràng buộc : 1≤T≤10; 1≤ n≤1e5; X[i] =0, 1;
# Output:
#     Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input:                  Output:
# 2
# 8
# 10010100010010101       224225
# 2
# 10010100010010101       10010100010010101

from math import log2

BASE = '0123456789ABCDEF'

for t in range(int(input())):
    base = int(log2(int(input())))
    num = input()
    while len(num) % base:
        num = '0' + num
    pow = [1]
    for i in range(1, base):
        pow = [pow[0]*2] + pow
    res = ''
    for i in range(0, len(num), base):
        e = 0
        for j in range(i, i+base):
            e += int(num[j])*pow[j-i]
        res += BASE[e]
    print(res)
