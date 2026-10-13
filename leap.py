import sys

def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return "Leap year"
    else:
        return "Not a leap year"

if __name__ == "__main__":
    year = int(sys.argv[1])
    print(f"{year} is {is_leap_year(year)}")
    print(sys.argv[0])