import sys

def leapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            year = int(sys.argv[1])
            if leapYear(year):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        except ValueError:
            print("Invalid year format passed.")
    else:
        # Fallback if run interactively locally
        year = int(input("Enter a year: "))
        if leapYear(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")