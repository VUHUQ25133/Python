# Cho vùng tọa độ Oxy bị giới hạn bởi gốc tọa độ (0, 0) và điểm trên cùng bên phải (X, Y). 
# Nhiệm vụ của bạn là hãy xác định xem có bao nhiêu tam giác vuông cân.
# Input:
#     Dòng đầu tiên là số lượng bộ test T (T <= 100).
#     Mỗi test gồm hai số nguyên X và Y.
#     Giới hạn
#         Subtask 1 (25%) 0 <= X, Y <= 20
#         Subtask 2 (25%) 0 <= X, Y <= 100.
#         Subtask 3 (50%) 0 <= X, Y <= 1000.
# Output: 
#     Với mỗi test, in ra số tam giác vuông tìm được trên một dòng.

# Example:            
#     Input               Output
#     3
#     0 5                 0
#     1 2                 10
#     1 1                 4

from sys import stdin
#this solution is relative =)), may get TLE 
def solve(i, j, x, y): 
    s, p = i - j, i + j
    a = min(s+y, x) - max(s, 0) + 1
    b = min(p, y) - max(p-x, 0) + 1
    return a*b - 1

for t in range(int(stdin.readline())):
    x, y = map(int, stdin.readline().split())
    ans = 0
    X, Y = (x + 2) >> 1, (y + 1) >> 1
    for i in range(X):
        for j in range(Y): ans += solve(i, j, x, y) << 1
        if y % 2 == 0: ans += solve(i, y >> 1, x, y)
        if i == (x - 1) >> 1: ans <<= 1
    print(ans)
