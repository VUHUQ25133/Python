# Một số được gọi là số không giảm nếu không có cặp chữ số cạnh nhau (i, i+1) nào mà số thứ i lớn hơn số thứ i+1.
# Viết chương trình kiểm tra số nguyên dương có thỏa mãn là số không giảm hay không.

# InpuT
# Dòng đầu ghi số bộ test (không quá 10).
# Mỗi dòng ghi một số nguyên dương (không quá 500 chữ số).

# Output
# Ghi ra YES nếu đó là số không giảm. NO nếu ngược lại

# Ví dụ

# Input                           Output
# 2
# 12345678888888888888889         YES
# 65645645465754765876857685846   NO

def check(s):
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return 'NO'
    return 'YES'


for t in range(int(input())):
    s = input()
    print(check(s))