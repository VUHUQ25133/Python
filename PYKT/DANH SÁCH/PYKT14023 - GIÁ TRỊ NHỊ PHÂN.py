# Cho một dãy nhị phân có N phần tử. 
# Ban đầu cả dãy có giá trị toàn 0. 
# Mỗi bước với hai giá trị x và y (1 ≤ x ≤ y ≤ N), 
#     thay đổi tất cả các bit từ vị trí x đến vị trí y        
#         (nếu đang là 1 thì thành 0 và ngược lại).
# Hãy cho biết sau Q lần thực hiện các truy vấn với 2 cặp số x, y thì 
#     trạng thái cuối cùng của dãy nhị phân là gì.

# Input:  Dòng đầu ghi hai số N và Q
#         Q dòng sau mỗi dòng ghi hai số x và y.
# Output: Ghi ra dãy kết quả.


#     Input       Output
#     3 2         0 0 1
#     1 2
#     1 3

# Ràng buộc:
#     50% test tương ứng với 1 ≤ N, Q ≤ 1000
#     50% test tương ứng với 1 ≤ N, Q ≤ 100000

n, q = map(int, input().split())
a = [0]*(n+2)
for i in range(q):
    x, y = map(int, input().split())
    a[x] += 1
    a[y+1] -= 1
for i in range(1,n+1): a[i] += a[i-1]
for i in range(1,n+1): print(a[i]%2, end=' ')
