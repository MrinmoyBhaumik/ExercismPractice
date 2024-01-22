def is_paired(input_string):
    stack = []
    open_brackets = "[{("
    close_brackets = "]})"
    for char in input_string:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack:
                return False
            top = stack.pop()
            if open_brackets.index(top) != close_brackets.index(char):
                return False
    return not stack