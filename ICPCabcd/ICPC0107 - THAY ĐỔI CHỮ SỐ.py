# Cho hai số nguyên dương X1, X2. 
# Ta chỉ được phép thay đổi chữ số p thành chữ số q và ngược lại chữ. 
# Hãy đưa ra tổng nhỏ nhất và tổng lớn nhất các số X1 và X2 được tạo ra theo nguyên tắc kể trên.
# Input:
#     Dòng đầu tiên đưa vào số lượng bộ test T.
#     Những dòng kế tiếp đưa vào T bộ test. 
#     Mỗi bộ test gồm 3 dòng: dòng đầu tiên ghi lại chữ số p và chữ số q; hai dòng kế tiếp ghi lại các số X1 và X2 theo thứ tự.
#     T, X1, X2 thỏa mãn ràng buộc: 1≤ T ≤100; 0≤ X1, X2 ≤1e1000.
# Output:
#     Đưa ra kết quả mỗi test theo từng dòng.

# Input:
# 1
# 5 6
# 645
# 666
# Output:
# 1100  1312

for t in range(int(input())):
    n, m = input().split()
    ip = input().split()
    if len(ip) == 1:
        str1 = ip[0]
        str2 = input()
    else:
        str1, str2 = ip
    num1 = int(str1.replace(n, m)) + int(str2.replace(n, m))
    num2 = int(str1.replace(m, n)) + int(str2.replace(m, n))
    print(min(num1, num2), max(num1, num2))
