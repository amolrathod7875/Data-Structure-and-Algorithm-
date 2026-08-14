import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from code import evaluateInfix

def test_evaluateInfix():
    test_cases = [
        (["2", "+", "3"], 5, "Simple addition"),
        (["10", "-", "3"], 7, "Simple subtraction"),
        (["4", "*", "5"], 20, "Simple multiplication"),
        (["10", "/", "2"], 5, "Simple integer division"),
        (["2", "+", "3", "*", "4"], 14, "Precedence: multiplication before addition"),
        (["(", "2", "+", "3", ")", "*", "4"], 20, "Parentheses"),
        (["2", "^", "3"], 8, "Exponentiation"),
        (["2", "^", "3", "^", "2"], 512, "Right-associative exponentiation"),
        (["100", "+", "200", "/", "2", "*", "5", "+", "7"], 607, "Complex expression"),
        (["42"], 42, "Single number"),
        (["2", "*", "(", "3", "+", "4", ")"], 14, "Nested parentheses"),
        (["10", "-", "3", "-", "2"], 5, "Left-associative subtraction"),
        (["1", "+", "2", "*", "3", "-", "4", "/", "2"], 5, "Mixed operators"),
        (["-5", "+", "3"], -2, "Negative number operand"),
        (["(", "(", "2", "+", "3", ")", "*", "4", ")", "+", "1"], 21, "Double parentheses"),
        (["5", "*", "(", "2", "+", "3", ")", "^", "2"], 125, "Parentheses with exponent"),
        (["16", "/", "2", "/", "2"], 4, "Left-associative division"),
    ]

    passed = 0
    failed = 0

    for arr, expected, description in test_cases:
        try:
            result = evaluateInfix(arr)
            if isinstance(expected, int) and isinstance(result, float):
                match = result.is_integer() and int(result) == expected
            else:
                match = result == expected

            if match:
                print(f"PASS: {description} -> {result}")
                passed += 1
            else:
                print(f"FAIL: {description} -> Expected {expected}, got {result}")
                failed += 1
        except Exception as e:
            print(f"ERROR: {description} -> {e}")
            failed += 1

    print(f"\n{passed} passed, {failed} failed")
    return failed == 0

if __name__ == "__main__":
    success = test_evaluateInfix()
    sys.exit(0 if success else 1)