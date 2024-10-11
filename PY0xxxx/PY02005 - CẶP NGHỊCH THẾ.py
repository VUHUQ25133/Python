# Cho dãy số A[] gồm có N phần tử.
# Một cặp nghịch thế là một cặp số (u, v) sao cho u < v và A[u] > A[v]. 
# Nhiệm vụ của bạn là hãy đếm số lượng cặp nghịch thế trong dãy số A[] ban đầu.

# Input:
# Dòng đầu tiên là N (N ≤ 1000), số lượng phần tử trong dãy số ban đầu.
# Dòng tiếp theo gồm N số nguyên A[i] (1 ≤ A[i] ≤ 109).
# Output: 
# In ra một số nguyên là số lượng dãy nghịch thế tìm được.
# Ví dụ:
# Input:
# 5
# 2 4 1 3 5
# Output
# 3

# Giải thích test:
# Có 3 cặp nghịch thế là (2, 1), (4,1) và (4, 3).

n = int(input())
a = [int(i) for i in input().split()]
cnt = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            cnt += 1
print(cnt)
