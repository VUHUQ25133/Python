# Cho đồ thị vô hướng G có N đỉnh, M cạnh. 
# Hãy liệt kê các đỉnh không cùng thành phần liên thông với một đỉnh cho trước.
# Input
#       Dòng đầu ghi 3 số N, M và X (0 < N < 300; 1 ≤ M ≤ N*(N-1)/2), 0 < X < N).
#       Tiếp theo là M dòng, mỗi dòng ghi một cạnh của đồ thị. Các cạnh được liệt kê với thứ tự bất kỳ.
# Output
#       Ghi ra các đỉnh không liên thông với đỉnh X theo thứ tự tăng dần, mỗi dòng ghi một đỉnh. Nếu không có đỉnh nào thì ghi ra số 0.
# Ví dụ
# Input
# 6 4 2
# 1 3
# 2 3
# 1 2
# 4 5
# Output    
# 4
# 5
# 6

n, m, x = map(int, input().split())
ke = [[] for x in range(0, n+1)]
for i in range(m):
    a, b = map(int, input().split())
    ke[a].append(b)
    ke[b].append(a)
un, q, = [0]*(n+1), [x]
un[x]=1
while len(q)>0:
    u = q.pop()
    for i in ke[u]:
        if un[i]==0:
            q.append(i)
            un[i]=1
check = True
for i in range(1,n+1):
    if un[i]==0:
        check = False
        print(i)
if check: print(0)