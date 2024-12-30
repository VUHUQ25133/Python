# Tình hình chiến sự ở vùng biển Z đang trở nên cực kì cam go. 
# Nhà vua quyết định gửi thêm quân chi viện tới chiến trường.  
# Trong tay nhà vua đang có quyền triệu tập k đội quân từ khắp mọi miền đất nước. 
# Để tập trung binh lực tốt nhất, nhà vua đã triệu tập cả k đội quân đến kinh thành rồi sau đó mới di chuyển đến chiến trường. 
# Do số lượng đoàn quân khá lớn, nhà vua quyết định để 1 đại tướng đi thuê xe để chở quân lính. 
# Vì tình đoàn kết, tất cả các chiến sĩ từ k quân đoàn tuyên bố: 
# Nếu di chuyển, họ muốn được di chuyển cùng tất cả các đồng đội của mình trên một xe và 
#     trên xe đó không được có tới 3 quân đoàn khác nhau vì như vậy rất dễ xảy ra xô xát. 
# Đến đây , tướng quân rất đau đầu trong việc chọn lựa loại xe đưa các đội quân đi vì nhà vua muốn chi phí di chuyển là ít nhất. 
# Chi phí di chuyển sẽ bằng số lượng xe thuê nhân với sức chứa của loại xe.  
# Hãy giúp tướng quân tính toán ra chi phí nhỏ nhất để thuê xe mà thỏa mãn yêu cầu của tất cả quân lính nhé

# Input:
#     Dòng đầu tiên gồm số n và k (1 ≤ n ≤ 5e5, 1 ≤ k ≤ 10000). Với n là số lượng quân lính, k là số lượng các quân đoàn. 
#         Giả sử các quân đoàn đánh số từ 1 đến k.
#     Dòng thứ 2 gồm n số nguyên a[i] (1 ≤ a[i] ≤ k) trong đó a[i] là số hiệu quân đoàn của người lính thứ i.
# Output:
#     Ghi ra chi phí nhỏ nhất.

# Input               Output
# 6 3
# 3 1 2 3 2 3         6

# Giải thích:
#     Có 6 người lính đến từ 3 đội quân khác nhau.
#         Đội 1 có 1 người
#         Đội 2 có 2 người
#         Đội 3 có 3 người
#     Cách tốt nhất là thuê 2 xe có sức chứa 3 người. 
# Khi đó đội quân 1 và 2 sẽ lên cùng 1 xe, đội quân 3 lên 1 xe. 
# Tổng chi phí thuê xe sẽ là 3 x 2 = 6.

n, k = map(int, input().split())
a = map(int, input().split())
cnt = [0]*k
for i in a: cnt[i-1] += 1
a = []
for i in cnt:
    if i: a.append(i)
a.sort()
k = len(a)

def get(box):
    L, R, res = 0, k - 1, 0
    while L <= R:
        res += 1
        if L == R:
            break
        if a[L] + a[R] > box:
            R -= 1
        else:
            L += 1
            R -= 1
    return res * box
l, r = a[-1], min(a[-1] + 500, a[-1]*2)
ANS = get(l)
for i in range(l + 1, r):
    ANS = min(ANS, get(i))
print(ANS)
