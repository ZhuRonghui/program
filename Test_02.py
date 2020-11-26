sum_num = count = 0
n_list = []
while 1:
    num = input("Enter a number:")
    try:
        num = int(num)
        sum_num = sum_num + num
        n_list.append(num)
        count = count + 1
    except:
        if num == "done":
            n_list.sort()
#            print(sum_num, count, sum_num / count)
            print(sum_num,count,n_list[-1],n_list[0])
            break
        else:
            print("Invalid input")
