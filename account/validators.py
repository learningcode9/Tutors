from django.core.exceptions import ValidationError
import re


def validate_password_digit(value):
    if not re.search(r"[\d]+", value):
        raise ValidationError("The password must contain at least one digit")
    else:
        return value

def validate_password_uppercase(value):
    if not re.search(r"[A-Z]+", value):
        raise ValidationError("The password must contain at least one uppercase character")
    else:
        return value
def validate_password_length(value):
    if len(value)<6:
        raise ValidationError("Password length must be more than 5 characters")
    else:
        return value


