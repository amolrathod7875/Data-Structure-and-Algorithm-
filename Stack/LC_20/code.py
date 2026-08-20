from typing import Any 

class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for char in s :
            if char == '(' or char == '[' or char == '{':
                st.append(char)
            elif char == ')' or char == ']' or char == '}':
                if not st:
                    return False
                top = st[-1]
                if (
                    (char == ')' and top != '(') or
                    (char == ']' and top != '[') or
                    (char == '}' and top != '{')
                ):
                    return False
                st.pop()
        return not st