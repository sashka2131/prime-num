def prime_num(num):
    if num < 1:
        return print("Error!\nEnter number bigger than 0")
    elif 1 <= num <= 2:
        return print(num)
    else:
        num_arr = [i for i in range(2, num+1)]
        print(num_arr)
        for i in num_arr:
            for j in num_arr:
                if j % i == 0 and j != i:
                    num_arr.remove(j)
        print(num_arr)


print("Enter number bigger than 0")
prime_num(int(input()))