# Xâu ký tự S được tạo ra bằng cách bổ sung dần các ký tự chữ cái Tiếng Anh in hoa như sau.
# Bước 1: Chỉ có chữ cái A
# Bước 2: Thêm chữ cái B vào giữa 2 chữ A => S = "ABA"
# Bước 3: Thêm chữ cái C vào giữa 2 xâu đã có ở bước 2: S = "ABACABA"
# Cứ như vậy cho đến bước thứ N (0 < N < 26)
# Hãy xác định ký tự thứ K trong bước biến đổi thứ N là chữ cái gì?
# Input:
# Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
# Mỗi test gồm số nguyên dương N và K (1 ≤ N ≤ 25, 1 ≤ K ≤ 2N - 1).
# Output: 
# Với mỗi test, in ra đáp án trên một dòng.
# Ví dụ:

# Input       Output
# 2
# 3 2         B
# 4 8         D
def find(n, k) :
    if k == 2**(n - 1) : return n
    if k > 2**(n - 1) : return find(n - 1, k - 2**(n - 1))
    return find(n - 1, k)

t = int(input())
for i in range(t) :
    n, k = [int(x) for x in input().split()]
    print(chr(find(n, k) + ord('A') - 1))
