# Cho hai số a và b trong đó a≤1e12, b≤1e250. Nhiệm vụ của bạn là tìm ước số chung lớn nhất của hai số a, b.

# Input:
# Dòng đầu tiên đưa vào T là số lượng bộ test.
# T dòng tiếp đưa các bộ test. Mỗi bộ test gồm hai dòng: dòng đầu tiên đưa vào số a; dòng tiếp theo đưa vào số b.
# Các số T, a, b thỏa mãn ràng buộc: 1≤T≤100; 1≤a≤1e12; 1≤b≤1e250;
# Output:
# Đưa ra kết quả mỗi test theo từng dòng.

# Ví dụ:
# Input
# 1
# 1221
# 1234567891011121314151617181920212223242526272829
# Output
# 3

from math import gcd

for t in range(int(input())):
    a = int(input())
    b = int(input())
    print(gcd(a, b))