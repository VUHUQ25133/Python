# Cho xâu ký tự có độ dài n bao gồm các ký tự từ ‘a’, ‘b’, …, ‘z’ và các số từ 0 đến 9. 
# Nhiệm vụ của bạn là tìm số lớn nhất xuất hiện trong xâu. 
#     Ví dụ với xâu X[]=”12ab29cd19” ta có kết quả là 29.
# Input:
#     Dòng đầu tiên đưa vào T là số lượng bộ test.
#     Những dòng tiếp theo, mỗi dòng đưa vào T test. Mỗi test là một xâu ký tự thỏa mãn yêu cầu bài toán.
#     T, n thỏa mãn ràng buộc : 1≤T≤100; 1≤ n≤1e5;
#     Dữ liệu vào đảm bảo số lớn nhất cũng không quá 18 chữ số
# Output:
#     Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input:          Output:
# 2
# 12ab29cd19      29
# ab123gh456cd    456

import re

for t in range(int(input())):
    print(max(int(i) for i in re.findall(r'\d+', input())))
