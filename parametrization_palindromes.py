


def is_palindrome(is_it_palindrome) -> bool:
    reverse = is_it_palindrome[::-1]
    if reverse.lower() == is_it_palindrome.lower():
        return True
    else:
        return False
