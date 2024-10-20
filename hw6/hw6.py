def exercise1(a, b):
    print("Exercise 1: two-sum: Start")
    print(f'Input: {a}, {b}')
    c = a + b
    print(f'Output: {c}')
    print("Exercise 1: Complete")
    return c

def exercise2(s):
    print("Exercise 2: reverse-string: Start")
    print(f'Input: {s}')
    s_reversed = s[::-1]
    print(f'Output: {s_reversed}')
    print("Exercise 2: Complete")
    return s_reversed

def exercise3(s):
    print("Exercise 3: string-length: Start")
    print(f'Input: {s}')
    s_len = len(s)
    print(f'Output: {s_len}')
    print("Exercise 3: Complete")
    return s_len

def exercise4(s1, s2):
    print("Exercise 4: concatenate-string: Start")
    print(f'Input: {s1}, {s2}')
    s_concat = s1 + s2
    print(f'Output: {s_concat}')
    print("Exercise 4: Complete")
    return s_concat

def exercise5(s):
    print("Exercise 5: is-vowel: Start")
    print(f'Input: {s}')
    VOWELS = 'aeiou'
    is_vowel = s.lower() in VOWELS
    print(f'Output: {is_vowel}')
    print("Exercise 5: Complete")
    return is_vowel

def exercise6(s):
    print("Exercise 6: swap-first-last: Start")
    print(f'Input: {s}')
    s_swapped = f'{s[-1]}{s[1:-2]}{s[0]}'
    print(f'Output: {s_swapped}')
    print("Exercise 6: Complete")
    return s_swapped

def exercise7(s):
    print("Exercise 7: to-uppercase: Start")
    print(f'Input: {s}')
    s_uppercase = s.upper()
    print(f'Output: {s_uppercase}')
    print("Exercise 7: Complete")
    return s_uppercase

def exercise8(length, width):
    print("Exercise 8: rectangle-area: Start")
    print(f'Input: {length}, {width}')
    area = length * width
    print(f'Output: {area}')
    print("Exercise 8: Complete")
    return area

def exercise9(n):
    print("Exercise 9: is-even: Start")
    print(f'Input: {n}')
    is_even = n % 2 == 0
    print(f'Output: {is_even}')
    print("Exercise 9: Complete")
    return is_even

def exercise10(s):
    print("Exercise 10: extract-first-three: Start")
    print(f'Input: {s}')
    s_three = s[:3]
    print(f'Output: {s_three}')
    print("Exercise 10: Complete")
    return s_three

def exercise11(name: str, age: int):
    print("Exercise 11: string-interpolation: Start")
    print(f'Input: {name}, {age}')
    s_interpolated = 'My name is {name} and I am {age} years old.'
    print(f'Output: {s_interpolated}')
    print("Exercise 11: Complete")
    return s_interpolated

def exercise12(s):
    print("Exercise 12: string-slicing: Start")
    print(f'Input: {s}')
    s_sliced = s[1:5]
    print(f'Output: {s_sliced}')
    print("Exercise 12: Complete")
    return s_sliced

def exercise13(s):
    print("Exercise 13: type-conversion: Start")
    print(f'Input: {s}, type: {type(s)}')
    s_integer = int(s)
    print(f'Output: {s_integer}, type: {type(s_integer)}')
    print("Exercise 13: Complete")
    return s_integer

def exercise14(s):
    print("Exercise 14: string-repetition: Start")
    print(f'Input: {s}')
    s_repeated = s * 3
    print(f'Output: {s_repeated}')
    print("Exercise 14: Complete")
    return s_repeated

def exercise15(a, b):
    print("Exercise 15: calculate-quotient-remainder: Start")
    print(f'Input: {a}, {b}')
    quotient = a // b
    remainder = a % b
    print(f'Output: quotient = {quotient}, remainder = {remainder}')
    print("Exercise 15: Complete")
    return quotient, remainder

def exercise16(a, b):
    print("Exercise 16: float-division: Start")
    print(f'Input: {a}, {b}')
    division = a / b
    print(f'Output: {division}')
    print("Exercise 16: Complete")
    return division

def exercise17(s, c):
    print("Exercise 17: string-methods: Start")
    print(f'Input: string = {s}, character = {c}')
    s_count = s.count(c)
    print(f'Output: {s_count}')
    print("Exercise 17: Complete")
    return s_count

def exercise18(s_main, s_include):
    print("Exercise 18: escape-sequences: Start")
    print(f'Input: {s_main}, to include {s_include}')
    s_escaped = f"{s_main} \"{s_include}\""
    print(f'Output: {s_escaped}')
    print("Exercise 18: Complete")
    return s_escaped

def exercise19(s_line_top, s_line_bottom):
    print("Exercise 19: multi-line-string: Start")
    print(f'Input: {s_line_top}, {s_line_bottom}')
    s_multiline = f"""{s_line_top}
        {s_line_bottom}"""
    print(f'Output: {s_multiline}')
    print("Exercise 19: Complete")
    return s_multiline

def exercise20(a, b):
    print("Exercise 20: exponentiation: Start")
    print(f'Input: {a}, {b}')
    exponent = a ** b
    print(f'Output: {exponent}')
    print("Exercise 20: Complete")
    return exponent

def exercise21(s):
    print("Exercise 21: is-palindrome: Start")
    print(f'Input: {s}')
    is_palindrome = s[::-1].lower() == s.lower()
    print(f'Output: {is_palindrome}')
    print("Exercise 21: Complete")
    return is_palindrome

def exercise22(str1, str2):
    print("Exercise 22: check-anagrams: Start")
    print(f'Input: {str1}, {str2}')
    from collections import Counter
    is_anagram = Counter(str1) == Counter(str2)
    print(f'Output: {is_anagram}')
    print("Exercise 22: Complete")
    return is_anagram


if __name__ == "__main__":
    exercise1(3, 5)
    print()
    exercise2('PythonBackEndCourse')
    print()
    exercise3('ThisTextHasThirtyCharacters')
    print()
    exercise4('String1', 'String2')
    print()
    exercise5('W')
    exercise5('e')
    print()
    exercise6('SwapThisString')
    print()
    exercise7('ThIs tExt nEedS soME UpPpeRcAse')
    print()
    exercise8(length=5, width=7)
    print()
    exercise9(18)
    exercise9(9779)
    print()
    exercise10('BaursakIsLove')
    print()
    exercise11('Nurlybek', 31)
    print()
    exercise12('PythonBackEndCourse')
    print()
    exercise13('42')
    print()
    exercise14('Teststring')
    print()
    exercise15(15, 4)
    print()
    exercise16(15, 4)
    print()
    exercise17('Parallel', 'l')
    print()
    exercise18('Outside text', 'Text to include')
    print()
    exercise19('Topline string.', 'Underline string.')
    print()
    exercise20(5, 2)
    print()
    exercise21('racecar')
    exercise21('bunny')
    print()
    exercise22('spar', 'rasp')
    exercise22('racecar', 'bunny')
