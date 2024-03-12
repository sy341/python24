m=number = int(input("input number : "))

is_prime_number = True  #Change variable name to count->is_prime_number for readability.
if number < 2:
    is_prime_number = False
else:
    #for i in range(2,number):
    i = 2
    while i*i < number:  #reduce loop operation
        if number % i == 0:
            #is_prime_number = is_prime_number +1
            is_prime_number = False #Remove addition operation
            break #Exit the loop when the first divisor is found. Performance is improved when the input is not prime number.
            print(i, end+' ')
            i = i + 1

# if count == 2:
if is_prime_number: #Remove comparison (equal) operator
    print(f"{number} is prime number~")
else:
    print(f"{number} is NOT prime number!")