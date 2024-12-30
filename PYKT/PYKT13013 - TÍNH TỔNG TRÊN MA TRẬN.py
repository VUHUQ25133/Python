# Cho một ma trận N x M (N hàng, M cột). 
# Ban đầu, các phần tử của ma trận được gán giá trị như sau:

#         1           2         …   M
#         M+1         M+2       …   M+N
#         ……………………………………………………………………………….
#         (N-1)M+1    (N-1)M+2  …   NM

# Có K loại truy vấn, mỗi truy vấn có dạng:
#     “R X Y”: Nhân hàng X của ma trận với Y
#     “S X Y”: Nhân cột X của ma trận với Y
# Nhiệm vụ của bạn là hãy tính tổng các phần tử của ma trận sau K truy vấn trên.

# Input:
#     Dòng đầu tiên chứa 3 số nguyên N, M, K (1 ≤ N, M ≤ 106, K ≤ 1000).
#     K dòng tiếp theo, mỗi dòng chứa một truy vấn (0 ≤ Y ≤ 109).
# Output: 
#     In ra đáp án của bài toán theo modulo 109 + 7.

#                 Test 1              Test 2
#     Input:      3 1 1               3 4 4
#                 S 1 4               R 2 4
#                                     S 4 2
#                                     R 3 3
#                                     R 2 0
#     Output:     24                  176

# Giải thích test 2: 1 + 2 + 3 + 8 + 27 + 30 + 33 + 72 = 176

#     1   2   3   8
#     0   0   0   0
#     27  30  33  72


mod = 1000000007
n, m, k = map(int, input().split())
row = {}
col = {}
ans=0 
for i in range(k):
    c, x, y = input().split()
    x = int(x)
    y = int(y)
    if c=='R': 
        if row.get(x) is None: row[x]=y
        else:
            row[x]*=y
            row[x]%=mod
    else: 
        if col.get(x) is None: col[x]=y
        else:
            col[x]*=y
            col[x]%=mod
def sumr(x):
    return (m*x+m*(x-1)+1)*m//2%mod
def sumc(x):
    return (n*x + m*((n-1)*n//2))%mod
ans = 0
ans = (n*m+1)*n*m//2%mod
for i in row: 
    ans+=sumr(i)*(row[i]-1)
    ans%=mod
for i in col: 
    ans+=sumc(i)*(col[i]-1)
    ans%-mod
for i in row:
    for j in col:
        x = (i-1)*m + j
        ans = (ans - x*(row[i]+col[j]-1) + x*row[i]*col[j])%mod
ans = (ans+mod)%mod
print(ans)
