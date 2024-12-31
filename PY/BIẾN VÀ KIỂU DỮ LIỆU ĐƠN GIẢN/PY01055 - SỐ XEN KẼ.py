# Một số được gọi là xen kẽ nếu thỏa mãn cả ba tính chất sau:
# Số chữ số là số lẻ
# Chữ số đầu tiên khác chữ số thứ hai.
# Các số ở vị trí đầu tiên, vị trí thứ 3, vị trí thứ 5…  và vị trí cuối cùng có giá trị bằng nhau
# Viết chương trình kiểm tra một số có phải xen kẽ hay không.

# Input
# Dòng đầu ghi số bộ test (không quá 10).
# Mỗi bộ test viết trên một dòng số cần kiểm tra, không quá 500 chữ số.

# Output
# Với mỗi bộ test viết ra YES hoặc NO tùy thuộc kết quả kiểm tra

# Ví dụ
# Input           Output
# 2
# 2324272921262   YES
# 13141516        NO

def check(s):
    if len(s) % 2 == 0 or s[0] == s[1]:
        return 'NO'
    for i in range(2, len(s), 2):
        if s[i] != s[0]:
            return 'NO'
    return 'YES'


for t in range(int(input())):
    print(check(input()))