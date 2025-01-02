# PY/BIẾN VÀ KIỂU DỮ LIỆU ĐƠN GIẢN/PY01013 - ƯỚC SỐ CHUNG NGUYÊN TỐ.py
```py
# Cho hai số nguyên dương a và b. 
# Hãy kiểm tra xem ước số chung lớn nhất của hai số này có tổng chữ số là nguyên tố hay không.
# Ví dụ a = 42, b = 28, ước số chung lớn nhất = 14. 
# Tổng chữ số của ước số chung là 1+4=5 là một số nguyên tố.

# Input
#       Dòng đầu ghi số bộ test. 
#       Mỗi test ghi trên một dòng hai số nguyên dương a,b (không quá 6 chữ số)
# Output
#       Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

    # Input           Output
    # 3
    # 28 42           YES
    # 123 18          YES
    # 550 55          NO

import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return n > 1

for t in range(int(input())):
    a, b = [int(i) for i in input().split()]
    if isPrime(sum(int(i) for i in str(math.gcd(a, b)))):
        print('YES')
    else:
        print('NO')
```
# PY/BIẾN VÀ KIỂU DỮ LIỆU ĐƠN GIẢN/PY01014 - CHIA HẾT CHO K.py
```py
# Cho ba số nguyên dương a, K, N. 
# Hãy liệt kê tất cả các số nguyên dương b thỏa mãn cả hai điều kiện:
#       a + b ≤ N
#       a + b chia hết cho K
# Input
#       Chỉ có một dòng ghi ba số nguyên dương theo thứ tự a, K, N (không quá 9 chữ số).
# Output
#       Ghi ra lần lượt các số b tìm được theo thứ tự tăng dần.
#       Nếu không tìm được số nào in ra -1

    # Input           Output
    # 10 1 10         -1
    # 10 6 40         2 8 14 20 26

a, k, n = [int(i) for i in input().split()]
b1 = (int(a / k) + 1) * k - a
b2 = int(n / k) * k - a
if b1 <= b2:
    for i in range(b1, b2 + 1, k):
        print(i, end=' ')
else:
    print(-1)
```
# PY/BIẾN VÀ KIỂU DỮ LIỆU ĐƠN GIẢN/PY01005 - SỐ MAY MẮN.py
```py
# Chữ số 4 và chữ số 7 được xem là các chữ số may mắn.
# Cho số nguyên dương N có không quá 18 chữ số. 
# Hãy đếm xem số chữ số 4 cộng với số chữ số 7 trong N có phải bằng 4 hay bằng 7 hay không.

# Input: Chỉ có số N
# Output: Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

    # Input                   Output
    # 40047                   NO
    # 7747774                 YES
    # 1000000000000000000     NO

s = input()
cnt = 0
for i in range(len(s)):
    if s[i] == '4' or s[i] == '7':
        cnt += 1
        
if cnt == 4 or cnt == 7:
    print('YES')
else:
    print('NO')
```
# PY/BIẾN VÀ KIỂU DỮ LIỆU ĐƠN GIẢN/PY01053 - SỐ CHIA HẾT CHO 3.py
```py
# Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
# Hãy kiểm tra xem N có chia hết cho 3 hay không.
# Input
#       Dòng đầu ghi số bộ test (không quá 20).
#       Mỗi test ghi số N (không quá 500 chữ số)
# Output
#       Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Input                   Output
# 2
# 12341                   NO
# 123456789123456789      YES

for t in range(int(input())):
    n = int(input())
    print('YES' if n % 3 == 0 else 'NO')
```
# PY/BIẾN VÀ KIỂU DỮ LIỆU ĐƠN GIẢN/PY01038 - KIỂM TRA CHIA HẾT CHO 7.py
```py
# Cho một số nguyên dương N. 
# Mỗi bước bạn thực hiện tính tổng của N với giá trị số đảo ngược của N. 
# Bạn sẽ dừng lại khi gặp giá trị chia hết cho 7 hoặc khi đã thực hiện quá 1000 bước lặp.
# Hãy tính giá trị chia hết cho 7 tìm được theo thủ tục trên,
#       hoặc ghi ra -1 nếu không thể tìm ra đáp án.

# Input:
#       Dòng đầu ghi số bộ test (không quá 1000).
#       Mỗi test ghi số N (1 ≤ N ≤ 1e18)
# Output:
#       Ghi ra giá trị chia hết cho 7 đầu tiên tìm được. 
#       Hoặc số -1 nếu không thể tìm được đáp án.

    # Input           Output
    # 5
    # 1               77
    # 2               77
    # 3               9447438
    # 4               77
    # 999999          999999

# Giải thích test 1: 1 => 2 => 4 => 8 => 16 => 77

def solve(n):
    for i in range(1000):
        if n % 7 == 0:
            return n
        rev_n = int(str(n)[::-1])
        n += rev_n
    return -1

for t in range(int(input())):
    n = int(input())
    print(solve(n))
```
# PY/BIẾN VÀ KIỂU DỮ LIỆU ĐƠN GIẢN/PY01041 - SỐ TĂNG GIẢM.py
```py
# Một số nguyên dương được gọi là số tăng giảm nếu thỏa mãn các điều kiện:
#   Có từ 3 chữ số trở lên
#   Tìm ra một vị trí trong dãy chữ số sao cho từ bên trái đến vị trí đó thỏa mãn thứ tự tăng dần (tăng chặt) 
#       còn từ vị trí đó đến hết thì thỏa mãn thứ tự giảm dần (giảm chặt).
# Viết chương trình kiểm tra một số có phải số tăng giảm hay không.

# Input
#       Dòng đầu ghi số bộ test. 
#       Mỗi bộ test viết trên một dòng số nguyên dương N không quá 18 chữ số
# Output
#       Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

    # Input       Output
    # 3
    # 12342       YES
    # 23342       NO
    # 5678961     YES

def solve(s):
    if len(s) < 3:
        return 'NO'
    arr = list(int(i) for i in s)
    up = True
    for i in range(1, len(arr)):
        if up and arr[i] <= arr[i - 1]:
            up = False
        elif not up and arr[i] >= arr[i - 1]:
            return 'NO'
    return 'YES'

for t in range(int(input())):
    s = input()
    print(solve(s))
```
# KIỂM TRA HỆ CƠ SỐ 5.py
```py
# Hệ cơ số 5 chỉ biểu diễn các số sử dụng chữ số là 0, 1, 2, 3, 4 và có tổng chữ số = 5.
# Nhập vào dãy biểu diễn không quá 18 ký tự, 
# hãy kiểm tra xem dãy biểu diễn nào là đúng với hệ cơ số 55.

# Input: Dòng đầu là số bộ test, mỗi dòng tiếp theo ghi một dãy biểu diễn cần kiểm tra.
# Output: Nếu đúng in ra YES, nếu sai in ra NO.

    # Input       Output
    # 3
    # 1214AB      NO
    # 102101      YES
    # 22222222    YES

def check(s):
    sum = 0
    for i in s:
        if s < '0' or i > '4':
            return 'NO'
        sum += int(i)
    if sum != 5: return 'NO'
    return 'YES'

for t in range(int(input())):
    print(check(input()))
```
# TÍCH CHỮ SỐ VỊ TRÍ LẺ.py
```py
# Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
# Hãy tính tích các chữ số vị trí lẻ của N. Chú ý bỏ qua các chữ số 0 nếu có. 

# Input
#       Dòng đầu ghi số bộ test (không quá 20).
#       Mỗi test ghi số N (không quá 500 chữ số).
# Output
#       Với mỗi bộ test, ghi ra kết quả tính được.
#       Dữ liệu vào đảm bảo kết quả tích các chữ số sẽ không vượt quá 18 chữ số.  

    # Input               Output
    # 2
    # 123410              3
    # 123456789123456789  362880

for t in range(int(input())):
    s = input()
    res = 1
    for i in range(0, len(s), 2):
        if int(s[i]) != 0:
            res *= int(s[i])
    print(res)
```
# Đọc flights.csv
```py
# Đọc file flights.csv và in ra số dòng, số cột của file
# Input: không có
# Output: số hàng và số cột, cách nhau một khoảng trắng
import csv

with open('flights.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)  # Chuyển dữ liệu trong file thành danh sách các dòng
    num_rows = len(rows) - 1  # Trừ đi dòng tiêu đề
    num_cols = len(rows[0]) if rows else 0  # Số cột dựa trên dòng đầu tiên

print(num_rows, num_cols)

```
# File Json1
```py
# File json với định dạng đã cho. 
# In ra giá trị của max và min, cách nhau bởi dấu trắng
import json

with open('Json1.json', 'r') as file:
    data = json.load(file)

max_value = data.get('max')
min_value = data.get('min')

print(max_value, min_value)
```
# Flight 2
```py
# in ra số dòng và số cột của file json filght
import json

with open('Flight2.json', 'r') as file:
    data = json.load(file)

num_rows = len(data)
num_cols = len(data[0]) if num_rows > 0 else 0

print(num_rows, num_cols)
```
# PY/BIẾN VÀ KIỂU DỮ LIỆU ĐƠN GIẢN/PY01020 - SỐ PHÁT LỘC.py
```py
# Một số kết thúc bởi hai chữ số 86 được gọi là số phát lộc. 
# Cho một số nguyên dương không quá 500 chữ số, hãy kiểm tra có phải số phát lộc hay không.

# Input
#       Dòng đầu ghi số bộ test. 
#       Mỗi bộ test ghi số nguyên dương cần kiểm tra (không quá 500 chữ số)
# Output
#       Ghi ra kết quả kiểm tra tương ứng (YES hoặc NO)

    # Input       Output
    # 3
    # 1539786     YES
    # 1234789     NO
    # 8686        YES

def check(s):
    l = len(s)
    if s[l - 2] == '8' and s[l - 1] == '6':
        return 'YES'
    else:
        return 'NO'
    # return 'YES' if s[-2:] == '86' else 'NO'  

for t in range(int(input())):
    s = input()
    print(check(s))
```
# Tích vị trí chẵn chia tổng lẻ
```py
# input:
# dòng đầu là bộ test
# các dòng sau mỗi dòng là 1 số có độ dài <= 100
# output:
# lấy tích các số vị trí lẻ chia tổng vị trí chẵn, nếu tổng 0 thì in ra INVALID
# kết quả làm tròn 6 chữ số sau ","
def calc(s):
    tich = 1
    tong = 0 

    for i in range(len(s)):
        if i % 2 == 0:
            tich *= int(s[i])
        else:
            tong += int(s[i])

    if tong == 0:
        return "INVALID"
    else:
        return f"{tich/tong:.6f}"

for t in range(int(input())):
    s = input()
    print(calc(s))
```
