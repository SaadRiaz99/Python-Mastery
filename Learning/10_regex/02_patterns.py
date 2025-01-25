# Common Regex Patterns

import re

# Email validation
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

print(is_valid_email('test@example.com'))
print(is_valid_email('invalid-email'))

# Phone number (Pakistan)
def is_valid_phone(phone):
    pattern = r'^03[0-9]{9}$'
    return bool(re.match(pattern, phone))

print(is_valid_phone('03001234567'))

# URL validation
def is_valid_url(url):
    pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return bool(re.match(pattern, url))

print(is_valid_url('https://example.com'))

# Extract data from text
text = 'Order #12345 placed on 2025-01-15 for .99'
order_id = re.search(r'#(\d+)', text)
date = re.search(r'(\d{4}-\d{2}-\d{2})', text)
amount = re.search(r'\', text)

print(f'Order: {order_id.group(1)}')
print(f'Date: {date.group(1)}')
print(f'Amount: {amount.group(1)}')

