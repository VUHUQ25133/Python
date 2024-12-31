# Cho danh sách chủ đề và bộ câu hỏi đi kèm theo chủ đề đó trong một bộ đề bài Tiếng Anh.
#     Mỗi bộ câu hỏi theo chủ đề sẽ cách nhau một dòng trống. 
# Mỗi câu hỏi được viết trên một dòng.
#     Ghi ra thống kê số lượng câu hỏi theo từng chủ đề. 
# Thứ tự của chủ đề ở kết quả được giữ nguyên với thứ tự xuất hiện trong dữ liệu vào.

# Input:
#       Dòng đầu cho tổng số dòng dữ liệu
#       Các dòng tiếp theo là danh sách các chủ đề, câu hỏi.
# Output:
#       In ra kết quả theo yêu cầu

#     Input:                                                  Output:
#     9                                                       Home/accommodation: 3
#     Home/accommodation                                      Study: 3
#     What kind of housing/accommodation do you live in?
#     Who do you live with?
#     How long have you lived there?

#     Study
#     Describe your education
#     What is your area of specialization?
#     Why did you choose to study that major?

a = []
for i in range(int(input())): a.append(input())
while len(a)>0:
    ind = len(a)
    for i in range(len(a)):
        if a[i] == '':
            ind = i
            break
    print(f'{a[0]}: {ind-1}')
    a = a[ind+1:]
