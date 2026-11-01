try:
    units = int(input("Enter units consumed: "))

    if units < 0:
        raise ValueError("Negative units not allowed")

except ValueError as e:
    print("Error:", e)

else:
    if units <= 100:
        bill = units * 1
    elif units <= 200:
        bill = 100 + (units - 100) * 2
    else:
        bill = 300 + (units - 200) * 3

    print("Electricity Bill:", bill)

finally:
    print("Bill calculation completed")