# Cho một số nhị phân, người ta nhận ra quy tắc đơn giản là chỉ cần 
# xét lần lượt các cụm ba chữ số nhị phân tình từ cuối của số đó, 
# sau đó chuyển lần lượt từng cụm sang giá trị thập phân tương ứng thì 
# kết quả nhận được chính là biểu diễn của số đó trong hệ cơ số 8. 
# Nếu cụm cuối cùng bị thiếu thì bổ sung các chữ số 0 cho đủ 3 chữ số.

# Ví dụ:
# 11001100 => 011 | 001 | 100 => 314

# Hãy áp dụng tính chất trên để chuyển đổi một số nhị phân (không quá 100 chữ số và luôn bắt đầu bởi chữ số 1) sang hệ cơ số 8.

# Input
# Chỉ có một số nhị phân, không quá 100 chữ số

# Output
# Ghi ra kết quả trong hệ cơ số 8

# Ví dụ

# Input       Output
# 1010        12
# 11001100    314

print(oct(int(input(), 2))[2::])