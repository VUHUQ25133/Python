# Cho dãy ký tự chuẩn P[] = “ABCDEFGHIJKLMNOPQRSTUVWXYZ_.”

# Phép mã hóa với khoảng cách K (0<K<28) được định nghĩa là:
# phép chuyển các ký tự s[i] thành ký tự P[(i+K)%28] trong dãy ký tự chuẩn P nói trên.
# Ví dụ với K = 3 thì ‘A’ chuyển thành ‘D’; ‘B’ chuyển thành ‘E’ và ‘.’ chuyển thành ‘C’.

# Cho số K và một xâu S (chỉ bao gồm các chữ cái thuộc P[], không có khoảng trống). 
# Hãy mã hóa xâu S theo quy tắc trên, sau đó đảo ngược thứ tự các chữ cái.

# Input
# Mỗi dòng ghi số K và xâu S.
# Input kết thúc khi K = 0.

# Output
# Ghi ra kết quả cho từng test.

# Ví dụ

# Input               Output
# 1 ABCD              EDCB
# 14 ROAD             ROAD
# 0

SS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True:
    str = input()
    if str == '0':
        break

    k, s = str.split()
    k = int(k)
    res = ''
    for i in s:
        j = SS.find(i)
        res += SS[(j + k) % 28]
    print(res[::-1])

