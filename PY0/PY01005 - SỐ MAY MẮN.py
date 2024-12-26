# Chữ số 4 và chữ số 7 được xem là các chữ số may mắn.
# Cho số nguyên dương N có không quá 18 chữ số. 
# Hãy đếm xem số chữ số 4 cộng với số chữ số 7 trong N có phải bằng 4 hay bằng 7 hay không.

# Input
# Chỉ có số N

# Output
# Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

# Ví dụ

# Input                   Output
# 40047                   NO
# 7747774                 YES
# 1000000000000000000     NO

s = input()
cnt = 0
for i in range(len(s)):
    if s[i] == '4' or s[i] == '7':
        cnt = cnt + 1
        
if cnt == 4 or cnt == 7:
    print('YES')
else:
    print('NO')