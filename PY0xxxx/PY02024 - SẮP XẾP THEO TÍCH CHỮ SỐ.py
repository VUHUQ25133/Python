# Cho dãy số A[] có N phần tử đều là các số nguyên dương, không quá 6 chữ số.
# Hãy sắp xếp dãy số theo tích các chữ số tăng dần. 
# Nếu tích các chữ số bằng nhau thì số nào nhỏ hơn sẽ viết trước.
# Input
# Dòng đầu ghi số bộ test (không quá 10)
# Mỗi bộ test gồm 2 dòng:
# Dòng đầu là số N (N < 100)
# Dòng thứ 2 ghi N số của mảng A[], các số đều nguyên dương và không quá 9 chữ số.
# Output
# Với mỗi bộ test, ghi trên một dòng dãy số kết quả.

# Ví dụ
# Input
# 1
# 8
# 143 43 22 99 7 9 1111 10000000
# Output
# 10000000 1111 22 7 9 43 143 99

def mul(s):
    x = 1
    for i in s:
        x *= int(i)
    return x


for t in range(int(input())):
    n = int(input())
    a = input().split()
    a.sort(key=lambda s: (mul(s), int(s)))
    print(*a)

