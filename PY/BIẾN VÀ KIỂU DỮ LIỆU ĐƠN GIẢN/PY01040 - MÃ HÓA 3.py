# Cho một xâu ký tự. 
# Quá trình mã hóa D - R - M sẽ trải qua ba bước Chia (Divide), Xoay (Rotate) và Trộn (Merge). 

# Ví dụ với xâu: EWPGAJRB quá trình này sẽ diễn ra như sau:

# Devide: Xâu ban đầu được chia thành 2 nửa: “EWPG” và “AJRB”.

# Rotate: Với mỗi nửa, tính toán giá trị xoay của nó bằng cách tính tổng giá trị các ký tự. 
# (A = 0; B = 1; … Z = 25).  
# Giá trị xoay của “EWPG” là 4 + 22 + 15 + 6 = 47. 
# Tiến hành xoay xâu  “EWPG”  đi 47 ký tự (tính cả bước chuyển từ Z về A nếu cần) ta sẽ được xâu: “ZRKB”. 
# Tương tự, “AJRB” được chuyển thành “BKSC”

# Merge: Trong bước này, mỗi ký tự trong xâu thứ nhất sẽ được xoay theo giá trị của ký tự ở vị trí tương ứng trong xâu thứ 2. 
# Trong ví dụ trên, chữ Z trong xâu thứ nhất sẽ xoay theo giá trị B, tức là 1 vị trí. 
# Do đó sẽ chuyển thành chữ A. Tiếp tục thực hiện với các ký tự tiếp theo ta sẽ có kết quả là “ABCD”.

# Cho một xâu ký tự chỉ bao gồm các chữ cái in hoa với số lượng ký tự là chẵn, 
# bạn hãy tìm xâu mã hóa DRM tương ứng.

# Input
# Dòng đầu ghi số bộ test T (T≤30).
# Mỗi bộ test ghi trên một dòng xâu ký tự cần mã hóa, chỉ gồm các chữ cái in hoa, độ dài là chẵn và không quá 15000 ký tự.
# Output
# Với mỗi test in ra trên một dòng kết quả mã hóa DRM tương ứng.
# Ví dụ
# Input                           Output
# 3
# EWPGAJRB                        ABCD
# BB                              E
# TPQJDRJWSQXGRRIPXFMINTELHBJA    FIRSTDATAFILEV

def Try(s) :
	d = 0
	x = ''
	for i in s :
		d += ord(i) - ord('A')
	for i in s :
		x += chr(((ord(i) - ord('A') + d) % 26 + ord('A')))
	return x
t = int(input())
for k in range(t) :
	s, x = input(), ''
	n = int(len(s) / 2)
	a, b = s[:n:], s[n::]
	a = Try(a)
	b = Try(b)
	for i in range(n) :
		x += chr(((ord(a[i]) - 2 * ord('A') + ord(b[i])) % 26 + ord('A')))
	print(x)