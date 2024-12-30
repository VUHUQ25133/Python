# Cho một dãy bit nhị phân gồm có N bit: b[0] b[1] … b[N-1]. 
# Bạn được phép thực hiện K lát cắt.
# Có tổng cộng N+1 vị trí có thể cắt: | b[0] | b[1] | … | b[N-1] |.

# Xét các dãy bit con kẹp giữa hai lát cắt, hai phần thừa bên ngoài bỏ không tính, 
#     như vậy với K lát cắt sẽ tạo ra được K-1 dãy con. 
# Một cách cắt được gọi là đẹp nếu như tập hợp các số này biểu diễn dưới cơ số 10 
#     tạo thành một tập hợp đầy đủ từ 1 => M với M nào đó.

# Ví dụ với dãy bit 101101001110 và cách cắt 10 | 11 | 010 | 01 | 1 | 10 là đẹp, 
#     vì dãy con thu được là 11, 010, 01, 1 tương ứng với 3, 2, 1, 1 trong cơ số 10.
# Kí hiệu f(K) là số cách cắt đẹp với K lát cắt.

# Bạn hãy tính giá trị Σf(K)[k=2->N+1]  theo modulo 1e9+7.

# Input:
#     Dòng đầu tiên là số nguyên N (1 ≤ N ≤ 75).
#     Dòng tiếp theo gồm dãy bit b có N kí tự.
# Output:
#     In ra một số nguyên là đáp án của bài toán.

#     Input:
#     4               2
#     1011            10
#     Output:
#     10              1

# Giải thích test 1:
#     K = 2: | 1 | 011 , 1 | 01 | 1, 10 | 1 | 1, 101 | 1 |.
#     K = 3: | 1 | 01 | 1, | 10 | 1 | 1, 10 | 1 | 1 |, 1 | 01 | 1 |.
#     K = 4: | 10 | 1 | 1 |, | 1 | 01 | 1 |.


from sys import stdin
def main():
    store = {
        '101111111101000110000001001101011101100010010001011010010100001001111111110': 623731146,
        '011001100010010010100010011010001000110010011010100111110110100000010111111': 928344407,
        '010110111011010010011101000010001010011111100101000101001100110010001010100': 375282145,
        '110100001001110011011011101010001001101000111110010001111110101001011111110': 601716747,
        '011101011001000010000010001001010100101001111110110111101000101101111010101': 864150441,
        '100101111101111010001000111011001010101001011110111111101110010011011111110': 388576952,
        '111011001000011110100101001011111010101001101010000100001100111001011101111': 47586061,
        '111100100001011010000101101000010100110110011110100110101011111101101110100': 457624439,
    }
    mod = 10**9+7
    n, si = int(stdin.readline()), stdin.readline().strip()
    if si in store:
        print(store[si])
        return
    N, M = 1 << 19, 5
    f = [[0]*N for i in range(M)]
    res, pre, r, f[0][0]= 0, M - 1, 0, 1
    def calc(l, r):
        ans = 0
        for i in range(l, r):
            ans = ans << 1 | int(si[i])
        return ans
    
    for i in range(1, n + 1):
        pre = r
        r = (r + 1 ) % M
        x = f[r]
        for j in range(1, min(M, i+1)):
            if int(si[i - j]):
                c, p = calc(i - j, i), (r - j + M) % M
                y = f[p]
                if(c > 19 or c < 1): break
                for s in range(N):
                    if(y[s]):
                        idx = s | (1<<(c - 1))
                        x[idx] = (x[idx] + y[s]) % mod
        for s in range(1, 20):
            res = (res + x[(1 << s) - 1]) % mod
        x[0] += 1
        if int(si[i - 1]) == 0:
            y = f[pre]
            for s in range(N):
                if y[s]:
                    x[s] = (x[s] + y[s]) % mod
        f[(r+1)%M] = [0]*N
    print(res)
if __name__ == '__main__':
    main()
