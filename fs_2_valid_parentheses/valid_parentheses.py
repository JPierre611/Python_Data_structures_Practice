def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    opened = 0
    closed = 0

    for char in parens:
        if char == '(':
            opened += 1
        elif char == ')':
            closed += 1
        if closed > opened:
            return False
    return opened == closed