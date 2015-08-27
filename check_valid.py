# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    str_stack = []
    for element in s:
        if element in ["(", "{", "["]:
            str_stack.append(element)
        if element in [")", "}", "]"]:
            if len(str_stack) == 0:
                return False
            if element == ")":
                ceil = str_stack.pop()
                if ceil != "(":
                    return False
            if element == "}":
                ceil = str_stack.pop()
                if ceil != "{":
                    return False
            if element == "]":
                ceil = str_stack.pop()
                if ceil != "[":
                    return False
    if len(str_stack) > 0:
        return False
    return True

if __name__ == "__main__":
    print isValid("[((]")