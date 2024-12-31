# Cho N xâu S[1], S[2], …, S[N] có độ dài bằng nhau. 
# Mỗi bước, với xâu T, bạn được phép xoay vòng 1 kí tự, tức lấy kí tự đầu tiên của T rồi chuyển xuống cuối. 
#     Ví dụ xâu “cool” sẽ chuyển thành “oolc”.
# Bạn cần phải xoay N xâu sao cho tất cả chúng đều giống nhau. 
# Hãy xác định số bước ít nhất để hoàn thành được công việc này?
# Input:
#     Mỗi test bắt đầu bởi số nguyên N (1 ≤ N ≤ 50).
#     N dòng tiếp theo, mỗi dòng gồm xâu S[i] có độ dài không quá 50.
# Output: 
#     Với mỗi test, in ra số bước ít nhất tìm được, nếu không thể biến đổi, hãy in ra “NO”.

# Test ví dụ:

#             Test 1      Test 2      Test 3      Test 4
# Input:      4           2           3           3
#             xzzwo       molzv       kc          aa
#             zwoxz       lzvmo       kc          aa
#             zzwox                   kc          ab
#             xzzwo                   
# Output:     5           2           0           -1

a, n = [], int(input()) 
for i in range(n): a.append(input())
def turn(des, src):
    if des == src: return 0
    for i in range(len(des)):
        src = src[1:] + src[0]
        if src == des: return i+1
    return -1
ans = 10**5
check = True
for i in range(n):
    cnt = 0
    for j in range(n):
        if i!=j:
            num = turn(a[i], a[j])
            if num == -1:
                check = False
                break
            else: cnt += num
    ans = min(ans, cnt)
if check: print(ans)
else: print(-1)
