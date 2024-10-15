# Một số nguyên dương N được gọi là số Krish nếu tổng giai thừa các chữ số của N bằng chính nó. 
#     Ví dụ N = 145 = 1! + 4! + 5! là một số Krish. 
# Cho số nguyên dương N, hãy kiểm tra N có phải là một số Krish hay không? 
#     Đưa ra “Yes” nếu N là một số Krish, ngược lại đưa ra “No”.
# Input:
#     Dòng đầu tiên đưa vào T là số lượng bộ test.
#     Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
#     T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤1e8;
# Output:
#     Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input:  Output:
# 2
# 145     Yes
# 235     No

kr = [1]*10
for i in range(2, 10):
    kr[i] = kr[i-1]*i

for case in range(int(input())):
    num = input()
    s = sum(kr[int(i)] for i in num)
    print('Yes' if s == int(num) else 'No')
