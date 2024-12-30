# Cho dãy số A[] gồm có N phần tử. 
# Tổng tuyệt đối của một dãy số là giá trị tuyệt đối của tổng tất cả các phần tử 
#     (tính tổng xong mới lấy giá trị tuyệt đối).
# Độ yếu của dãy số A[] được tính bằng giá trị lớn nhất 
#   trong số các tổng tuyệt đối của tất cả các dãy con liên tiếp của A.
# Bạn hãy xác định số thực X sao cho dãy số A[1]-X, A[2]-X, …, A[N]-X có độ yếu là nhỏ nhất.
# Input:
#     Dòng đầu tiên gồm số nguyên N (1 ≤ N ≤ 100 000).
#     Dòng tiếp theo gồm N số nguyên A[i] (-10 000 ≤ A[i] ≤ 10 000).
# Output: 
#     In ra số độ yếu của dãy A[1]-X, A[2]-X, …, A[N] - X.
#     Kết quả ghi ra với 6 chữ số phần thập phân. 

# Ví dụ:


#     Input:          Input:          Input: 
#     3               4               10
#     1 2 3           1 2 3 4         1 10 2 9 3 8 4 7 5 6
#     Output:         Output:         Output:
#     1.000000        2.000000        4.500000

# Giải thích test 1: Với X = 1, dãy số mới thu được là -1, 0, 1. Dãy số này có độ yếu bằng 1.
# Giải thích test 2: Với X = 2.5, dãy số mới là -1.5 -0.5 0.5 1.5. Độ yếu của dãy số bằng 2 (|-1.5-0.5| = |0.5+1.5| = 2).

from sys import stdin
# stdin = open("d:/code/in.txt")
n = int(stdin.readline())
a = [i for i in map(float, stdin.readline().split())]

def weak(X):
    pos, neg, prep, pren = 0.0, 0.0, 0.0, 0.0
    for i in a:
        b = i - X
        prep += b
        pren += b
        if prep > 0.0:
            if prep > pos: pos = prep
        else: prep = 0.0
        if pren < 0.0:
            if pren < neg: neg = pren
        else: pren = 0.0
    return round(pos, 6), round(-neg, 6)
        
def main():
    l, r = min(a), max(a)
    pos, neg = 1.0, 0.0
    while pos != neg:
        mid = (l + r) / 2
        pos, neg = weak(mid)
        if pos > neg: l = mid
        else: r = mid
    print(f'{pos:.6f}')
main()
