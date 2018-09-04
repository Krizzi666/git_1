
n = int(input("Enter the length of the sequence: ")) # Do not change this line

first_num = 1
second_num = 2
last_num = 3
counter = 1

if counter <= 3:
    print(first_num)
    print(2)
    print(3)
    

while n > 0 and counter < n:
    summa = last_num + second_num + first_num
    first_num = second_num
    second_num = last_num
    last_num = summa
    print(summa)
    counter += 1