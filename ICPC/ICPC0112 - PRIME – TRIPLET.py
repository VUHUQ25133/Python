# Bộ ba số nguyên tố được gọi là Prime-Triplet nếu nó là bộ ba số nguyên tố 
#     dưới dạng (p, p+2, p+6) hoặc (p, p+4, p+6), trong đó p là một số nguyên tố. 
#     Ví dụ các bộ ba số (5, 7, 11) hoặc (7, 11, 13) đều là các Prime-Triplet. 
# Cho số tự nhiên N, nhiệm vụ của bạn là đếm số các Prime-Triplet nhỏ hơn N.      

# Input:
#     Dòng đầu tiên đưa vào T là số lượng bộ test.
#     Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
#     T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤1e6;
# Output:
#     Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input   Output
# 2
# 15      2
# 25      5

MAX = int(1e6+1)

prime = [1]*int(MAX)
prime[0] = prime[1] = 0
for i in range(1000):
    if prime[i]:
        for j in range(i*i, MAX, i):
            prime[j] = 0

for case in range(int(input())):
    cnt = 0
    for i in range(int(input())-5):
        if prime[i] and prime[i+6]:
            if prime[i+2] or prime[i+4]:
                cnt += 1
    print(cnt)
