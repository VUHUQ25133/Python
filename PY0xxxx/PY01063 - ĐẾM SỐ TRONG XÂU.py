# Cho một ký tự S[] chỉ có các chữ số, độ dài không quá 1000, 
# và số nguyên dương N (không quá 9 chữ số). 
# Hãy đếm xem số N xuất hiện bao nhiêu lần trong S[].
# Chú ý: các ký tự số không được đếm lặp. Tức là mỗi ký tự chỉ được xét một lần.
# Ví dụ: S[] = “1212121112211221121”, N = 121 thì đáp án là 3. 

# Input
# Dòng đầu ghi số bộ test, không quá 20.
# Mỗi test gồm hai dòng, dòng đầu là xâu ký tự S[], dòng sau là số N.

# Output
# Với mỗi bộ test, ghi ra kết quả tính được trên một dòng.

# Ví dụ
# Input                   Output

# 2
# 1212121112211221121     3
# 121
# 2222222222322292        2
# 2222

for t in range(int(input())):
    s = input()
    n = input()
    l, id, cnt = len(n), s.find(n), 0
    while id != -1:
        cnt += 1
        id = s.find(n, id + l)
    print(cnt)

    