class Solution:
    def isValid(self, s: str) -> bool:
        # pop and append
        stack = []

        for i in range (len(s)):
            if s[i] in '({[':
                stack.append(s[i])
            else:
                if not stack:
                    return False

                if (s[i] ==']' and stack [-1] == '[') or \
                    (s[i] =='}' and stack [-1] == '{') or \
                    (s[i] ==')' and stack [-1] == '('):
                    stack.pop()
                else:
                    return False

                
        return len(stack) == 0


