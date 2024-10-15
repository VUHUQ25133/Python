# Cho mảng A[] gồm N số nguyên.      
# Nhiệm vụ của bạn là tìm tổng nhỏ nhất của bộ ba số trong mảng. 
#     Ví dụ A[] = {1, 2, 3, 4, 5}, ta nhận được tổng nhỏ nhất của bộ ba số là 1 + 2 + 3 = 6. 
#     Chú ý nếu sử dụng kỹ thuật sắp xếp, submit lời giải của bạn sẽ bị fail.
# Input:
#     Dòng đầu tiên đưa vào T là số lượng bộ test.
#     Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào N là số lượng phần tử của mảng A[]; dòng tiếp theo đưa vào các phần tử A[i] của mảng A[].
#     T, N, A[i] thỏa mãn ràng buộc : 1 ≤ T ≤ 100; 1 ≤ N ≤1e6; -1e8 ≤ A[i] ≤ 1e8;
# Output:
#     Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input:              Output:
# 2
# 7
# 1 2 3 0 -1 8 10     0
# 7
# 9 8 20 3 4 -1 0     2

import heapq
import re

t = int(input())
for z in range(t) :
    n = int(input())
    main = ' ' + input().replace(' ', '  ') + ' '
    a = []
    i = -8
    while i < 9 and len(a) < 4:
        s = '\d' * abs(i) + ' '
        if i < 0 :
            s = '-' + s
        elif i > 0 :
            s = ' ' + s
        else :
            i += 1
            continue
        a += [int(x) for x in re.findall(s, main)]
        i += 1
    ans = 0
    for x in heapq.nsmallest(3, a):
        ans += x
    print(ans)
