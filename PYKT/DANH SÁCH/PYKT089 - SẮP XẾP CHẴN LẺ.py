# Cho dãy số A[] có n phần tử. 
# Hãy sắp xếp các số chẵn trong dãy theo thứ tự tăng dần 
#                      và các số lẻ theo thứ tự giảm dần.
# In ra dãy kết quả đã sắp xếp trong đó 
#     vị trí số chẵn và vị trí số lẻ không thay đổi so với dãy ban đầu.

# Input
#     Dòng đầu ghi số n (1 < n ≤ 1000)
#     Các dòng tiếp theo ghi đủ n số của dãy A[], 
#         các số đều nguyên dương và không quá 1000.
# Output
#     Ghi ra dãy kết quả đã sắp xếp trong đó các vị trí của số chẵn và số lẻ không thay đổi.

#     Input                   Output
#     10
#     1 2 3 4 5 6 7 7 9 6     9 2 7 4 7 6 5 3 1 6

n = int(input())
a = []
while len(a)<n:
    a.extend(list(map(int, input().split())))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]%2==0:
            if a[j]%2==0:
                if a[i]>a[j]:
                    tmp = a[i]
                    a[i] = a[j]
                    a[j] = tmp 
        else:
            if a[j]%2==1:
                if a[i]<a[j]:
                    tmp = a[i]
                    a[i] = a[j]
                    a[j] = tmp
for i in a: print(i,end=' ')
