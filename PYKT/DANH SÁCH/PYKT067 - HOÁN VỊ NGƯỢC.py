# Cho số nguyên dương N. 
# Nhiệm vụ của bạn là hãy liệt kê tất cả các hoán vị của 1, 2, .., N theo thứ tự ngược. 
# Ví dụ với N = 3 ta có kết quả: 321, 312, 231, 213, 132, 123.
# Input
#     Dòng đầu tiên đưa vào số lượng test T.
#     Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test là một số tự nhiên N được viết trên một dòng.
#     T, n thỏa mãn ràng buộc: 1 ≤ T, N ≤ 10.
# Output:
#     Với mỗi test, dòng đầu tiên đưa ra số lượng hoán vị. Dòng thứ hai liệt kê các hoán vị ngược tìm được.
# Ví dụ:
# Input       Output
# 2           2
# 2           21 12 
# 3           6
#             321 312 231 213 132 123 

from itertools import permutations
for i in range(int(input())):
    a = list(reversed(list(permutations([str(x) for x in range(1, int(input())+1)]))))
    print(len(a))
    for i in a: print(''.join(i), end=' ')
    print()
