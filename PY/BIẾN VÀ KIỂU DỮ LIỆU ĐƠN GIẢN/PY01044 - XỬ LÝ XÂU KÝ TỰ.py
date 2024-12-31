# Trong lập trình cơ bản, một từ được hiểu là 
# một dãy ký tự liên tiếp không chứa khoảng trống, dấu tab hoặc dấu xuống dòng.

# Viết chương trình nhập hai dòng ký tự và hiển thị hợp và giao của hai tập từ tương ứng. 
# Các từ trong tập từ không được phép trùng nhau, mỗi từ chỉ liệt kê một lần và theo đúng thứ tự từ điển. 
# Các từ đều được chuyển hết về chữ viết thường. 

# Input
# Chỉ có 2 dòng, mỗi dòng có độ dài không quá 1000 ký tự.

# Output
# Dòng 1 ghi hợp của 2 tập từ theo thứ tự từ điển
# Dòng 2 ghi giao của 2 tập từ theo thứ tự từ điển.

# Ví dụ

# Input
# Lap trinh huong doi tuong
# Ngon ngu lap trinh C++

# Output
# c++ doi huong lap ngon ngu trinh tuong
# lap trinh

a = [i.lower() for i in input().split()]
b = [i.lower() for i in input().split()]
m1, m2, m3 = {}, {}, {}

for i in a:
    m1[i] = 1
    m2[i] = 1
for i in b:
    m1[i] = 1
    m3[i] = 1
    
for i in sorted(m1):
    print(i, end=' ')
print()

for i in sorted(m2):
    if i in m3:
        print(i, end=' ')