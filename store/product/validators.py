from django.core.exceptions import ValidationError


def validate_stars(value):
    if 1 <= value <= 5:
        return value

    raise ValidationError("value must be between 0-5")
