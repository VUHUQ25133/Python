# Ai cũng biết số lộc phát theo quan niệm người Việt là số chỉ chứa các chữ số 6 và/hoặc 8. 
# Người ta định nghĩa thêm “số lộc phát đẹp” là số thỏa mãn tính chất nếu xét từ trái qua phải 
# thì nó được ghép bởi 3 số: 6; 68; 688. Không nhất thiết phải dùng đủ cả 3 số này.
# Ví dụ: các số 666666; 668688; 688688688 là các số lộc phát đẹp.

# Cho trước một số nguyên dương N không quá 100 chữ số. 
# Hãy kiểm tra xem đó có phải là số lộc phát đẹp hay không.

# Input
# Chỉ có một dòng ghi số N có không quá 100 chữ số

# Output
# Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

# Ví dụ

# 666666  ==> YES
# 668688  ==> YES
# 886236  ==> NO

def check(s) :
    if s[0] != '6' : return 0
    for i in range(len(s)) :
        if s[i] != '6' and s[i] != '8' : return 0
        if i >= 2 and s[i - 2:i + 1:] == '888' : return 0
    return 1

s = input()
if check(s) == 1 : print("YES")
else : print("NO")