# Để hiểu địa chỉ Ipv4 là gì có thể lấy ví dụ như sau: 
# Giả sử ta có 1 dải số như sau: 172.16.254.1. 
# Dải số này có thể được dùng để đặt tên cho 1 địa chỉ Ipv4 nào đó. 
# Có thể thấy địa chỉ Ipv4 có tổng cộng 4 số và mỗi số phải nằm trong giới hạn từ 0->255.

# Cho một danh sách các chuỗi ký tự, hãy kiểm tra xem 
#     chuỗi ký tự này có phải địa chỉ IP hợp lệ hay không.

# Input:
#     Dòng đầu tiên cho số T là số bộ test
#     T dòng tiếp theo mỗi dòng là một chuỗi bất kỳ có độ dài < 1000
# Output:
#     In ra kết quả theo từng dòng

#     Input:              Output:
#     2   
#     192.168.1.1         YES
#     256.255.255.255     NO

def check(a):
    if len(a) != 4: return 'NO'
    for i in a:
        if i < 0 or i > 255: return 'NO'
    return 'YES'
for t in range(int(input())):
    try: print(check(list(map(int, input().split('.')))))
    except: print('NO')
