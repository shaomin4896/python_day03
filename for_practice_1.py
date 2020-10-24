#1 - 印出0-10
for i in range(0,11,1):
    print(i)
print('--------')
#2 - 印出0-100之間的偶數
for i in range(0,101,2):
    print(i)
print('--------')
#3 - 印出100-50之間的偶數    
for i in range(50,101,2):
    print(i)
print('---------')
#4 - 串列家總及平均
ls = [80,75,98,69,83,92]
total = 0
average = 0
for i in ls:
    total += i
print(total)
average = total / len(ls)
print(average)
#4 - 串列家總及平均
total = 0
average = 0
for i in range(len(ls)):
    total += ls[i]
print(total)
print(total/len(ls))
# 絕招
total = sum(ls)
print(total)
print(total/len(ls))
print('---------')
#5 - 印星星
for i in range(0,10):
    string = ""
    for i in range(0,10):
        string += "*"
    print(string)
print("---------")
for i in range(1,11):
    print(' '*(10-i)+'*'*i)
print("-------------")
for i in range(0,10):
    print(' '*(10-i)+'*'*i*2+'*')
#3_1 挑戰費式數列 <= 100
num_list = [1,1]
for i in range(9999):
    num = num_list[len(num_list)-1] + num_list[len(num_list)-2]
    if num <= 100:
        num_list.append(num)
print(num_list)
#3_2 挑戰質數 2-100
for i in range(2,101):
    flag = True
    for x in range(2,i):
        if i % x == 0:
            flag = False
    if flag:
        print(i)

