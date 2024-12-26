# Cho một xâu ký tự có thể có các ký tự chữ cái và chữ số. 
# Người ta thực hiện một phép mã hóa đơn giản, 
# trong đó đếm từ trái qua phải các ký tự giống nhau liên tiếp và viết số đếm trước ký tự đó.
# Ví dụ:  AACDDPQ được mã hóa thành 2A1C2D1P1Q
#         11111147g được mã hóa thành 6114171g
# Viết chương trình thực hiện thao tác mã hóa như trên.

# Input
# Dòng đầu ghi số bộ test. Mỗi dòng sau là một xâu ký tự, độ dài không quá 1000.

# Output
# Với mỗi bộ test, ghi ra xâu ký tự mã hóa tương ứng.

# Ví dụ

# Input               Output
# 3
# AACDDPQ             2A1C2D1P1Q
# 11111147g           6114171g
# 1111111111          101

for t in range(int(input())):
    s = input() + '!'
    cnt, ch = 0, s[0]
    for i in s:
        if i == ch:
            cnt += 1
        else:
            print(str(cnt) + ch, end='')
            cnt, ch = 1, i
    print()




