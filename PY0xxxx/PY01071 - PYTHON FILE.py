# Một file code Python sẽ có phần mở rộng là .py.
# Trong hệ điều hành Windows tên file sẽ không phân biệt chữ hoa, chữ thường. 
# Hãy kiểm tra xem tên file có đúng là file code Python hay không. 
# Input
# Chỉ có một dòng ghi tên file S (1 ≤ |S| ≤ 128). 
# Tên file chỉ chứa các ký tự ‘a’-‘z’, ‘A’-‘Z’, ‘.’ và dấu ‘_’.
# Output
# In ra "yes" hoặc "no" tùy thuộc kết quả kiểm tra.

# abc.py ==> yes

# abc.bin ==> no

s = input().lower()
print('yes' if len(s) >= 3 and s[-3:] == '.py' else 'no')