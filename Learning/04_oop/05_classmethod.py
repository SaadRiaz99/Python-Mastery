# classmethod and staticmethod

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_str):
        d, m, y = map(int, date_str.split('-'))
        return cls(d, m, y)

    @staticmethod
    def is_valid(d, m, y):
        return 1 <= m <= 12 and 1 <= d <= 31

    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'

d1 = Date(15, 1, 2025)
d2 = Date.from_string('20-3-2025')
print(f'Date 1: {d1}')
print(f'Date 2: {d2}')
print(f'Valid: {Date.is_valid(15, 13, 2025)}')

