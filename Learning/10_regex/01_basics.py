# Python Regular Expressions

import re

# Basic patterns
text = 'Hello World! My email is saad@example.com and phone is 0300-1234567'

# Find all emails
emails = re.findall(r'[\\w.+-]+@[\\w-]+\\.[\\w.-]+', text)
print(f'Emails: {emails}')

# Find all phone numbers
phones = re.findall(r'\\d{4}-\\d{7}', text)
print(f'Phones: {phones}')

# Match and search
pattern = r'Hello'
if re.match(pattern, text):
    print('Text starts with Hello')

if re.search(r'World', text):
    print('Found World in text')

# Groups
date = '2025-01-15'
match = re.match(r'(\\d{4})-(\\d{2})-(\\d{2})', date)
if match:
    year, month, day = match.groups()
    print(f'Year: {year}, Month: {month}, Day: {day}')

# Named groups
pattern = r'(?P<year>\\d{4})-(?P<month>\\d{2})-(?P<day>\\d{2})'
match = re.match(pattern, date)
if match:
    print(f'Year: {match.group(\
