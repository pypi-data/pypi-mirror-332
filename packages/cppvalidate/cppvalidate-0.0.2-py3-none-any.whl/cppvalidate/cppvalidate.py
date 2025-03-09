import re
from django.core.exceptions import ValidationError

class Validator:
    @staticmethod
    def is_valid_email(value):
        """Check if email is valid"""
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
            raise ValidationError("Enter a valid email address.")

    @staticmethod
    def is_strong_password(value):
        """Check if password is strong"""
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', value):
            raise ValidationError("Password must be at least 8 characters long and contain both letters and numbers.")

    @staticmethod
    def is_valid_phone(value):
        """Check if phone number is valid"""
        if not re.match(r'^\+?\d{9,15}$', value):
            raise ValidationError("Enter a valid phone number with 9 to 15 digits.")
