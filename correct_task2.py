# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
# Requires: pip install email-validator
from email_validator import validate_email, EmailNotValidError

def count_valid_emails(emails):
    count = 0
    if emails is None: # no email means 0 valid email.
        return 0
    for email in emails:
        try:
            validate_email(email, check_deliverability=False)
            count += 1
        except (ValueError, TypeError):   # if an error occurred, then it is invalid.
            continue
    return count
