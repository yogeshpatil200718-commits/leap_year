from leap import leapYear

def test_leap_year():
    assert leapYear(2000) == True
    assert leapYear(2004) == True
    assert leapYear(1900) == False
    assert leapYear(2023) == False