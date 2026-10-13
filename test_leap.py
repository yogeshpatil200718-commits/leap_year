from leapyear import is_leap_year

def test_leap_year1():
    assert is_leap_year(2020) == "Leap year"

def test_leap_year2():
    assert is_leap_year(2021) == "Not a leap year"