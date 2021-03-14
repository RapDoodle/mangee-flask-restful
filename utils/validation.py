import re
from validate_email import validate_email

def verify_regex(regex: str, d: str) -> bool:
    d = str(d)
    regex = re.compile(regex)
    if regex.match(d) is None:
        return False
    return True

def is_money(d: str) -> bool:
    return verify_regex('^[0-9]+(\.[0-9]{1,2})?$', d)

def is_rating(d):
    # A rating should be an integer between 1 and 5
    return verify_regex('^[1-5]$', d)

def is_valid_email(d: str):
    return validate_email(d)

def is_valid_length(d: str, min: int, max: int) -> bool:
    # The function checks whether d's length is in the range [min, max]
    d = str(d)
    if (len(d) >= min and len(d) <= max):
        return True
    return False

def is_valid_username(
        d: str, min_len: int = 6, max_len: int = 24, 
        allow_lower: bool = True, allow_upper: bool = True,
        allow_digit: bool = True, allow_underscore: bool = True,
        allow_dash: bool = True) -> bool:
    return verify_regex(f"^[{'a-z' if allow_lower else ''}" + 
                        f"{'A-Z' if allow_upper else ''}" + 
                        f"{'0-9' if allow_digit else ''}" +
                        f"{'_' if allow_underscore else ''}" + 
                        f"{'-' if allow_dash else ''}" + 
                        f"]{{{min_len},{max_len}}}$", d)

def is_valid_password(
        d: str, min_len: int = 8, max_len: int = 24, 
        require_upper: bool = True, require_lower: bool = True, 
        require_digit: bool = True, 
        require_special_char: bool = False) -> bool:    
    assert min_len < max_len
    return verify_regex(f"^{'(?=.*[a-z])' if require_lower else '' }" + 
                        f"{'(?=.*[A-Z])' if require_upper else ''}" +
                        f"{'(?=.*[0-9])' if require_digit else ''}" +
                        f"{'(?=.*[#?!@$ %^&*-])' if require_special_char else ''}" +
                        f".{{{min_len},{max_len}}}$", d)
