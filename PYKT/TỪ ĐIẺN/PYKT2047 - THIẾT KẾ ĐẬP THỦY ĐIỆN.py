# Trên thượng lưu sông High River, một con đập lớn đang được xây dựng.
# Do dòng sông chảy xiết, các kĩ sư thiết kế N bức tường chắn nước tại các vị trí L[i], có độ cao tương ứng bằng H[i].
# Mỗi bức tường có độ dày bằng 1 đơn vị.

# Do tính phức tạp của con đập, một số bức tường vẫn đang được xây dựng tiếp theo ở phía dưới. 
# Do đó, các kĩ sư cần có hệ thống cảnh báo để xác định giới hạn vùng an toàn cho công việc xây dựng ở phía sau.

# Giả sử lưu lượng nước đổ về là K đơn vị thể tích. 
# Các bạn giúp các kĩ sư hãy tính toán xem vị trí bức tường cuối cùng sẽ bị nước tràn qua?

# Input
#     Dòng đầu tiên là số lượng bộ test T (T <= 20).
#     Mỗi test bắt đầu bởi số lượng bức tường N (N <= 10^5).
#     Dòng thứ hai gồm N số nguyên L[] mô tả vị trí của các bức tường (1 <= L[i] <= 10^9, L[i] > L[i-1] + 1).
#     Dòng thứ ba gồm N số nguyên H[] mô tả chiều cao của các bức tường (1 <= H[i] <= 10^5).
#     Tiếp theo là số lượng truy vấn Q (Q <= 10^5).
#     Q dòng tiếp theo, mỗi dòng gồm một số nguyên K (1 <= K <= 10^15).
# Output
#     Với mỗi truy vấn, hãy in ra đáp án trên một dòng. Nếu bức tường thứ nhất không bị vượt qua, in ra 0.
 
# Test ví dụ:
#     Input               Output
#     1
#     4                   3
#     1 3 5 8             1
#     2 5 3 1             1
#     3
#     17
#     3
#     13


def low(a, l, r, x):
    while l<r:
        mid = (l + r) >> 1
        if a[mid] < x: l = mid + 1
        else: r = mid
    return l
def first_big(a, arr):
    st = []
    for i in range(1, len(a)):
        if len(st) == 0:
            arr[i] = 0
            st.append(i)
        else:
            while len(st) > 0 and a[st[-1]] <= a[i]: st.pop()
            if len(st) == 0: arr[i] = 0
            else: arr[i] = st[-1]
            st.append(i)
test = int(input())
e = []
while True:
    try: e.extend(map(int, input().split()))
    except: break
I = 0
for t in range(test):
    n = e[I]
    I += 1
    l = [-1] + e[I:I+n]
    I += n
    h = [0] + e[I:I+n]
    I += n

    left = [0]*(n+1)
    first_big(h, left)

    Vn, Vw = [0] * (n + 2), [0] * (n + 2)
    for i in range(1, n + 1):
        if h[i] > h[i-1]: 
            Vn[i] = Vn[left[i]] + h[i]*(l[i] - l[left[i]] - 1) - (Vw[i-1] - Vw[left[i]])
        else: Vn[i] = Vn[i-1] + h[i]*(l[i] - l[i-1] - 1)
        Vw[i] = Vw[i-1] + h[i]
    Vn[n+1] = 10**18
    Q = e[I]
    I += 1
    for q in range(Q):
        k = e[I + q]
        print(low(Vn, 1, n+1, k) - 1)
    I += Q
