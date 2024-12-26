# Con số duyên nợ là con số có chữ số đầu và chữ số cuối giống nhau.
# Viết chương trình kiểm tra xem một số nguyên dương n ghi trong hệ thập phân có chữ số đầu và chữ số cuối giống nhau không?
# Input
#     Gồm nhiều dòng, mỗi dòng chứa một số nguyên dương n ghi ở hệ thập phân.
#     Giới hạn:1 ≤ n ≤ 10^100
# Output
#     Ứng với mỗi số nguyên dương n, ghi ra trên một dòng là YES nếu số n tương ứng có chữ số đầu và chữ số cuối giống nhau, NO nếu ngược lại.
# Ví dụ
# Input:          Output:
# 2
# 12345           NO
# 123451          YES

for case in range(int(input())):
    str = input()
    print('YES' if str[0] == str[-1] else 'NO')
