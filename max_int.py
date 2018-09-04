
num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code

max_int = 1
number = 1

while num_int > 0:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int > max_int and num_int > 0:
        max_int = num_int
    continue

print("The maximum is", max_int)    # Do not change this line
