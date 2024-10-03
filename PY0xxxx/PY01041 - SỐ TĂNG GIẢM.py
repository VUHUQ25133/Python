# Một số nguyên dương được gọi là số tăng giảm nếu thỏa mãn các điều kiện:
# Có từ 3 chữ số trở lên
# Tìm ra một vị trí trong dãy chữ số sao cho từ bên trái đến vị trí đó thỏa mãn thứ tự tăng dần (tăng chặt) còn từ vị trí đó đến hết thì thỏa mãn thứ tự giảm dần (giảm chặt).
# Viết chương trình kiểm tra một số có phải số tăng giảm hay không.

# Input
# Dòng đầu ghi số bộ test. Mỗi bộ test viết trên một dòng số nguyên dương N không quá 18 chữ số

# Output
# Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ

# Input       Output
# 3
# 12342       YES
# 23342       NO
# 5678961     YES

def solve(s):
    if len(s) < 3:
        return 'NO'
    ar = list(int(i) for i in s)
    up = True
    for i in range(1, len(ar)):
        if up and ar[i] <= ar[i - 1]:
            up = False
        elif not up and ar[i] >= ar[i - 1]:
            return 'NO'
    return 'YES'


for t in range(int(input())):
    s = input()
    print(solve(s))