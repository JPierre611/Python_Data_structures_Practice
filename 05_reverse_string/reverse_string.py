def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    if type(phrase) is str:
        return phrase[::-1]
    return 'Phrase must be a string.'