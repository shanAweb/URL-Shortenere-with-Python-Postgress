from db import get_connection, get_original_url
import string
import random
combination = string.ascii_letters+ string.digits
def generate_short_code():
    short_code = ''.join(random.choices(combination, k=6))
    return short_code

def check_short_code():
    short_code = generate_short_code()
    check_code = get_original_url(short_code=short_code)

    if check_code:
        print("Short Code already exist, generating a new one")
        return check_short_code()
    else:
        return short_code

if __name__ == "__main__":
    print(check_short_code())
