def is_prime_number(n) -> bool:
    """
    prime umber determination function
    :param n: a positive integer
    :return: Returns Ture if it is a prime number, and returns False if it is not a prime number.
    """
    #is_prime_number = True
    if k < 2:
        #is_prime_number = False
        return False
    else:
        i = 2
        while i *i <= k:
            if k % i == 0:
                #is_prime_number = False
                #break
                return False
            i = i +1
        return True
    pass


start, end = list(map(int, input("input start number : ").split()))

for k in range (start, end+1):
        if is_prime_number(k): print(k, end=' ')


