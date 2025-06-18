# Python Exception Handling

# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print('Cannot divide by zero!')

# Multiple exceptions
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print('Error: Division by zero')
        return None
    except TypeError:
        print('Error: Invalid types')
        return None
    return result

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide('10', 2))

# Try-except-else-finally
try:
    num = int(input('Enter a number: '))
except ValueError:
    print('That is not a valid number!')
else:
    print(f'You entered: {num}')
finally:
    print('This always runs')

# Custom exceptions
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Cannot withdraw . Balance: ')

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

account = BankAccount(100)
try:
    print(account.withdraw(50))
    print(account.withdraw(70))
except InsufficientFundsError as e:
    print(f'Error: {e}')

# Exception hierarchy
class ValidationError(Exception):
    pass

class EmailValidationError(ValidationError):
    pass

def validate_email(email):
    if '@' not in email:
        raise EmailValidationError(f'Invalid email: {email}')
    return True

try:
    validate_email('invalid-email')
except EmailValidationError as e:
    print(f'Email error: {e}')
except ValidationError as e:
    print(f'Validation error: {e}')

