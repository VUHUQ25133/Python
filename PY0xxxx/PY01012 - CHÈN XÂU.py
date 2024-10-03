# Cho xâu S1 và xâu S2, độ dài không quá 100.
# Hãy chèn xâu S2 vào vị trí p trong xâu S1 (vị trí ký tự đầu tiên là vị trí 1).

# Input:
# Dòng thứ nhất ghi xâu S1
# Dòng thứ hai ghi xâu S2
# Dòng thứ ba ghi số p (giá trị p đảm bảo nằm trong phạm vi xâu S1)

# Output:
# Ghi ra kết quả.

# Ví dụ:

# Input                   
# mon thcs2 hoc de
# ngon ngu C.
# 1

# Output
# ngon ngu C.mon thcs2 hoc de

S1 = input()
S2 = input()
p = int(input())

result = S1[:p-1] + S2 + S1[p-1:]
print(result)
