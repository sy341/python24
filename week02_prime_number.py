m=number = int(input("input number : "))
print (number -3 )

if number < 2:
    is_prime_number = True  #Change variable name to count->is_prime_number for readability.
else:
    is_prime_number = False
    for i in range(2,number):
        if number % i == 0:
            #is_prime_number = is_prime_number +1
            is_prime_number = False #Remove addition operation
            break #Exit the loop when the first divisor is found. Performance is improved when the input is not prime number.
            print(i, end+' ')

# if count == 2:
if is_prime_number: #Remove comparison (equal) operator
    print(f"{number} is prime number~")
else:
    print(f"{number} is NOT prime number!")