def find_leap_year(year: int):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 'leap year.'
            else:
                return 'not a leap year'
        else:
            return "Leap year"
    else:
        return "Leap year."