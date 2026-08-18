class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        n = len(s)
        nums = []   # operand stack
        ops = []    # operator stack: '+', '-', '('

        def apply():
            b = nums.pop()
            a = nums.pop()
            op = ops.pop()
            if op == '+':
                nums.append(a + b)
            else:  # '-'
                nums.append(a - b)

        i = 0
        while i < n:
            ch = s[i]
            if ch.isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                nums.append(num)
                continue
            elif ch == '(':
                ops.append(ch)
            elif ch == ')':
                while ops and ops[-1] != '(':
                    apply()
                ops.pop()                      # discard '('
            elif ch in '+-':
                is_unary = (i == 0) or (s[i - 1] in '+-(')
                if ch == '-' and is_unary:
                    nums.append(0)             # represent unary minus as 0 - x
                    ops.append('-')
                elif ch == '+' and is_unary:
                    pass                       # unary plus is a no-op
                else:
                    # binary: flush equal-precedence operators first
                    while ops and ops[-1] in '+-':
                        apply()
                    ops.append(ch)
            i += 1

        while ops:
            apply()

        return nums[0]