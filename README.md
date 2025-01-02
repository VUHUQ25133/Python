# I. Variable & Data type
## Biến
### Quy tắc và một số hướng dẫn:
- Tên biến chỉ có thể chứa các chữ cái, số và dấu gạch dưới. Chúng có thể bắt đầu bằng một chữ cái hoặc một dấu gạch dưới, nhưng không phải bằng một số.
- Không được phép sử dụng dấu cách trong tên biến, nhưng có thể sử dụng dấu gạch dưới để tách các từ trong tên biến.
- Tránh sử dụng các từ khóa Python và tên hàm làm tên biến
- Tên biến phải ngắn nhưng mang tính mô tả.
- Cẩn thận khi sử dụng chữ cái viết thường l và chữ cái viết hoa O vì chúng có thể bị nhầm lẫn với số 1 và số 0

## Chuỗi (Strings)
Một chuỗi là một chuỗi các ký tự. Mọi thứ bên trong dấu ngoặc kép đều được xem xét một chuỗi. Với Python, ta có thể sử dụng dấu (') hoặc (") xung quanh chuỗi.
`"This is a string."`
`'This is also a string.'`
`'I told my friend, "Python is my favorite language!"'`
`"The language 'Python' is named after Monty Python, not the snake."`
`"One of Python's strengths is its diverse and supportive community.`
### Sử dụng chữ hoa trong chuỗi với các phương thức
- title() thay đổi chữ thường thành chữ hoa như tiêu đề, do đó mỗi ký tự đầu chữ sẽ thành chữ hoa.
- upper() đổi hết thành chữ hoa
- lower() đổi hết thành chữ thường
```py
    name = "Ada Lovelace"
    print(name.title()) # Ada Lovelace
    print(name.upper()) # ADA LOVELACE
    print(name.lower()) # ada lovelace
```
### Sử dụng biến trong chuỗi
1. Sử dụng giá trị của một biến bên trong một chuỗi (f-strings)
2. Sử dụng f-string để tạo thông điệp hoàn chỉnh
3. Sử dụng f-string để soạn thông điệp, sau đó gán toàn bộ thông điệp cho một biến
```py
    first_name = "ada"
    last_name = "lovelace"
    full_name = f"{first_name} {last_name}"

    print(full_name)    # 1. ada lovelace
    print(f"Hello, {full_name.title()}!")   # 2. Hello, Ada Lovelace!
    message = f"Hello, {full_name.title()}!"
    print(message)  # 3. Hello, Ada Lovelace!
```
### Thêm khoảng trắng vào chuỗi với Tab hoặc dòng mới
Để thêm Tab vào chuỗi, sử dụng tổ hợp ký tự: \t
Để thêm một dòng mới trong một chuỗi, hãy sử dụng tổ hợp ký tự \n
### Bỏ khoảng trắng
- Khoảng trắng thừa có thể gây nhầm lẫn, do cần loại bỏ trước khi thực hiện các tác vụ.
- Python giúp loại bỏ dễ dàng khoảng trắng thừa từ dữ liệu người dùng nhập vào bằng phương thức strip()
- Lưu ý: Để xóa khoảng trắng vĩnh viễn, ta thực hiện phép gán:
  - Xóa khoảng trắng bên phải: rstrip()
  - Xóa khoảng trắng bên trái: lstrip()
```py
    favorite_language = ' python '
    favorite_language.rstrip() # ' python'
    favorite_language.lstrip() # 'python '
    favorite_language.strip()  # 'python'
```
### Tránh lỗi cú pháp với String
- Cách sử dụng chính xác dấu nháy kép và dấu nháy đơn:
- Nếu sử dụng dấu nháy đơn, Python không thể xác định vị trí chuỗi nên kết thúc
```py
    message = "One of Python's strengths is its diverse community."
    print(message) # One of Python's strengths is its diverse community
# dùng nháy đơn sẽ SyntaxError
```
## Số (Numbers)
### Integers
- Trong một phiên đầu cuối, Python trả về kết quả của toán tử. Python sử dụng hai ký hiệu nhân để biểu diễn số mũ:
```
>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 10 ** 6
1000000
```
### Floats
- Khi chia hai số bất kỳ, ngay cả khi chúng là số nguyên dẫn đến kết quả đều sẽ là số thực
- Nếu kết hợp số nguyên và số thực trong một phép toán, kết quả sẽ nhận được là số thực
```
>>> 4 / 2
2.0
>>> 1 + 2.0
3.0
>>> 2 * 3.0
6.0
>>> 3.0 ** 2
9.0
```
### Các gạch dưới trong số
- Khi viết các số dài, ta có thể nhóm các chữ số bằng dấu gạch dưới để làm cho các số lớn dễ đọc hơn:
  `universe_age = 14_000_000_000`
- Khi in ra số dùng gạch dưới, Python chỉ in ra các số
  ```py
    print(universe_age) # 14000000000
  ```
### Gán nhiều biến cùng lúc
- Gán giá trị cho nhiều biến chỉ bằng một dòng duy nhất, điều này làm cho chương trình ngắn hơn và dễ đọc hơn
- Cần tách các tên biến bằng dấu phẩy và thực hiện tương tự với các giá trị và Python sẽ chỉ định từng giá trị tương ứng với biến theo vị trí
  `x, y, z = 0, 0, 0`
### Constants
- Python không có sẵn các loại hằng số, nhưng các LTV Python sử dụng tất cả các chữ cái viết hoa để chỉ ra một biến nên được coi là không đổi và không bao giờ bị thay đổi: `MAX_CONNECTIONS = 5000`
- Khi muốn coi biến là một hằng số trong mã, hãy viết hoa tất cả các chữ cái trong tên biến. 

# II. Condition Statements
## Kiểm tra có điều kiện
**Cú pháp:** 
```py
    if condition:
        # one or more statements

    # Ví dụ:
    if (number % 2 == 0):
        print (number + "is even")
    else:
        print (number + "is odd")
```
### Kiểm tra đẳng thức
```
>>> car = 'bmw'                     >>> car = 'audi'
>>> car == 'bmw'                    >>> car == 'bmw'
True                                False
```
Trong ví dụ trên, dấu bằng '=' chính là một câu, thực hiện lệnh gán. Trong khi đó, dấu bằng kép '==' lại khiến nó trở thành câu hỏi: “Liệu giá trị của biến car có bằng 'bmw' hay không?”.
### Bỏ qua chữ viết hoa khi kiểm tra đẳng thức
```
>>> car = 'Audi'            >>> car = 'Audi'                >>> car = 'Audi'
>>> car == 'audi'           >>> car.lower() == 'audi'       >>> car.lower() == 'audi'
False                       True                            True

>>> car
'Audi'
```
### Kiểm tra nhiều điều kiện
- **and, or**
- **in** kiểm tra một giá trị cụ thể đã có trong danh sách hay chưa.
```
    >>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
    >>> 'mushrooms' in requested_toppings
    True
    >>> 'pepperoni' in requested_toppings
    False
```
=> Kỹ thuật này là khá mạnh mẽ vì chúng ta có thể tạo danh sách các giá trị thiết yếu và sau đó dễ dàng kiểm tra xem giá trị ta đang kiểm tra có khớp với một trong các giá trị trong danh sách hay không.
- **not in** kiểm tra một phần tử không nằm trong danh sách

## Câu lệnh if
### Lệnh đơn giản
Chúng ta có thể có bao nhiêu dòng mã tùy thích trong khối theo sau câu lệnh if.
```py 
    age = 19
    if age >= 18:
        print("You are old enough to vote!")
        print("Have you registered to vote yet?")
```
### Chuỗi if-elif-else
```py
age = 12
①   if age < 4:
        print("Your admission cost is $0.")
②   elif age < 18:
        print("Your admission cost is $25.")
③   else:
        print("Your admission cost is $40.")
```
- Thay vì in giá vào cửa trong khối if-elif-else, sẽ ngắn gọn hơn nếu chỉ đặt giá bên trong chuỗi if-elif-else, sau đó có một lệnh gọi print() đơn giản chạy sau khi chuỗi đã được đã đánh giá
```py
    age = 12
    if age < 4:
①       price = 0
    elif age < 18:
②       price = 25
    else:
③       price = 40
④   print(f"Your admission cost is ${price}.")
```
- Có thể sử dụng bao nhiêu khối elif trong mã tùy thích
- Python không yêu cầu một khối else ở cuối chuỗi if-elif. Đôi khi một khối else hữu ích; đôi khi việc sử dụng một khối elif khác khiến nó rõ ràng hơn

# III. Loops
## FOR
    
```py
    for variable in [val1, val2, etc.]: statements
# VD: 
    for val in "apple": print(val) # a, p, p, l, e
```
### Hàm range() với vòng lặp
`range(start, end, step)`
Trong đó:
    - start: giá trị bắt đầu
    - end: giá trị kết thúc
    - step: bước nhảy vòng lặp

Đặc điểm của range:
    - Một tham số: được sử dụng làm giới hạn kết thúc
    - Hai tham số: giá trị bắt đầu và giới hạn kết thúc
    - Ba tham số: tham số thứ ba là giá trị bước (step value)
VD:
```py
    for n in range(10):
        print(n, end = ' ')    # 0 1 2 3 4 5 6 7 8 9
    for n in range(1,10):
        print(n, end = ' ')    # 1 2 3 4 5 6 7 8 9
    for n in range(1,10,2):
        print(n, end = ' ')    # 1 3 5 7 9 
    for n in range(10,0,-1):
        print(n, end = ' ')    # 10 9 8 7 6 5 4 3 2 1 
    for n in range(10,0,-2):
        print(n, end = ' ')    # 10 8 6 4 2
    for n in range(2,11,2):
        print(n, end = ' ')    # 2 4 6 8 10
```
## WHILE
```py
# Cú pháp:
    while (condition):
        block

# VD:
print("Nhập N = ")
n = int(input())
s = 0
i = 1
while i <= n:
    s += i;
    i += 1;
print("Tổng = ", s)

# VD2:
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
print(message)
```
- Tại message = input(prompt), Python hiển thị lời nhắc và đợi người dùng nhập thông tin đầu vào của họ. Bất cứ thứ gì người dùng nhập đều được gán vào biến message và in ra; sau đó, Python đánh giá lại điều kiện của vòng lặp while.
- Miễn là người dùng chưa nhập từ ‘quit’, lời nhắc được hiển thị lại và Python chờ thêm đầu vào. Khi người dùng cuối cùng nhập ‘quit’, Python dừng thực hiện vòng lặp while và chương trình kết thúc

# IV. User Input
## Cách hàm Input() hoạt động
- Hàm input() tạm dừng chương trình của chúng ta và đợi người dùng nhập một số tiếp theo. Khi Python nhận được đầu vào của người dùng, nó sẽ gán đầu vào đó cho biến để giúp thuận tiện khi làm việc.
- Hàm input() nhận một đối số: dấu nhắc hoặc hướng dẫn, mà chúng ta muốn hiển thị cho người dùng để họ biết phải làm gì. 
Chương trình đợi trong khi người dùng nhập phản hồi của họ và tiếp tục sau khi người dùng nhấn enter. Câu trả lời là được gán cho biến message, sau đó hàm print(message) hiển thị tại đầu vào cho người dùng
### Viết lời nhắc rõ ràng
Gán lời nhắc của mình cho một biến và chuyển biến đó vào hàm input()
```py
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

# If you tell us who you are, we can personalize the messages you see.
# What is your first name? Eric
# Hello, Eric!
```
### Sử dụng int() để nhận đầu vào số nguyên
Khi ta sử dụng hàm input(), Python sẽ thông dịch mọi thứ mà người dùng nhập dưới dạng một chuỗi. Hàm int() chuyển đổi biểu diễn chuỗi của một số thành biểu diễn số
```py
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
# How tall are you, in inches? 71
# You're tall enough to ride!
```


# V. Lists
## Định nghĩa danh sách
- Trong Python, ngoặc vuông ([ ]) chỉ định một danh sách và các phần tử trong danh sách được phân tách bởi dấu phẩy (,). Ví dụ danh sách chứa các loại xe đạp khác nhau.
```py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# ['trek', 'cannondale', 'redline', 'specialized']
```
### Truy cập các phần tử trong danh sách
Để truy cập một phần tử trong danh sách, hãy viết tên của danh sách theo sau là chỉ mục của mục được đặt trong dấu ngoặc vuông. Ví dụ: hãy lấy chiếc xe đạp đầu tiên trong danh sách bicycles:
```py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])  # trek
```
Python chỉ trả về phần tử đó mà không có dấu ngoặc vuông
Có thể định dạng phần tử 'trek' gọn gàng hơn bằng cách sử dụng
phương thức title():
```py
print(bicycles[0].title()) # Trek
```
### Đánh chỉ mục
- Chỉ mục danh sách bắt đầu từ 0
- Để truy cập mục thứ tư trong danh sách, ta yêu cầu phần tử chỉ mục 3
- Để truy cập phần tử cuối cùng trong danh sách, dùng chỉ mục -1
```py
print(bicycles[1]) # cannondale
print(bicycles[3]) # specialized
print(bicycles[-1]) # specialized
```
### Ví dụ
Đoạn mã sau đây lặp lại danh sách tên xe và tìm kiếm giá trị 'bmw'. Bất cứ khi nào giá trị là 'bmw', nó sẽ được in bằng chữ hoa thay vì chữ hoa tiêu đề
cars = ['audi', 'bmw', 'subaru', 'toyota']
```py
for car in cars:                # Audi
    if car=='bmw':              # BMW
        print(car.upper())      # Subaru
    else:                       # Toyota
        print(car.title())
```
## Thay đổi, thêm, và xóa các phần tử
### Thay đổi phần tử trong danh sách
Để thay đổi một phần tử, sử dụng tên của danh sách theo sau bằng chỉ mục của phần tử mong muốn thay đổi, sau đó cung cấp giá trị
```py
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)          # ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'   # ['ducati', 'yamaha', 'suzuki']
print(motorcycles)
```
### Thêm phần tử vào danh sách
- Thêm phần tử vào cuối danh sách: dùng phương thức append()
- Dùng append() để tạo danh sách động: 
```py
motorcycles = ['honda', 'yamaha', 'suzuki']     
print(motorcycles)              # ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)              # ['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)      # ['honda', 'yamaha', 'suzuki']
```
- Thêm một phần tử mới ở bất kỳ vị trí nào trong danh sách bằng cách sử dụng
phương thức insert()
```py
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)      # ['ducati', 'honda', 'yamaha', 'suzuki']
```
Phương thức insert() tạo ra một khoảng trống tại giá trị 0 và lưu giá trị ‘ducati’ tại vị trí đó. Câu lệnh này dịch chuyển tất cả các phần tử còn lại một vị trí sang phải
### Xóa phần tử khỏi danh sách
- Xóa phần tử sử dụng lệnh del (Khi biết vị trí của phần tử trong danh sách)
- Phương thức pop() loại bỏ mục cuối cùng trong danh sách, nhưng nó cho phép ta làm việc với mục đó sau khi loại bỏ nó.
- Sử dụng pop() để xóa một mục khỏi bất kỳ vị trí nào trong danh sách bằng cách bao gồm chỉ mục của mục mà ta muốn xóa
```py
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)      # ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)      # ['honda', 'suzuki']

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)          # ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)          # ['honda', 'yamaha']
print(popped_motorcycle)    # suzuki

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.") # The last motorcycle I owned was a Suzuki

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.") # The first motorcycle I owned was a Honda.
```
=> Khi ta muốn xóa một mục khỏi danh sách và không sử dụng mục đó theo bất kỳ cách nào, hãy sử dụng câu lệnh del; 
=> Nếu ta muốn sử dụng phần tử khi ta xóa nó, hãy sử dụng phương thức pop()

VD: Sử dụng vòng lặp while để kéo người dùng khỏi danh sách người dùng chưa
được xác minh và sau đó thêm họ vào một danh sách riêng người dùng đã xác
minh
```py
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:                                # Verifying user: Candace
    current_user = unconfirmed_users.pop()              # Verifying user: Brian
    print(f"Verifying user: {current_user.title()}")    # Verifying user: Alice
    confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")     # The following users have been confirmed:
for confirmed_user in confirmed_users:                  # Candace
    print(confirmed_user.title())                       # Brian
                                                        # Alice
```
### Xóa phần tử bằng giá trị
- Nếu ta chỉ biết giá trị của phần tử muốn xóa, ta có thể sử dụng
phương thức remove()
- Sử dụng phương thức remove() để làm việc với một giá trị đang bị xóa khỏi
danh sách
```py
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']
print(f"\nA {too_expensive.title()} is too expensive for me.")
# A Ducati is too expensive for me.
```
- Giả sử ta có một danh sách các vật nuôi có giá trị 'cat' được lặp lại nhiều lần. Để loại bỏ tất cả các trường hợp của giá trị đó, ta có thể chạy một vòng lặp while cho đến khi 'cat' không còn trong danh sách
```py
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)     # ['dog', 'dog', 'goldfish', 'rabbit']
```
## Tổ chức danh sách
- Thông thường, danh sách sẽ được tạo theo một thứ tự không
thể biết trước, bởi vì không thể kiểm soát thứ tự mà người dùng
cung cấp dữ liệu của họ.
- Vấn đề là ta luôn cần trình bày thông tin theo một trật tự nào đó.
- Đôi khi, ta cần giữ nguyên thứ tự ban đầu của dữ liệu, đôi khi lại cần thay đổi thứ tự theo lúc đầu.
### sort()
- Phương thức sort() của Python giúp sắp xếp danh sách: 
- Sắp xếp danh sách này theo thứ tự bảng chữ cái ngược lại bằng cách chuyển đối số reverse = True vào phương thức sort()
```py
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) # ['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse = True)
print(cars) # ['toyota', 'subaru', 'bmw', 'audi']
```
### sorted()
- Hàm sorted() cho phép hiển thị danh sách theo một thứ tự cụ thể nhưng không ảnh hưởng đến thứ tự thực tế của danh sách.
- Hàm sorted() cũng có thể chấp nhận đối số reverse = True nếu ta muốn hiển thị danh sách theo thứ tự bảng chữ cái ngược lại.
### In danh sách theo thứ tự ngược
Để đảo ngược thứ tự ban đầu của danh sách, ta có thể sử dụng phương thức reverse()
### Tìm độ dài của danh sách
Tìm độ dài của danh sách bằng cách sử dụng hàm len().
*Chú ý: Python đếm các mục trong danh sách bắt đầu bằng một, vì vậy ta sẽ không gặp phải bất kỳ lỗi nào khi xác định độ dài của danh sách*
```py
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars)) # 4
```
## Tránh lỗi chỉ mục
- Giả sử danh sách có 3 phần tử, ta yêu cầu in ra phần tử thứ 4, Python sẽ thông báo lỗi chỉ mục. Lỗi chỉ mục có nghĩa là Python không thể kết xuất một mục tại chỉ mục được yêu cầu. Nếu lỗi chỉ mục xảy ra trong chương trình, hãy thử điều chỉnh chỉ mục đang được yêu cầu một đơn vị. 
- Bất cứ khi nào ta muốn truy cập phần tử cuối cùng trong danh sách, hãy sử dụng chỉ mục (-1). Tiếp cận này chỉ xảy ra lỗi trong trường hợp duy nhất đó là khi danh sách trống
### Câu lệnh If với danh sách
Ta có thể thực hiện một số công việc thú vị khi kết hợp danh sách và câu lệnh if. Ta có thể xem các giá trị đặc biệt cần được xử lý khác hơn so với các giá trị khác trong danh sách
```py
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")
# Adding mushrooms.
# Adding green peppers.
# Adding extra cheese.
# Finished making your pizza!
```
### Kiểm tra một danh sách không rỗng
VD: 
```py
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
# Are you sure you want a plain pizza?
```
### Sử dụng range() để tạo ra danh sách số
- Ta có thể chuyển đổi kết quả của hàm range() trực tiếp vào một danh sách bằng cách sử dụng hàm list(). Khi chúng ta bọc list() xung quanh một hàm range(), đầu ra sẽ là một danh sách các số.
- Nếu ta truyền đối số thứ ba vào range(), Python sẽ sử dụng giá trị đó như một kích thước bước khi tạo số
```py
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]

# VD
squares = []
for value in range(1,11):
    squares.append(value**2)
    print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
### Thống kê đơn giản với danh sách số
Dễ dàng tổng hợp các giá trị tối thiểu, tối đa và tổng của một danh
sách số:
```
>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> min(digits)
0
>>> max(digits)
9
>>> sum(digits)
45
```
### Hiểu về danh sách
Ví dụ xây dựng cùng một danh sách các số bình phương mà ta đã thấy ở trên nhưng sử dụng khả năng hiểu danh sách:
```py
squares = [value**2 for value in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
- Vòng for cho giá trị trong range(1,11) để đưa giá trị từ 1 tới 10 vào trong biểu thức. 
- Ghi nhớ là không sử dụng dấu hai chấm ở cuối câu lệnh for.

## Làm việc với một phần của danh sách (slice)
- Để in ra 3 phần tử đầu tiên trong danh sách, ta cần chỉ định từ 0 tới 3, Python sẽ trả về 3 phần tử là 0,1,2.
```py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # ['charles', 'martina', 'michael']
print(players[1:4]) # ['martina', 'michael', 'florence']
```
- Nếu ta bỏ qua chỉ mục đầu tiên slice, Python sẽ tự động bắt đầu slice đầu danh sách:
```py 
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4]) # ['charles', 'martina', 'michael', 'florence']
```
- Nếu muốn tất cả các phần tử từ thứ ba đến cuối cùng, ta có thể bắt đầu với 2 và bỏ qua chỉ mục thứ hai.
```py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:]) # ['michael', 'florence', 'eli']
```
Cần nhớ rằng một chỉ mục âm trả về một phần tử cách cuối danh sách một khoảng cách nhất định; Ta có thể xuất bất kỳ lát nào từ cuối danh sách. Ví dụ, nếu ta muốn xuất ra ba cầu thủ cuối cùng trong danh sách, có thể sử dụng `players[-3:]`
```py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:]) # ['michael', 'florence', 'eli']
```
### ặp qua một lát cắt
Lặp lại ba người chơi và in tên của họ như một phần của danh sách:
```py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player.title())
# Charles
# Martina
# Michael
```
### Sao chép danh sách
- Để sao chép một danh sách, chúng ta có thể tạo một phần bao gồm toàn bộ danh sách gốc bằng cách bỏ qua chỉ mục đầu tiên và chỉ mục thứ hai ([:]).
```py
my_foods = ['pizza', 'falafel', 'carrot cake']  # My favorite foods are:
friend_foods = my_foods[:]                      # ['pizza', 'falafel', 'carrot cake']
print("My favorite foods are:")                 # My friend's favorite foods are:
print(my_foods)                                 # ['pizza', 'falafel', 'carrot cake']
print("\nMy friend's favorite foods are:")
print(friend_foods)
```
- Xác thực hai danh sách riêng biệt
```py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]             # My favorite foods are:
my_foods.append('cannoli')             # ['pizza', 'falafel', 'carrot cake', 'cannoli']
friend_foods.append('ice cream')       # My friend's favorite foods are:
print("My favorite foods are:")        # ['pizza', 'falafel', 'carrot cake', 'ice cream']
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
```
- Sao chép hai danh sách không sử dụng lát cắt
```py
my_foods = ['pizza', 'falafel', 'carrot cake']
# This doesn't work:
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
```
## Vòng lặp for cho list
Cú pháp:
```py
for val in list:
    print(val)
```
Trong đó:
    • val: biến nhận giá trị của từng mục trong chuỗi trên mỗi lần lặp.
    • list: danh sách những phần tử cần lặp
```py
# VD
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```
Sẽ hữu ích khi chọn một cái tên có ý trong vòng for nghĩa đại diện cho một mục
duy nhất từ danh sách
```py
# VD:
    for cat in cats:
    for dog in dogs:
    for item in list_of_items:
```
Bất kỳ dòng mã nào sau vòng lặp for không được thụt lề đều được thực thi một lần mà không lặp lại. 

## Tuples
- Một bộ tuple trông giống như một danh sách ngoại trừ việc ta sử dụng dấu ngoặc đơn thay vì dấu ngoặc vuông.
- Khi định nghĩa một bộ tuple, ta có thể truy cập các phần tử riêng lẻ bằng cách sử dụng chỉ mục của từng mục, giống như cách làm đối với danh sách.
```py
dimensions = (200, 50)
print(dimensions[0])    # 200
print(dimensions[1])    # 50
```
Hãy thử thay đổi giá trị của một phần tử trong Tuple:
```py
dimensions[0] = 250
# TypeError: 'tuple' object does not support item assignment
```
Nếu ta muốn xác định một tuple với một phần tử, ta cần bao gồm một dấu phẩy ở cuối:
```py
my_t = (3,)
print(my_t[0])  # 3
```
Lặp lại tất cả các giá trị trong một bộ bằng cách sử dụng vòng lặp for, giống như đã làm với danh sách:
```py 
dimensions = (200, 50)
for dimension in dimensions:
print(dimension)
# 200
# 50
```
### Ghi lên Tuple
Chúng ta không thể sửa đổi tuple, nhưng ta có thể chỉ định một giá trị mới cho một biến đại diện cho một tuple. Vì vậy, nếu chúng ta muốn thay đổi thứ kích cỡ của hình chữ nhật, chúng ta sẽ định nghĩa lại tuple
```py 

dimensions = (200, 50)              # Original dimensions:
print("Original dimensions:")       # 200
for dimension in dimensions:        # 50
    print(dimension)                
dimensions = (400, 100)             # Modified dimensions:
print("\nModified dimensions:")     # 400
for dimension in dimensions:        # 100
    print(dimension)
```

```py
# Import thư viện
import random

# Tạo một tuple
supplies = ('pens', 'staplers', 'flamethrowers', 'binders')

# Lặp trên chỉ số của tuple
print("Lặp trên chỉ số với tuple:")

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
# Sử dụng hàm enumerate() với tuple
print("\nSử dụng hàm enumerate() với tuple:")

for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

# Sử dụng random.choice() với tuple
print("\nSử dụng random.choice() với tuple:")

pets = ('Dog', 'Cat', 'Moose')
print("Random choice 1:", random.choice(pets))
print("Random choice 2:", random.choice(pets))
print("Random choice 3:", random.choice(pets))

# Sử dụng random.shuffle() với tuple (phải chuyển đổi sang danh sách)
print("\nSử dụng random.shuffle() với tuple (chuyển tuple thành danh sách):")

people = ('Alice', 'Bob', 'Carol', 'David')

# Chuyển đổi tuple thành danh sách
people_list = list(people)
print("Danh sách trước khi trộn:", people_list)
# Trộn ngẫu nhiên
random.shuffle(people_list)
print("Danh sách sau khi trộn:", people_list)
# Nếu cần, chuyển lại về tuple
people_shuffled = tuple(people_list)
print("Tuple sau khi trộn:", people_shuffled)
```
```
Lặp trên chỉ số với tuple:
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flamethrowers
Index 3 in supplies is: binders

Sử dụng hàm enumerate() với tuple:
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flamethrowers
Index 3 in supplies is: binders

Sử dụng random.choice() với tuple:
Random choice 1: Cat
Random choice 2: Moose
Random choice 3: Dog

Sử dụng random.shuffle() với tuple (chuyển tuple thành danh sách):
Danh sách trước khi trộn: ['Alice', 'Bob', 'Carol', 'David']
Danh sách sau khi trộn: ['Carol', 'David', 'Alice', 'Bob']
Tuple sau khi trộn: ('Carol', 'David', 'Alice', 'Bob')

```

# VI. Dictionaries
## Ví dụ đơn giản về từ điển
Giả sử một trò chơi có các đồ vật (aliens) có mầu sắc và có các điểm số khác nhau. Một từ điển đơn giản lưu thông tin về một đồ vật cụ thể
```py 
alien_0 = {'color':'green','point':5}
print(alien_0['color']) # green
print(alien_0['point']) # 5
```
Từ điển alien_0 lưu giá trị mầu sắc và điểm của đồ vật
## Làm việc với từ điển
- Một từ điển được đặt trong dấu ngoặc nhọn, {} , với một loạt các cặp khóa-giá trị bên trong dấu ngoặc nhọn: `alien_0 = {'color': 'green', 'points': 5}`
- Cặp khóa-giá trị là một tập hợp các giá trị được liên kết với nhau. Khi chúng ta cung cấp một khóa, Python sẽ trả về giá trị được liên kết với khóa đó.
- Mọi khóa được kết nối với giá trị của nó bằng dấu hai chấm (:) và các cặp khóa-giá trị riêng lẻ được tách riêng bằng dấu phẩy.
- Chúng ta có thể lưu trữ nhiều cặp khóa-giá trị tùy thích trong từ điển.
- Từ điển đơn giản nhất có chính xác một cặp khoá-giá trị: `alien_0 = {'color': 'green'}`
- Từ điển này lưu trữ một phần thông tin về alien_0, cụ thể là màu của alien. Chuỗi 'color' là một khóa và các liên kết với giá trị là 'green'
### Truy cập các giá trị trong từ điển
- Để lấy giá trị được liên kết với một khóa, cần đặt tên từ điển và sau đó đặt khóa bên
trong một tập hợp các dấu ngoặc vuông 
```py
alien_0 = {'color': 'green'}
print(alien_0['color']) # Green
```
- Có thể có số lượng cặp khóa-giá trị không giới hạn trong một từ điển.
```py
alien_0 = {'color': 'green', 'points': 5}
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!") # You just earned 5 points!
```
### Thêm các cặp khoá-giá trị mới
- Ta sẽ cung cấp tên của từ điển, sau đó là khóa mới trong ô vuông dấu ngoặc cùng với giá trị mới. Thêm hai thông tin vào từ điển của alien_0: hai tọa độ x và y của một đồ vật, giúp hiển thị đồ vật tại một vị trí nhất định trên màn hình
```py
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# {'color': 'green', 'points': 5}
# {'color': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}
```
Phiên bản sau của từ điển có bốn cặp khóa-giá trị. Hai cặp đầu chỉ mầu sắc và điểm của
đồ vật, hai cặp sau chỉ vị trí của con đồ vật
### Bắt đầu với từ điển rỗng
- Bắt đầu một từ điển với cặp ngoặc nhọn ({}) rỗng và sau đó thêm cặp giá trị-khóa vào từ điển trong một dòng mã riêng
```py
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0) # {'color': 'green', 'points': 5}
```
### Sửa giá trị trong từ điển
- Thiết lập tên từ điển với giá trị của khóa trong ngoặc vuông, sau đó tới giá trị của khóa mà ta muốn gán cho khóa đó.
```py
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")  # The alien is green.
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.") # The alien is now yellow.
```
Ví dụ: theo dõi vị trí của con đồ vật có thể di chuyển với các tốc độ khác nhau.
```py
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")    # Original x-position: 0
if alien_0['speed'] == 'slow':
    x_inc = 1
elif alien_0['speed'] == 'medium':
    x_inc = 2
else:
    x_inc = 3
# The new position is the old position plus the increment.
alien_0['x_position'] += x_inc
print(f"New position: {alien_0['x_position']}")         # New x-position: 2
```
### Xóa các cặp khóa-giá trị
Khi không còn cần một phần thông tin được lưu trữ trong một từ điển nữa, có thể sử dụng câu lệnh del để xóa hoàn toàn một cặp khóa-giá trị.
```py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)          # {'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0)          # {'color': 'green'}
```
### Từ điển của các đối tượng tương tự
Cũng có thể sử dụng từ điển để lưu trữ một loại thông tin về nhiều đối tượng. Ví dụ, giả sử ta muốn thăm dò ý kiến một số người và hỏi họ ngôn ngữ lập trình yêu thích của họ là gì
```py
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.") # Sarah's favorite language is C.
```
### Sử dụng get() để truy cập các giá trị
Việc sử dụng các khóa trong dấu ngoặc vuông để truy xuất giá trị mà chúng ta quan tâm từ từ điển có thể gây ra một vấn đề tiềm ẩn: nếu khóa ta yêu cầu không tồn tại, chương trình sẽ gặp lỗi.
```py
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points']) 
# Traceback (most recent call last):
# File "alien_no_points.py", line 2, in <module>
#   print(alien_0[‘points’])
# KeyError: 'points'
```
Có thể sử dụng phương thức get() để đặt giá trị mặc định sẽ được trả về nếu khóa được
yêu cầu không tồn tại
```py
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned. ')
print(point_value)  # No point value assigned
```

## Lặp qua toàn bộ từ điển
### Lặp qua tất cả các cặp khóa-giá trị
- Xem xét một từ điển mới được thiết kế để lưu trữ thông tin về người dùng trên một trang web. Từ điển sau sẽ lưu trữ username, first name, and last name
```py
user_0 = {  
    'username': 'efermi',               # Key: last
    'first': 'enrico',                  # Value: fermi
    'last': 'fermi',                    # Key: first
}                                       # Value: enrico
for key, value in user_0.items():       # Key: username
    print(f"\nKey: {key}")              # Value: efermi
    print(f"Value: {value}")
```
- Nếu ta lặp qua từ điển favorite_languages, ta sẽ nhận được tên của từng người trong
từ điển và ngôn ngữ lập trình yêu thích của họ.
```py
fav_languages = {
    'jen': 'python',                    # Jen's favorite language is Python.
    'sarah': 'c',                       # Sarah's favorite language is C.
    'edward': 'ruby',                   # Edward's favorite language is Ruby.
    'phil': 'python',                   # Phil's favorite language is Python.
}
for name, language in fav_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
```
### Lặp qua tất cả các khoá trong từ điển
- Phương thức key() hữu ích khi ta không cần phải làm việc với tất cả các giá trị trong từ điển. Hãy xem qua từ điển fav_languages và in tên của những người đã tham gia cuộc thăm dò ý kiến
```py
fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in fav_languages.keys():
print(name.title())
```
- Lặp qua các khóa thực sự là hành vi mặc định khi lặp qua từ điển, vì vậy hai đoạn mã này
sẽ có cùng đầu ra: `for name in fav_languages:`, `for name in fav_languages.keys():`
- Có thể truy cập giá trị được liên kết với bất kỳ khóa nào ta quan tâm bên trong vòng lặp bằng cách sử dụng khóa hiện tại.
```py
friends = ['phil', 'sarah']
for name in fav_languages.keys():
    print(name.title())
    if name in friends:
        language = fav_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
# Hi Jen.
# Hi Sarah.
# Sarah, I see you love C!
# Hi Edward.
# Hi Phil.
# Phil, I see you love Python!
```
- Có thể sử dụng phương thức keys() để tìm hiểu xem một người cụ thể có được thăm dò ý kiến hay không
```py
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")    # Erin, please take our poll!
```
### Lặp các khoá của từ điển theo một thứ tự cụ thể
Ta có thể sử dụng hàm sorted() để lấy bản sao của các khóa theo thứ tự:
```py
fav_languages = {
    'jen': 'python',            # Edward, thank you for taking the poll.
    'sarah': 'c',               # Jen, thank you for taking the poll.
    'edward': 'ruby',           # Phil, thank you for taking the poll.
    'phil': 'python',           # Sarah, thank you for taking the poll.
}
for name in sorted(fav_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
```
### Lặp qua tất cả các giá trị trong từ điển
Giả sử chúng ta chỉ muốn có một danh sách tất cả các ngôn ngữ được chọn trong cuộc thăm dò ngôn ngữ lập trình mà không có tên của người đã chọn từng ngôn ngữ
```py
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
# The following languages have been mentioned:
# Python
# C
# Python
# Ruby
```
### Kiểu dữ liệu set
Set là một tập hợp có thể chứa nhiều các phần tử và các phần tử này không có thứ tự. Thực tế set không được sử dụng nhiều bằng LIST hay TUPLE.
Một Set gồm các yếu tố sau:
- Được giới hạn bởi cặp ngoặc {}, tất cả những gì nằm trong đó là
những phần tử của Set.
- Các phần tử của Set được phân cách nhau ra bởi dấu phẩy (,).
- Set không chứa nhiều hơn 1 phần tử trùng lặp

Set có thể thay đổi (thêm bớt phần tử) nhưng các phần tử của tập hợp phải ở dạng không thể thay đổi (tức là xác định được dung lượng bộ nhớ ngay khi khai báo).
Sử dụng các dấu ngoặc nhọn {} trong khai báo Set, ví dụ:
```py
friends = {"Rolf","Bob","Anne"}
print(friends)
```
***Chú ý:***
- **[]** sử dụng khai báo **List**
- **()** sử dụng khai báo **Tuple**
- **{}** sử dụng khai báo **Set**

#### Phương thức kiểu dữ liệu set
- Phương thức .add()
- Phương thức .remove()
- Phương thức .discard()
- Phương thức .pop()
- Phương thức .clear()
- (...)

Set là một tập hợp trong đó mỗi mục phải là duy nhất. VD:
```py
favorite_languages = {                  # The following languages have been mentioned:
    'jen': 'python',                    # Python
    'sarah': 'c',                       # C
    'edward': 'ruby',                   # Ruby
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
```

## Nesting
- Đôi khi chúng ta muốn lưu trữ nhiều từ điển trong một danh sách hoặc một danh sách các mục dưới dạng một giá trị trong từ điển. Điều này được gọi là nesting.
- Chúng ta có thể lồng các từ điển vào bên trong một danh sách, một danh sách các mục bên trong một từ điển, hoặc thậm chí một từ điển bên trong một từ điển khác. Nesting là một tính năng mạnh mẽ, như các ví dụ sau đây sẽ chứng minh điều đó.

### Danh sách các từ điển
Làm thế nào ta có thể quản lý một đội alien? Một cách là lập danh
sách alien, trong đó mỗi alien là một từ điển thông tin về alien đó
```py
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}    
aliens = [alien_0, alien_1, alien_2]    # {'color': 'green', 'points': 5}
for alien in aliens:                    # {'color': 'yellow', 'points': 10}
    print(alien)                        # {'color': 'red', 'points': 15}
```
VD khác:
```py
# Make an empty list for storing aliens.
aliens = [] 
# Make 30 green aliens
for alien_number in range(30): .
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)      

for alien in aliens[0:2]:               # {'color': 'red', 'points': 15, 'speed': 'fast'}
    if alien['color'] == 'green':       # {'color': 'red', 'points': 15, 'speed': 'fast'}
        alien['color'] = 'yellow'       # {'color': 'yellow', 'points': 10, 'speed': 'medium'}
        alien['speed'] = 'medium'       # {'color': 'green', 'points': 5, 'speed': 'slow'}
        alien['points'] = 10            # {'color': 'green', 'points': 5, 'speed': 'slow'}
    elif alien['color'] == 'yellow':    # ...
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:5]: # Show the first 5 aliens.
    print(alien)
print("...")
```
### Danh sách trong từ điển
Có thể lồng một danh sách vào bên trong từ điển bất kz lúc nào ta muốn nhiều giá trị được liên kết với một khóa duy nhất trong từ điển
```py
fav_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in fav_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
# Jen's favorite languages are:
# Python
# Ruby
# Sarah's favorite languages are:
# C
# Phil's favorite languages are:
# Python
# Haskell
# Edward's favorite languages are:
# Ruby
# Go
```
### Từ điển bên trong từ điển
Chúng ta có thể lồng một từ điển bên trong một từ điển khác, nhưng code có thể trở nên phức tạp nhanh chóng khi ta làm như vậy.
```py
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
```
### Sử dụng vòng lặp while với từ điển
    • Để theo dõi nhiều người dùng và các thông tin, chúng ta sẽ cần sử dụng danh sách và từ điển với vòng lặp while.
    • Vòng lặp for có hiệu quả để lặp qua một danh sách, nhưng chúng ta không nên sửa đổi danh sách bên trong vòng lặp for vì Python sẽ gặp khó khăn trong việc theo dõi các phần tử trong danh sách.
    • Để sửa đổi danh sách khi ta làm việc với nó, nên sử dụng vòng lặp while. Sử dụng vòng lặp while với danh sách và từ điển cho phép ta thu thập, lưu trữ và tổ chức nhiều đầu vào để kiểm tra và báo cáo về sau

# VII. Function
## Định nghĩa Hàm
Cấu trúc đơn giản nhất của một hàm:
```py
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()
```
Dòng lệnh đầu tiên sử dụng từ khóa def để thông báo cho Python rằng ta đang định nghĩa một hàm.
Bất kỳ dòng thụt lề nào theo sau def greet_user(): tạo nên phần thân của hàm
Dòng """Display a simple greeting.""" là một chú thích được gọi là mỗi chuỗi tài liệu (docstring)
Dòng print("Hello!") Là dòng code duy nhất trong phần thân của hàm này, vì vậy, greet_user() chỉ có một lệnh: print(“Hello!").
### Truyền thông tin tới một hàm
Để truyền thông tin tới một hàm, nhập tham số username trong dấu ngoặc đơn định nghĩa hàm.
Hàm yêu cầu ta cung cấp một giá trị cho username mỗi khi gọi nó 
```py
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
greet_user('jesse') #Hello, Jesse!
``` 
Lệnh `greet_user('jesse')` sẽ gọi hàm greet_user() và cung cấp cho hàm thông tin cần thiết để thực hiện lệnh gọi print(). Hàm chấp nhận tên được chuyển và hiển thị lời chào cho tên đó
### Đối số và tham số
- Biến username của greet_user() là một ví dụ về một tham số, một phần thông tin mà hàm cần để thực hiện công việc của nó.
- Giá trị 'jesse' trong greet_user('jesse') là một ví dụ về đối số. Đối số là một phần thông tin được truyền từ một lệnh gọi hàm đến một hàm. Khi chúng ta gọi hàm, chúng ta đặt giá trị mà chúng ta muốn hàm hoạt động trong dấu ngoặc đơn.
- Trong trường hợp này, đối số 'jesse' đã được chuyển đến hàm greet_user() và giá trị được gán cho tham số username.
### Truyền tham số
- Bởi vì một định nghĩa hàm có thể có nhiều tham số, một lệnh gọi hàm có thể cần nhiều đối số. Chúng ta có thể truyền các đối số cho các hàm của mình theo một số cách.
- Ta có thể sử dụng các đối số có vị trí, các đối số này cần theo cùng thứ tự mà các tham số đã được viết; các đối số từ khóa, trong đó mỗi đối số bao gồm một tên biến và một giá trị; và danh sách và từ điển các giá trị.
### Đối số có vị trí
Khi gọi một hàm, Python phải khớp từng đối số trong lệnh gọi hàm với một tham số trong định nghĩa hàm. Cách đơn giản nhất để làm điều này là dựa trên thứ tự của các đối số được cung cấp
```py
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
# I have a hamster.
# My hamster's name is Harry.
```
### Đối số từ khóa
- Đối số từ khóa là một cặp tên-giá trị được truyền cho một hàm.
- Chúng ta liên kết trực tiếp tên và giá trị bên trong đối số, vì vậy khi ta truyền đối số vào hàm, sẽ không có sự nhầm lẫn nào
```py
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamster', pet_name='harry')
```
- Thứ tự của các đối số từ khóa không quan trọng vì Python biết mỗi giá trị sẽ đi đến đâu. Hai lệnh gọi hàm sau đây là tương đương : 
    - `describe_pet(animal_type='hamster', pet_name='harry')`
    - `describe_pet(pet_name='harry', animal_type='hamster')`
### Giá trị mặc định
- Khi viết một hàm, ta có thể xác định một giá trị mặc định cho mỗi tham số. Nếu một đối số cho một tham số được cung cấp trong lệnh gọi hàm, thì Python sẽ sử dụng giá trị đối số. Nếu không, nó sử dụng giá trị mặc định của thông số.
- Khi xác định giá trị mặc định cho một tham số, ta có thể loại trừ đối số tương ứng
mà ta thường viết trong lệnh gọi hàm.
```py
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')
# I have a dog.
# My dog's name is Willie.
```
Để mô tả một con vật không phải con chó, ta có thể sử dụng một lệnh gọi hàm như sau:
`describe_pet(pet_name='harry', animal_type='hamster')`
Bởi vì một đối số rõ ràng cho animal_type được cung cấp, Python sẽ bỏ qua giá trị mặc định của tham số.
*Ghi chú:* Khi ta sử dụng giá trị mặc định, bất kỳ thông số nào có giá trịmặc định cần được liệt kê sau tất cả các tham số không có giá trị mặc định. Điều này cho phép Python tiếp tục diễn giải các đối số vị trí một cách chính xác.
### Lệnh gọi hàm tương đương
Bởi vì các đối số vị trí, đối số từ khóa và giá trị mặc định đều có thể được sử dụng cùng nhau, nên thường ta sẽ có một số cách tương đương để gọi một hàm.
```py
def describe_pet(pet_name, animal_type='dog'):
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
```
### Tránh lỗi đối số
Các đối số không khớp xảy ra khi ta cung cấp ít hoặc nhiều đối số hơn một hàm
cần thực hiện công việc của nó
```py
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet()
# Traceback (most recent call last):
#   File "d:\CODE\CODEPTIT.py", line 22, in <module>
#     describe_pet()
# TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'
```
### Giá trị trả về
- Không phải lúc nào một hàm cũng phải hiển thị trực tiếp đầu ra của nó. Thay vào đó, nó có thể xử lý một số dữ liệu và sau đó trả về một giá trị hoặc tập hợp các giá trị.
- Giá trị mà hàm trả về được gọi là giá trị trả về. Câu lệnh trả về nhận một giá trị từ bên trong một hàm và gửi trở lại dòng được gọi là hàm. 
- Giá trị trả về cho phép ta chuyển phần lớn công việc khó khăn của chương trình sang các hàm, điều này có thể đơn giản hóa phần nội dung chương trình của mình.
### Trả về giá trị đơn
Hãy xem xét một hàm lấy họ và tên và trả về tên đầy đủ
```py
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted. """
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)     # Jimi Hendrix
```
Khi ta gọi một hàm trả về một giá trị, ta cần cung cấp một biến mà giá trị trả về có thể được
gán cho. Trong trường hợp này, giá trị trả về được gán cho biến musician.
