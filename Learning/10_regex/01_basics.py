import re

# Basic patterns
text = "Hello World! My email is saad@example.com and phone is 0300-1234567"

# Find all emails
emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
print(f"Emails: {emails}")

# Find all phone numbers
phones = re.findall(r"\d{4}-\d{7}", text)
print(f"Phones: {phones}")

# Match and search
pattern = r"Hello"
if re.match(pattern, text):
    print("Text starts with Hello")

if re.search(r"World", text):
    print("Found World in text")

# Groups
date = "2025-01-15"
match = re.match(r"(\d{4})-(\d{2})-(\d{2})", date)
if match:
    year, month, day = match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")

# Named groups
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match = re.match(pattern, date)
if match:
    print(f"Year: {match.group(\"year\")}")

# Find and replace
text2 = "Price is $100 and $200"
result = re.sub(r"\$(\d+)", r"Rs. \1", text2)
print(f"Replaced: {result}")

# Split
text3 = "one, two; three: four"
parts = re.split(r"[,;:]", text3)
print(f"Split: {parts}")

# Compile pattern
email_pattern = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
emails = email_pattern.findall("Contact: a@b.com or c@d.org")
print(f"Compiled pattern: {emails}")

# Common patterns
# Phone: r"\d{3}-\d{7}"
# URL: r"https?://[\w.-]+\.[\w.-]+"
# IP: r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
# Username: r"^[a-zA-Z0-9_]{3,16}$"

