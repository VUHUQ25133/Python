# Cho hai file văn bản DATA1.in và DATA2.in.
# Một từ được định nghĩa là một dãy ký tự liên tiếp 
#   không có khoảng trống, dấu tab hay dấu xuống dòng. 
# Tạm thời chưa xét đến các dấu câu trong bải toán này.
# Hãy viết chương trình liệt kê tập hợp các từ có mặt trong file DATA1.in 
#   nhưng không có trong file DATA2.in và ngược lại.
#       Các từ được chuyển hết về dạng chữ thường trước khi so sánh. 
#           Kết quả cần liệt kê theo thứ tự từ điển.

# Input
#   Hai file văn bản DATA1.in và DATA2.in, có không quá 200 dòng.
# Output
#       Dòng 1 ghi các từ khác nhau có mặt trong file DATA1.in nhưng không có trong file DATA2.in.
#       Dòng 2 ghi các từ khác nhau có mặt trong file DATA2.in nhưng không có trong file DATA1.in.

# DATA1.in                             Output
#     lap trinh huong doi tuong           c++ doi ngon ngu tuong
#     ngon ngu lap trinh C++              ban co phan thanh
# DATA2.in
#     lap trinh co ban
#     lap trinh huong thanh phan


with open("DATA1.in") as f: set1 = set(f.read().lower().split())
with open("DATA2.in") as f: set2 = set(f.read().lower().split())
print(' '.join(sorted(set1.difference(set2))))
print(' '.join(sorted(set2.difference(set1))))
