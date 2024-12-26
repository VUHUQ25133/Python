# Tí năm nay đã lên lớp 1 rồi, Tết đến Tí rất vui vì nhận được rất nhiều lời chúc.
# Vì mới tập viết nên Tí đã ghi lại tất cả các lời chúc đó.
# Cũng vì rất trân trọng các lời chúc nên Tí đã ghi tất cả các lời chúc bằng chữ IN HOA, 
#     tuy nhiên do mới tập viết nên Tí ghi không có dấu. Giờ ngồi lật lại cuốn nhật ký ghi các lời chúc, Tí thấy mình đã ghi được n lời chúc.
# Tí muốn biết có bao nhiêu lời chúc khác nhau.
# Bạn hãy lập chương trình giúp Tí đếm xem có bao nhiêu lời chúc khác nhau nhé.
# Input:
#     Dòng đầu chứa số nguyên dương n là số lời chúc Tí ghi được;
#     n dòng tiếp theo, mỗi dòng chứa một xâu ký tự S là một lời chúc.
#     n, S thỏa mãn ràng buộc: 1 ≤ n ≤ 10^4; Các lời chúc S có độ dài không quá 30 ký tự gồm các chữ cái la tinh IN HOA ‘A’…’Z’ và dấu cách.
# Output:
#     Một số nguyên dương duy nhất là số lời chúc khác nhau.
# Ví dụ:
# Input:                  Output:
# 4
# CHUC MUNG NAM MOI       3
# HAPPY NEW YEAR
# CHUC MUNG TUOI MOI
# CHUC MUNG NAM MOI

print(len({input() for i in range(int(input()))}))
