# Hãy liệt kê tất cả các xâu ký tự có độ dài không quá N, chỉ tạo bởi các ký tự A, B, C và 
# thỏa mãn các điều kiện sau:
# Chứa cả ba ký tự A, B, C
# Số ký tự A không nhiều hơn số ký tự B, số ký tự B không nhiều hơn số ký tự C
# Input
# Chỉ có một dòng ghi số N, không quá 12.
# Output
# Ghi ra lần lượt các xâu thỏa mãn theo thứ tự độ dài từ ngắn nhất đến dài nhất.
# Nếu có cùng độ dài thì ghi theo thứ tự từ điển.
# Mỗi xâu ghi trên một dòng.

# Ví dụ

# Input
# 4
# Output
# ABC ("\n") ACB ("\n") BAC ("\n") BCA ("\n") CAB ("\n") CBA ("\n")
# ABCC ("\n") ACBC ("\n") ACCB ("\n") BACC ("\n") BCAC ("\n") BCCA ("\n") CABC ("\n") CACB ("\n") CBAC ("\n") CBCA ("\n") CCAB ("\n") CCBA

def Try(s, n, a, b, c):
    if len(s) == n and a > 0  and a <= b and b <= c:
        print(s)
    if len(s) < n:
        Try(s + 'A', n, a + 1, b, c)
        Try(s + 'B', n, a, b + 1, c)
        Try(s + 'C', n, a, b, c + 1)


n = int(input())
for i in range(3, n + 1):
    Try('', i, 0, 0, 0)