# Cho dãy số A[] có N phần tử. 
# Với mỗi vị trí thứ i trong dãy, hãy tính độ dài của đoạn liên tiếp tính từ i trở về phía trước 
# mà các giá trị đều nhỏ hơn hoặc bằng A[i].

# Input: Dòng đầu ghi số bộ test (không quá 10). Mỗi test có 2 dòng.
#     Dòng đầu tiên gồm 1 số nguyên N (1 ≤ N ≤ 1e5).
#     Dòng tiếp theo gồm N số nguyên A1, A2, …, AN (1 ≤ A[i] ≤ 1e6).
# Output
#     Với mỗi bộ test, in ra dãy kết quả trên một dòng.
# Ví dụ:
# Input
# 1
# 7
# 100 80 60 70 60 75 85
# Output
# 1 1 1 2 1 4 6

for t in range(int(input())):
    n = int(input())
    list = [int(i) for i in input().split()]
    st, res = [], [0] * n
    for i in range(n):
        while len(st) > 0 and list[st[-1]] <= list[i]:
            st.pop()
        res[i] = i + 1 if len(st) == 0 else i - st[-1]
        st.append(i)
    print(*res)
