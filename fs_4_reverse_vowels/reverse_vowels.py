def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = set('aeiou')

    # Collect the vowels in string s into vowels_str.
    vowels_str = ''
    for char in s:
        if char.lower() in vowels:
            vowels_str += char

    # Make a reversed iterable of vowels_str into vowels_in_str.
    vowels_in_str = reversed(vowels_str)

    # Iterate through string s replacing each vowel with its reverse into reveresd_str.
    reversed_str = ''
    for char in s:
        if char.lower() in vowels:
            reversed_str += next(vowels_in_str)
        else:
            reversed_str += char

    return reversed_str
