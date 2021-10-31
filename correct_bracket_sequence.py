import A_stack


def is_bracket_sequence_correct(s: str):
    """
    Проверяет корректность скобочной последовательности
    из клуглых и квадратных скобок () []

    >>> is_bracket_sequence_correct("((([])))[]")
    True
    >>> is_bracket_sequence_correct("([)]")
    False
    >>> is_bracket_sequence_correct("()[")
    False
    >>> is_bracket_sequence_correct("]")
    False
    """
    for bracket in s:
        if bracket not in "()[]":
            continue
        if bracket in "([":
            A_stack.push(bracket)
        else:
            assert bracket in ")]", "Fail!"
            if A_stack.is_empty():
                return False
            left = A_stack.pop()
            assert left in "([", "Fail!"
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            if right != bracket:
                return False
    return A_stack.is_empty()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
