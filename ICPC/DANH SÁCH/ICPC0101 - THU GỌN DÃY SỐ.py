# Cho dãy số A[] chỉ bao gồm các số nguyên dương. 
# Người ta thu gọn dần dãy số bằng cách loại bỏ các cặp phần tử kề nhau mà có tổng là chẵn. 
# Sau khi cặp phần tử đó bị loại ra thì dãy số được dồn lại. 
# Cứ tiếp tục như vậy cho đến khi không còn cặp phần tử nào kề nhau có tổng chẵn nữa.
# Hãy tính xem cuối cùng dãy A[] còn bao nhiêu phần tử.
# Input
#     Dòng đâu ghi số N là số phần tử của dãy (1 ≤ N ≤ 1e5).
#     Dòng tiếp theo ghi N số của dãy A (1 ≤ A[i] ≤ 100).
# Output
#     Ghi ra trên một dòng số phần tử còn lại trong dãy A[].

# Ví dụ
# Input                   Output
# 5
# 2 3 4 5 6               5

# 10
# 1 5 5 8 6 4 3 5 9 3     2

n = int(input())
list = [int(i) for i in input().split()]
i = 1
while i < len(list):
    if (list[i-1]+list[i]) % 2 == 0:
        list.pop(i)
        list.pop(i-1)
        if i > 1:
            i -= 1
    else:
        i += 1
print(len(list))
