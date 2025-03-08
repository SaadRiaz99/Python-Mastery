def calculate_bill(units, consumer_type='unprotected'):
    if consumer_type == 'protected':
        if units <= 100: return units * 2.00
        elif units <= 200: return 100 * 2.00 + (units - 100) * 5.79
        elif units <= 300: return 100 * 2.00 + 100 * 5.79 + (units - 200) * 8.11
        else: return 100 * 2.00 + 100 * 5.79 + 100 * 8.11 + (units - 300) * 10.20
    else:
        if units <= 100: return units * 4.00
        elif units <= 200: return 100 * 4.00 + (units - 100) * 10.00
        elif units <= 300: return 100 * 4.00 + 100 * 10.00 + (units - 200) * 14.00
        else: return 100 * 4.00 + 100 * 10.00 + 100 * 14.00 + (units - 300) * 18.00

def calculate_total_bill(units, consumer_type='unprotected'):
    basic_bill = calculate_bill(units, consumer_type)
    duty = basic_bill * 0.05
    gst = basic_bill * 0.17
    total = basic_bill + duty + gst
    return {'units': units, 'consumer_type': consumer_type, 'basic_bill': round(basic_bill, 2), 'duty': round(duty, 2), 'gst': round(gst, 2), 'total': round(total, 2)}

def main():
    print('=== Electricity Bill Calculator ===')
    units = int(input('Enter units consumed: '))
    consumer_type = 'protected' if input('Protected? (y/n): ').lower() == 'y' else 'unprotected'
    bill = calculate_total_bill(units, consumer_type)
    print(f'Basic Bill: Rs. {bill[\
