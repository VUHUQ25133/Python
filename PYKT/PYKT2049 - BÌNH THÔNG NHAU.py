# Có N thùng nước được đánh số từ 1 đến N, giữa 2 thùng bất kỳ đều có một ống nối có một van có thể khóa hoặc mở. 
# Ở trạng thái ban đầu tất cả các van đều đóng.

# Bạn được cho một số yêu cầu, trong đó mỗi yêu cầu có 2 dạng:
#    Dạng X Y 1 có ý nghĩa là bạn cần mở van nối giữa 2 thùng X và Y.
#    Dạng X Y 2 có ý nghĩa là bạn cần cho biết với trạng thái các van hiện tại 
#	thì 2 thùng X và Y có thuộc cùng một nhóm bình thông nhau hay không.
# Hai thùng được coi là thuộc cùng một nhóm bình thông nhau 
#    nếu nước từ bình này có thể chảy đến được bình kia qua một số ống có van đang mở.

# Input:
#     Dòng đầu tiên là số lượng truy vấn Q (Q <= 100 000).
#     Mỗi truy vấn gồm 3 số nguyên X, Y, Z (X, Y <= 100 000).

# Output: 

#     Với mỗi truy vấn, in ra đáp án tìm được trên một dòng.

# Input		Output
# 9
# 1 2 2         0        
# 1 2 1	        0
# 3 7 2	        1
# 2 3 1	        0
# 1 3 2	        1
# 2 4 2	        0
# 1 4 1
# 3 4 2
# 1 7 2

n = int(input())
par = [-1] * (n + 1)
def root(x):
    if par[x] < 0: return x
    par[x] = root(par[x])
    return par[x]
def merge(x, y):
    x = root(x)
    y = root(y)
    if x == y: return
    if par[y] < par[x]: 
        tmp = x
        x = y
        y = tmp
    par[x] += par[y]
    par[y] = x
for i in range(n):
    x, y, z = map(int, input().split())
    if z == 1: merge(x, y)
    else: print(1 if root(x) == root(y) else 0)
