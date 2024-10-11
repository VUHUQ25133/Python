# Cho dãy số A[] gồm có N phần tử. 
# Nhiệm vụ của bạn là hãy tìm một số có tần số xuất hiện nhiều nhất, 
# yêu cầu lớn hơn N/2 lần xuất hiện trong dãy số.

# Input:
# Dòng đầu tiên là số lượng bộ test T (T ≤ 10).
# Mỗi test gồm số nguyên N (1≤ N ≤ 100000), số lượng phần tử trong dãy số ban đầu.
# Dòng tiếp theo gồm N số nguyên A[i] (1 ≤ A[i] ≤ 1 000 000).
# Output: 
# Với mỗi test in ra đáp án của bài toán trên một dòng. 
# Nếu có nhiều số cùng thỏa mãn thì in ra số nhỏ nhất.
# Nếu không tìm được đáp án, in ra “NO”.

# Ví dụ:

# Input                   Output
# 2
# 9                       4
# 3 3 4 2 4 4 2 4 4
# 8                       NO
# 3 3 4 2 4 4 2 4

for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    if len(a) == 1:
        print(a[0])
    else:
        m, ans, cnt = {}, a[0], 1
        for i in a:
            if i in m:
                m[i] += 1
                if m[i] > cnt:
                    ans, cnt = i, m[i]
            else:
                m[i] = 1
        if cnt * 2 > len(a):
            print(ans)
        else:
            print("NO")
