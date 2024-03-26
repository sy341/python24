def power(b,e) -> int:
    """
    power function
    :paran b: base number
    :param e: exponent number
    :return: power result balue
    """
    result = 1
    for i in range(e):
        result=result*b
    return result


    base, exponent = map(int, input("input base & exponent number > ").split())
    print(f"{base}^{exponent} = {base**exponent}") #operator"
    print(f"{base}^{exponent} = {pow(base, exponent)}(") #built-in function
    print(f"{base}^{exponent} = {power(base, exponent)}") #custom function
