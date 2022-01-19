def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    swapped = to_swap.swapcase()
    fixed = [char.swapcase() if char in (to_swap, swapped) else char for char in phrase]
    return ''.join(fixed)