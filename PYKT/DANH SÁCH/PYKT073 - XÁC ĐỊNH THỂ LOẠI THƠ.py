# Cho danh sách các bài thơ gồm hai thể loại thơ:
#     1. Thơ lục bát
#     2. Thơ thất ngôn tứ tuyệt
# Nhiệm vụ của bạn là hãy viết chương trình xác định số lượng bài thơ và thể thơ (ghi bằng số) của từng bài từ danh sách các bài thơ có sẵn.
# Input:
#     Dòng đầu tiên cho số N là tổng số dòng của tất cả các bài thơ.
#     N dòng tiếp theo ghi lại các câu thơ của từng bài. Các bài thơ lục bát sẽ đảm bảo không đặt liên tiếp nhau.
# Output:
#     In ra kết quả số bài thơ và số tương ứng với thể thơ theo từng dòng.
# Input:
# 8
#     Minh ve minh co nho ta
#     Muoi lam nam ay thiet tha man nong
#     Minh ve minh co nho khong
#     Nhin cay nho nui nhin song nho nguon
#     Mot canh hai canh lai ba canh
#     Tran troc ban khoan giac chang lanh
#     Canh bon canh nam vua chop mat
#     Sao vang nam canh mong hon bay
# Output:
#     2
#     1
#     2



pre, ans, _ = -1, [], input()
try:
    while True:
        l = len(input().split())
        if l == 6: 
            input()
            if l != pre: ans.append(1)
        else: 
            ans.append(2)
            for i in range(3): input()
        pre = l
except: pass
print(len(ans))
for i in ans: print(i)

