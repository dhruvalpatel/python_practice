"""Check whether a string is palindrome or not?"""


def is_palindrome(s):
    """Matching with revers string."""
    return s == s[::-1]


def is_palindrome_method_2(s):
    """Matching ith character from front-back."""
    len_of_string = len(s)
    for i in range(0, len_of_string):
        if not s[i] == s[len_of_string - i - 1]:
            return False
    return True


s1 = "malayalam"
print("is_palindrome ", is_palindrome(s1))
print("is_palindrome_method_2: ", is_palindrome_method_2(s1))
s2 = "Hindi"
print("is_palindrome ", is_palindrome(s2))
print("is_palindrome_method_2: ", is_palindrome_method_2(s2))
