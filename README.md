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
