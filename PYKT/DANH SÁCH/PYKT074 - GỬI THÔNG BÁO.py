# Theo quy định của một số thiết bị, nội dung thông báo chỉ được phép chứa tối đa 100 ký tự. 
# Điều này đòi hỏi lập trình viên phải xử lý nội dung các thông báo có độ dài lớn hơn 100 ký tự bằng cách rút gọn thông tin. 
# Tuy nhiên, việc rút gọn phải đảm bảo nguyên tắc không bị cắt giữa từ. 
# Trong trường hợp nếu từ hiện tại làm độ dài thông báo vượt quá 100 ký tự sẽ loại bỏ từ đó khỏi thông báo.

# Nhiệm vụ của bạn là hãy viết chương trình xử lý yêu cầu trên.
# Input:
#     Dòng đầu tiên là số bộ test T < 100.
#     T dòng tiếp theo mỗi dòng là một xâu ký tự có độ dài tối đa 1000 ký tự.
# Output:
#     In ra kết quả các thông báo đã xử lý
# Input:
#     2
#     Can cu Ke hoach giang day - hoc tap hoc ky 1 nam hoc 2021 - 2022 Can cu ket qua thi hoc ky 2 va hoc ky phu ky he nam hoc 2020 - 2021
#     Hoc vien Cong nghe Buu chinh Vien thong to chuc khai giang truc tuyen
# Output:
#     Can cu Ke hoach giang day - hoc tap hoc ky 1 nam hoc 2021 - 2022 Can cu ket qua thi hoc ky 2 va
#     Hoc vien Cong nghe Buu chinh Vien thong to chuc khai giang truc tuyen

for t in range(int(input())):
    s = input().split()
    ans = s[0]
    for i in s[1:]:
        if(len(ans) + len(i) + 1 > 100): break
        ans += ' ' + i
    print(ans)
