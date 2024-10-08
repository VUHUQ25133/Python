# Cho xâu ký tự S bao gồm các ký tự ‘A’,..,’Z’ và các chữ số ‘0’,...,’9’. 
# Nhiệm vụ của bạn in các ký tự từ ’A’,.., ‘Z’ trong S theo thứ tự từ điển 
# và nối với tổng các chữ số trong S ở cuối cùng. 
# Ví dụ S =”ACCBA10D2EW30” ta nhận được kết quả: “AABCCDEW6”.

# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T.
# Những dòng kế tiếp đưa vào T bộ test. Mỗi bộ test là một xâu ký tự S.
# T, S thỏa mãn ràng buộc: 1 ≤ T ≤ 100; 1 ≤ Length(S) ≤ 1e5.

# Output:
# Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:

# Input               Output: 
# 2
# AC2BEW3             ABCEW5
# ACCBA10D2EW30       AABCCDEW6

t = int(input())
for z in range(t) :
    a = input()
    d = 0
    s = ""
    for i in a :
        if i.isdigit() : d += int(i)
        else : s += i
    print(''.join(sorted(s)), d, sep = "")