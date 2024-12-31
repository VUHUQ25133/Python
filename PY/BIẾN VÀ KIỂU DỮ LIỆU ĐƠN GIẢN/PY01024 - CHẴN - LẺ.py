# Cho số nguyên dương N. 
# Hãy kiểm tra xem N có thỏa mãn đồng thời hai tính chất sau đây hay không?

# Tổng chữ số của N chia hết cho 10
# Các chữ số cạnh nhau đều khác nhau đúng 2 đơn vị

# Input
# Dòng đầu ghi số bộ test. Mỗi bộ test ghi trên một dòng số nguyên dương N. N có ít nhất 3 chữ số nhưng không quá 18 chữ số.

# Output
# Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

# Ví dụ

# Input       Output
# 3
# 1353        NO
# 246864      YES
# 123435      NO

def check(s):
    if sum(int(i) for i in s) % 10 != 0:
        return 'NO'
    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i + 1])) != 2:
            return 'NO'
    return 'YES'


for t in range(int(input())):
    s = input()
    print(check(s))