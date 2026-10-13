from leap import leapYear

def test_year1():
    assert leapYear(2012) == "Leap year"

def test_year2():
    assert leapYear(2021) == "Not a leap year"