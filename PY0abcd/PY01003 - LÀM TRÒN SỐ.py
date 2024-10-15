# Cho số nguyên dương không quá 9 chữ số. Hãy làm tròn số N theo quy tắc sau:

# Nếu N>10, làm tròn đến số hàng chục gần nhất
# Sau đó nếu kết quả lớn hơn 100 thì làm tròn đến số hàng trăm gần nhất
# Sau đó nếu kết quả lớn hơn 1000 thì làm trong đến số hàng nghìn gần nhất
# Cứ tiếp tục như vậy …
# Chú ý: Giá trị 5 sẽ được làm tròn lên.

# Input
# Dòng đầu ghi số bộ test (không quá 100)
# Mỗi bộ test ghi số N trên một dòng (N nguyên dương và không quá 9 chữ số)

# Output
# Với mỗi test, ghi ra kết quả làm tròn tương ứng trên một dòng.

# Ví dụ
# Input           Output
# 7
# 15              20
# 14              10
# 5               5
# 99              100
# 12345678        10000000
# 44444445        50000000
# 1445            2000

for t in range(int(input())):
    arr = list(int(i) for i in input())
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] >= 5:
            arr[i - 1] = arr[i - 1] + 1
        arr[i] = 0
    if arr[0] == 10:
        arr[0] = 0
        arr = [1] + arr
    for i in arr:
        print(i, end='')
    print()