def remove_exclamation_marks(s):
    return s.replace("!", "")

def correct(s):
    return s.replace("5","S").replace("0","O").replace("1","I")

def is_palindrome(s):
    s=s.lower()
    if s == s[::-1]:
        return True
    return False