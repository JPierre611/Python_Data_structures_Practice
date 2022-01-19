def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    num1_str = str(num1)
    num2_str = str(num2)
    
    num1_digits = set(num1_str)
    num2_digits = set(num2_str)

    frequency1 = {digit1: num1_str.count(digit1) for digit1 in num1_digits}
    frequency2 = {digit2: num2_str.count(digit2) for digit2 in num2_digits}

    return frequency1 == frequency2