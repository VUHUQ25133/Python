# Thang điểm IELTS được tính từ 1.0 - 9.0 IELTS.
# 4 kỹ năng của IELTS cũng tính từ 1.0 - 9.0 để sau đó tính điểm thi IELTS Overall.
# Cả 2 phần thi nghe (Listening) và đọc (Reading) đều có 40 câu hỏi thí sinh cần trả lời. 
# Với một câu trả lời đúng sẽ được 1 điểm, tối đa là 40 điểm và 
#     quy đổi sang thang điểm 1.0 - 9.0 dựa trên tổng số câu trả lời đúng.
# Dưới đây là bảng điểm quy đổi sẽ giúp cho các bạn hiểu hơn về cách chuyển đổi điểm cho từng phần thi Reading và Listening.

#         Listening/Reading
#         Correct ans     Band score
#         39 - 40         9.0
#         37 - 38          8.5
#         35 - 36         8.0
#         33 - 34         7.5
#         30 - 32         7.0
#         27 - 29         6.5
#         23 - 26         6.0
#         20 - 22         5.5
#         16 - 19         5.0
#         13 - 15         4.5
#         10 - 12         4.0
#         7 -  9         3.5
#         5 -  6         3.0
#         3 -  4         2.5

# Điểm tổng của 4 kỹ năng sẽ được làm tròn số theo quy ước chung như sau: 
# Nếu điểm trung bình cộng của 4 kỹ năng 
#     có số lẻ là .25, thì sẽ được làm tròn lên thành .5, 
#     còn nếu là .75 sẽ được làm tròn thành 1.0.

# Một trung tâm tổ chức thi thử Tiếng Anh cho các học viên. 
# Hãy giúp trung tâm tính điểm overall dựa trên kết quả bài làm của thí sinh nhé.

# Input:
#         Dòng đầu cho số T là số lượng thí sinh
#         T dòng tiếp theo mỗi dòng cho 4 số là số câu đúng lần lượt của Reading, Listening, speaking và writing.
# Output: In ra kết quả theo từng dòng.

# Input:              Output:
# 2
# 15 25 5.0 5.5       5.5
# 22 32 6.0 6.0       6.0

def p(x):
    if x > 38: return 9.0
    if x > 36: return 8.5
    if x > 34: return 8.0
    if x > 32: return 7.5
    if x > 29: return 7.0
    if x > 26: return 6.5
    if x > 22: return 6.0
    if x > 19: return 5.5
    if x > 15: return 5.0
    if x > 12: return 4.5
    if x >  9: return 4.0
    if x >  6: return 3.5
    if x >  4: return 3.0
    if x >  2: return 2.5
    return 1.0
def r(x):
    ext = x - int(x)
    if ext >= 0.75: return int(x) + 1.0
    if ext >= 0.25: return int(x) + 0.5
    return float(int(x))
for t in range(int(input())):
    a = input().split()
    s = (p(int(a[0])) + p(int(a[1])) + float(a[2]) + float(a[3]))/4
    print(r(s))
