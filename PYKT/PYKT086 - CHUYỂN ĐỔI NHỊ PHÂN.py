# Cho xâu nhị phân X[] có độ dài n. 
# Nhiệm vụ của bạn là hãy đổi xâu nhị phân thành một số ở hệ cơ số b, 
#     trong đó b chỉ là một trong các số 2, 4, 8, 16. 
# Ví dụ xâu X ="10010100010010101" và b = 8 
#     ta có kết quả là 224225 là số ở hệ cơ số 8.

# Input - file văn bản DATA.in:
#     Dòng đầu tiên đưa vào T là số lượng bộ test.
#     Những dòng tiếp theo, mỗi dòng đưa vào T test. 
#       Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào b là cơ số của hệ đếm; 
#       dòng tiếp theo đưa vào xâu nhị phân có độ dài n.
#     T, n, X[] thỏa mãn ràng buộc : 1 ≤ T ≤ 10; 1 ≤ n≤ 1e5; X[i] = 0, 1;
# Output:
#     Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
#     DATA.in                     Output:
#     2                           1121127
#     8                           10010100010010101
#     10010100010010101
#     2
#     10010100010010101

from math import log2
def toS(i):
    if i<=9: return str(i)
    return chr(ord('A') + i-10)
def convert(s):
    r = 0
    for i in s: r = r<<1 | int(i)
    return toS(r)
f = open('DATA.in', 'r')
for t in range(int(f.readline())):
    b = int(log2(int(f.readline())))
    s = f.readline().strip()
    r = ''
    while s!='':
        r = convert(s[-b:]) + r
        s = s[:-b]
    print(r)
