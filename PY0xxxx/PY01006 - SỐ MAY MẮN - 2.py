# Một số được xem là số may mắn nếu chỉ có các chữ số 4 và 7. 
# Cho số nguyên dương N không quá 200 chữ số. Hãy kiểm tra xem N có phải số may mắn hay không.

# Input
# Dòng đầu ghi số bộ test (không quá 10).
# Mỗi test ghi số nguyên dương N không quá 200 chữ số.

# Output
# Với mỗi test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

# Ví dụ

# Input                               Output
# 3                                   
# 4477                                YES
# 44444487777777777                   NO
# 47474747474777777777777744444       YES

def checkLuckyNum(s):
    for i in range(len(s)):
        if s[i] != '4' and s[i] != '7':
            return 'NO'
    return 'YES'


for t in range(int(input())):
    s = input()
    print(checkLuckyNum(s))