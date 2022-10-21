"""
Правильная скобочная последовательность
"""


def isValid(_str) -> bool:
    """Совпадают ли скобки

    Args:
        _str (string): строка состоящая из скобок

    Returns:
        bool: является ли строка правильной
    """    
    bracket_tuple = "()", "{}", "[]"
    while any(two_chars in _str for two_chars in bracket_tuple):
        for bracket in bracket_tuple:
            _str = _str.replace(bracket, "")
    return _str == ""


print(isValid("()[]{}"))
print(isValid("{[]}"))
print(isValid("((()(())))"))
print(isValid("(]"))
print(isValid("([)]"))

