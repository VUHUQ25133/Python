# Một câu trong văn bản được hiểu là dãy ký tự (có cả khoảng trống) 
# cho đến khi gặp dấu ngắt câu hoặc xuống dòng 
#     (đôi khi người ta quên viết dấu ngắt câu nhưng cứ xuống dòng là sang một câu mới). 
# Các dấu ngắt câu trong bài toán này bao gồm: (.), (!), (?).

# Hãy viết chương trình chuẩn hóa các câu trong dữ liệu vào với các yêu cầu sau:
#     Ký tự đầu mỗi câu viết hoa, các ký tự khác viết thường.
#     Các từ cách nhau đúng một khoảng trống.
#     Tự động điền thêm dấu chấm (.) nếu xuống dòng mà chưa có dấu ngắt câu.
#     Dấu ngắt câu phải viết sát ký tự cuối cùng của câu (không tính khoảng trống)
# Input
#     Một văn bản không quá 100 dòng.
# Output
#     Ghi ra các câu đã chuẩn hóa, mỗi câu 1 dòng.

#     Input
#         Chuong trinh Dao Tao CLC nganh CNTT duoc Thiet     Ke theo chuan quoc te.
#         co 03 chuyen nganh la: Cong  nghe phan mem, Tri tue nhan tao va An toan thong tin
#         muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep
#         moi    CAC BAN danG ky     thaM giA !
#     Output
#         Chuong trinh dao tao clc nganh cntt duoc thiet ke theo chuan quoc te.
#         Co 03 chuyen nganh la: cong  nghe phan mem, tri tue nhan tao va an toan thong tin.
#         Muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep.
#         Moi cac ban dang ky tham gia!

doc = ''
while True:
    try:
        doc += input()
        if doc[-1] not in '.?!': doc+=' .'
        else:
            if doc[-2] != ' ': doc = f'{doc[:-1]} {doc[-1]}'
        doc += ' '
    except:
        break
words = doc.split()
i = 0 
while i<len(words):
    sen = ''
    while i<len(words) and words[i] not in '.?!':
        sen+=words[i]+' '
        i+=1
    if words[i] in '.?!': sen = sen[:-1] + words[i]
    i += 1
    print(sen[0].upper() + sen[1:].lower())
