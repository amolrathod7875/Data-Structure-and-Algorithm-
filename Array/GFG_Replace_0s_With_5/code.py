class Solution:
    def convertFive(self, n):
        """Replace every 0 digit in `n` with 5 and return the resulting number.

        Digits are processed from least significant to most significant. Each
        zero is replaced by 5 before being reassembled at its original place
        value.
        """
        if n == 0:
            return 5

        result = 0
        place = 1
        while n > 0:
            digit = n % 10
            if digit == 0:
                digit = 5

            result += digit * place
            place *= 10
            n //= 10
        return result