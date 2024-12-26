# Cho một số nguyên (có thể âm) không quá 100.000 chữ số. 
# Mỗi bước thực hiện thay thế số nguyên này bằng giá trị tổng chữ số của số đó. 
# Hỏi sau mấy bước thì số đó chỉ còn duy nhất 1 chữ số.

# Input
# Chỉ có duy nhất số nguyên N (không quá 100.000 chữ số)

# Output
# Ghi ra số bước cần thực hiện.

# Ví dụ

# Input       Output
# 10          1
# 919         3
# 6           1



def trans(s) :
    n = 0
    for i in s : n += ord(i) - ord('0')
    return str(n)

s = input()
d = 0
while(len(s) > 1) :
    s = trans(s)
    d += 1
print(d)