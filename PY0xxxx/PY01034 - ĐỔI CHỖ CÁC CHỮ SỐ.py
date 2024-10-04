# Cho một số nguyên không âm N được biểu diễn như một xâu ký tự. 
# Hãy sử dụng nhiều nhất một phép đổi chỗ các chữ số trong N sao cho ta nhận được số lớn nhất nhỏ hơn N. 
# Phép biến đổi có số 0 cho số đầu tiên sẽ không được chấp nhận. 
# Ví dụ số N = 354 thì số lớn nhất nhỏ hơn N được tạo ra là 345. 
# Số 100 sẽ không có phép biến đổi vì số 010 có số 0 đứng đầu.
# Input:
# Dòng đầu tiên đưa vào số lượng test T (T≤100).
# Những dòng kế tiếp đưa vào các test. 
# Mỗi bộ test là một xâu ký tự bao gồm các ký tự số. Độ dài tối đa là 1000.
# Output:
# Với mỗi test in ra số nguyên lớn nhất tìm được trên một dòng. 
# Nếu không tồn tại đáp án, in ra -1.
# Ví dụ:
# Input       Output
# 4
# 354         345
# 999         -1
# 100         -1
# 11101       11011

t = int(input())
for k in range(t) :
	a = input()
	n, p , s = len(a), -1, '0'
	for i in range(n - 2, -1, -1) :
		if a[i] > a[i + 1] :
			p = i
			break
	if p == -1 :
		print(-1)
		continue
	q = p + 1
	for i in range(p + 2, n) :
		if a[i] > s and a[i] > a[p + 1] and a[i] < a[p] :
			s = a[i]
			q = i
	a = a[:p:] + a[q] + a[p + 1:q:] + a[p] + a[q + 1::]
	if a[0] == '0' : print(-1)
	else : print(a)
