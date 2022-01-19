def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if (type(a) is int or type(a) is float) and (type(b) is int or type(bin) is float):
        if a == b:
            return 'Numbers are equal.'
        elif a < b:
            return 'Second is greater.'
        else:
            return "First is greater."
    return 'Both a and b must be int or float.'