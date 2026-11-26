class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n_str = str(n)
        
        x_str = "".join(digit for digit in n_str if digit != '0')
        
        if not x_str:
            x = 0
            sum_of_digits = 0
        else:
            x = int(x_str)
            sum_of_digits = sum(int(digit) for digit in x_str)
            
        result = x * sum_of_digits
        return result