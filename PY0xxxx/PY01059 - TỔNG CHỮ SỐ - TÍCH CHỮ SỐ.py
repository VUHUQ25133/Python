# Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số. 
# Xét các vị trí từ trái qua phải (tính từ 0). Hãy tính:
# Tổng các chữ số ở vị trí chẵn
# Tích các chữ số ở vị trí lẻ. – giá trị tích chữ số có thể đến 18 chữ số. 
# Chú ý khi tính tích bỏ qua các chữ số 0, nhưng nếu tất cả các vị trí lẻ đều là giá trị 0 thì tích = 0.
# Input
# Dòng đầu ghi số bộ test (không quá 20)
# Mỗi bộ test ghi trên một dòng số nguyên dương N (ít nhất 2 chữ số và không quá 500 chữ số)
# Output
# Với mỗi bộ test, viết trên một dòng hai giá trị: tổng chữ số và tích chữ số tính được.

# Ví dụ
# Input               Output
# 3
# 12345678            16 384
# 20000               2 0
# 22334455667788      35 40320

for t in range(int(input())):
    a = list(int(i) for i in input())
    su, mu = 0, 0
    for i in range(len(a)):
        if i % 2 == 0:
            su += a[i]
        else:
            if a[i] != 0:
                if mu == 0:
                    mu = a[i]
                else:
                    mu *= a[i]
    print(str(su) + " " + str(mu))