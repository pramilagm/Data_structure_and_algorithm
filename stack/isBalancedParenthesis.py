def isBalanced(exp):
    stack = []

    # Traversing the Expression
    for char in exp:
        if char in ["(", "{", "["]:
            # Push the element in the stack
            stack.append(char)
        else:
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if len(stack) == 0:
                return False
            current_char = stack.pop()

            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    # Check Empty Stack
    if len(stack) == 0:
        return True
    else:
        return False


expr = "{()}[]"
ex = "{([])}"
e = "[{}{})(]"
st = "{[]{()}}"
print(isBalanced(expr))
print(isBalanced(ex))
print(isBalanced(e))
print(isBalanced(st))
