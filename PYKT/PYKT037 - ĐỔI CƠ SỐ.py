# Cơ số từ 2 đến 36 được xây dựng từ 10 chữ số (0 đến 9) và 26 chữ cái Tiếng Anh in hoa ('A' đến 'Z').
# Hãy viết chương trình chuyển một số nguyên dương N trong cơ số 10 sang cơ số b. Trong đó N không quá 100.000, 2 ≤ b ≤ 36.
# Input
#     Dòng đầu ghi số bộ test, không quá 10.
#     Mỗi bộ test ghi 2 số N và b.
#     N là một số nguyên dương N trong cơ số 10, không quá 100.000.  2 ≤ b ≤ 36
# Output
#     Với mỗi bộ test ghi ra kết quả đổi cơ số tương ứng.
# Ví dụ
#     Input       Output
#     3
#     10 2        1010
#     2021 2      11111100101
#     1F
#     31 16       

def std(i):
    if i<=9: return i
    return chr(ord('A') + i - 10)
for t in range(int(input())):
    a, b = map(int, input().split())
    i = 0 
    while a >= b**i: i+=1
    i-=1
    for j in range(i+1):
        c = a//(b**i)
        print(std(c), end='')
        a = a - c*(b**i)
        i-=1
    print()