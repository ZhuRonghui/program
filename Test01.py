hours = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    hours = float(hours)
    rate = float(rate)
    if hours > 40:
        print("Pay:", (hours - 40) * 1.5 * rate + 40 * rate)
    else:
        print("Pay:", hours * rate)
except Exception as e:
    print(e)


