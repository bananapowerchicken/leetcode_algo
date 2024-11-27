# https://leetcode.com/problems/valid-parentheses/description/
# easy


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    open_bracket_stack = []
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']

    if s:
        if s[0] in close_brackets:
            return False
        for el in s:
            if el in open_brackets:
                open_bracket_stack.append(el)
            elif el in close_brackets:
                if open_bracket_stack != []:
                    if open_brackets.index(open_bracket_stack[-1]) == close_brackets.index(el):
                        open_bracket_stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                return False
            
    return open_bracket_stack == []

def test():
    isValid('([])')


if __name__ == "__main__":
    test()

# ()
# ()[]{}
# (])