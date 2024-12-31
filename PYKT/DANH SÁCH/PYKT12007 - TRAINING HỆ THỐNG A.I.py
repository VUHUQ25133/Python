# Một hệ thống nhận diện khuôn mặt gồm có N module. 
#     Mỗi module có khả năng hoạt động chính xác bằng P[i]. 
# Xác suất hoạt động chính xác của hệ thống được xác định bằng tích của tất cả các module.
#     Để tăng độ chính xác của hệ thống, bạn phải thực hiện train dữ liệu cho mỗi module. 
# Tuy nhiên, việc này mất rất nhiều thời gian và bạn chỉ có tổng cộng U đơn vị thời gian. 
#     Train một model trong X đơn vị thời gian, độ chính xác của module này tăng lên thêm X (tối đa là bằng 1).
# Bạn hãy xác định xem sau khi training, độ chính xác lớn nhất mà hệ thống đạt được là bao nhiêu?

# Input:
#     Dòng đầu tiên là số lượng bộ test T (1 ≤ T ≤ 100).
#         Mỗi test gồm số nguyên dương N (1 ≤ N ≤ 50).
#     Dòng tiếp theo là số thực U.
#     Dòng cuối gồm N số thực P[i] (0 ≤ P[i] ≤ 1).
# Output: Với mỗi test in ra trên một dòng đáp án tìm được với độ chính xác 10^-6.

# Ví dụ:

#     Input                           Output
#     2
#     4                               1.000000
#     1.4000                          0.250000
#     0.5000 0.7000 0.8000 0.6000
#     2
#     1.0000
#     0.0000 0.0000

for t in range(int(input())):
    n = int(input())
    s = float(input())
    arr = list(map(float, input().split()))
    a = {}
    for i in arr:
        if a.get(i) is None: a[i] = 1
        else: a[i]+=1
    a = [[i, a[i]] for i in sorted(a)]
    while len(a)>1:
        dis = a[1][0]-a[0][0]
        if s>dis*a[0][1]:
            s-=dis*a[0][1]
            a[1][1] += a[0][1]
            a.pop(0)
        else: break
    a[0][0] += s/a[0][1]
    ans = 1
    for i in a:
        ans*=i[0]**i[1]
    print(f'{min(1, ans):.6f}')
