units = int(input("Enter consumed units: "))
consumer_type = input("Enter consumer type (protected/unprotected): ").lower()

bill = 0

meter_rent = 150
electricity_duty_rate = 0.05
gst_rate = 0.17

if consumer_type == "protected":
    if units <= 100:
        bill = units * 10.54
    elif units <= 200:
        bill = (100 * 10.54) + (units - 100) * 13.01
    else:
        print("Usage above 200 units is NOT allowed for protected users.")
        exit()

elif consumer_type == "unprotected":
    slabs = [
        (100, 22.44),
        (100, 28.91),
        (100, 33.10),
        (100, 37.10),
        (100, 40.20),
        (100, 41.62),
        (100, 42.76),
        (float('inf'), 47.69)
    ]

    remaining = units

    for limit, rate in slabs:
        if remaining <= 0:
            break
        used = min(limit, remaining)
        bill += used * rate
        remaining -= used

else:
    print("Invalid consumer type")
    exit()

subtotal = bill + meter_rent
electricity_duty = subtotal * electricity_duty_rate
gst = (subtotal + electricity_duty) * gst_rate
final_bill = subtotal + electricity_duty + gst

print("Energy Charges:", round(bill, 2))
print("Meter Rent:", meter_rent)
print("Electricity Duty:", round(electricity_duty, 2))
print("GST:", round(gst, 2))
print("TOTAL PAYABLE:", round(final_bill, 2))
