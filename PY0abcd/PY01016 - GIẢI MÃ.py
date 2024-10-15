# Cho một xâu ký tự độ dài không quá 100 chỉ bao gồm các chữ cái in hoa. 
# Người ta thực hiện mã hóa bằng cách đếm các ký tự cạnh nhau giống nhau 
# và viết số lượng phía sau các chữ cái đó.
# Ví dụ xâu AAECCCCGGGD thì được mã hóa thành A2E1C4G3D1

# Với giả thiết không có ký tự nào xuất hiện nhiều hơn 9 lần liên tiếp.
# Cho trước xâu kết quả mã hóa. Hãy khôi phục xâu ký tự ban đầu tương ứng.

# Input
# Dòng đầu ghi số bộ test. Mỗi bộ test ghi xâu mã hóa.

# Output
# Với mỗi test ghi ra xâu ký tự ban đầu.

# Ví dụ

# Input           Output
# 2
# A8              AAAAAAAA
# A2E1C4G3D1      AAECCCCGGGD

for t in range(int(input())):
    s = input()
    res = ''
    for i in range(0, len(s), 2):
        res += s[i] * int(s[i + 1])
    print(res)
