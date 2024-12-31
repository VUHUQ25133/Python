# Dãy số nguyên dương tăng dần trong đó 
# ước số nguyên tố lớn nhất của các số trong dãy đều không vượt quá 5 được gọi là dãy số Hamming. 
# Ví dụ 10 = 2 x 5 thuộc dãy Hamming còn 26 = 2 x 13 không thuộc dãy Hamming.
# Số 1 được coi là số đầu tiên của dãy Hamming.
# Cho số nguyên dương N.  
# Hãy xác định xem N có thuộc dãy Hamming hay không và nếu có thì thứ tự của N trong dãy Hamming là bao nhiêu.
# Input:
# Dòng đầu tiên ghi số bộ test (không quá 105).
# Mỗi test ghi một số N (1 ≤ N ≤ 1018).
# Output:
# Nếu giá trị N thuộc dãy Hamming thì ghi ra thứ tự của N (tính từ 1).
# Nếu không thì ghi ra “Not in sequence”
# Ví dụ:

# Input   Output
# 11
# 1       1
# 2       2
# 6       6
# 7       Not in sequence
# 8       7
# 9       8
# 10      9
# 11      Not in sequence
# 12      Not in sequence
# 13      10
# 14      Not in sequence

N = 10**18
list = []

i = 1
while i <= N:
    j = 1
    while j <= N:
        k = 1
        while k <= N:
            list += [i * j * k]
            k *= 5
        j *= 3
    i *= 2
list.sort()

def binSearch(l, r, x):
    if l > r:
        return 'Not in sequence'
    m = (l + r) // 2
    if list[m] == x:
        return m + 1
    if list[m] < x:
        return binSearch(m + 1, r, x)
    return binSearch(l, m - 1, x)


for t in range(int(input())):
    n = int(input())
    print(binSearch(0, len(list), n))
