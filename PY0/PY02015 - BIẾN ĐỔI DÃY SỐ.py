# Cho một dãy số A[] có 4 số nguyên dương, đánh số vị trí từ 1 đến 4. 
# Tại mỗi bước, giá trị A[i] được thay thế bằng abs(A[i] – A[i+1]), riêng A[4] = abs(A[4]-A[1]).
# Hàm abs (trị tuyệt đối) được sử dụng để đảm bảo các giá trị của dãy số luôn dương.

# Hãy đếm xem sau bao nhiêu bước thì dãy số A[] có cả 4 vị trí đều bằng nhau.

# Input
# Có 4 số của dãy A[], các giá trị không quá 9 chữ số. Input kết thúc với 4 số 0.
# Output
# Với mỗi test, ghi ra số bước cần thực hiện.
# Ví dụ

# Input       Output
# 1 3 5 9     6
# 4 3 2 1     4
# 0 0 0 0

while True:
    list = [int(i) for i in input().split()]
    if list.count(0) == 4:
        break
    cnt = 0
    while list.count(list[0]) != 4:
        tmp = list.copy()
        for i in range(4):
            list[i] = abs(tmp[i] - tmp[(i + 1) % 4])
        cnt += 1
    print(cnt)
