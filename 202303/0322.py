import re

# Input string
email_string = "TO:\naa@a.com\naa45@a.com\nCC\nb.c@a.con\nzz@a.com"

# Extract email addresses from the TO list using regular expressions
to_emails = re.findall(r"TO:\n(.*?)\n", email_string, re.DOTALL)

# If TO list is found
if to_emails:
    # Extract individual email addresses
    to_emails = to_emails[0].split('\n')
    
    # Filter out invalid email addresses and CC list
    to_emails = [email.strip() for email in to_emails if '@' in email and not email.endswith('@')]

    # Join the email addresses into a comma-separated string
    to_emails_str = ', '.join(to_emails)
    print(to_emails_str)
else:
    print("TO list not found in the input string.")