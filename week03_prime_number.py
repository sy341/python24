test = input("input start number : ").split()
# print (int(test[0]), int(test[1]))

start = int(test[0])
end = int(test[1])

for k in range (start, end+1):
    is_prime_number = True
    if k < 2:
        is_prime_number = False
    else:
        i = 2
        while i*i <= k:
            if k % i == 0:
                is_prime_number = False
                break
            i = i +1
        if is_prime_number: print(k, end=' ')

is_prime_number = True  #Change variable name to count->is_prime_number for readability.
if number < 2:
    is_prime_number = False
else:
    #for i in range(2,number):
    i = 2
    while i*i <= number:  #bug fix
        if number % i == 0:
            #is_prime_number = is_prime_number +1
            is_prime_number = False #Remove addition operation
            break #Exit the loop when the first divisor is found. Performance is improved when the input is not prime number.
            print(i, end+' ')
            i = i + 1

