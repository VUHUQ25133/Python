# Cho xâu ký tự có độ dài n bao gồm các ký tự từ ‘a’, ‘b’, …, ‘z’ và các số từ 0 đến 9. 
# Nhiệm vụ của bạn là tìm số nhỏ nhất xuất hiện trong xâu. 
#     Ví dụ với xâu X[]=”12ab29cd19” ta có kết quả là 12.
# Input:
#     Dòng đầu tiên đưa vào T là số lượng bộ test.
#     Những dòng tiếp theo, mỗi dòng đưa vào T test. Mỗi test là một xâu ký tự thỏa mãn yêu cầu bài toán.
#     T, n thỏa mãn ràng buộc : 1≤T≤100; 1≤ n≤1e5;
#     Dữ liệu vào đảm bảo số lớn nhất cũng không quá 18 chữ số
# Output:
#     Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:

# Input:              Output:
# 2
# 12ab29cd19          12
# ab123gh456cd        123

t = int(input())
for i in range(t) :
    n = input()
    n = n + 'z'
    ans = 10 ** 20
    s = 0
    for i in range(len(n)) :
        if n[i].isalpha() :
            if i != 0 and n[i - 1].isdigit() : ans = min(ans, s)
            s = 0
        else : s = s * 10 + int(n[i])
    print(ans)