number = int(input("Input number : "))

is_prime_number = True #which represents "count"
if number < 2:
    is_prime_number = False
else:
    #for i in range(2, number+1):
    i = 2
    while i*i < number:
        if number % i == 0:
            is_prime_number = False
            #count += 1
            break #Exit the loop when the first divisor is found.
            # Performance is improved when the input value is not a prime number.
        print(i, end=" ")
        i += 1

if count == 0:
    print(f"{number} is prime number~")
else:
    print(f"{number} is NOT prime number!")