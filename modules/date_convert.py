def is_leap_year(year:int) -> bool:
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(year:int, month:int) -> int:
    """Return the number of days in a given month for a given year."""
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    return days[month]


def day_to_date(start_date:tuple, days:int) -> tuple:
    """
    Calculate the date that is 'days' days after 'start_date'.
    
    Args:
        start_date: tuple(year, month, day) where year is 4 digits, month and day are integers
        days: number of days to add
    
    Returns:
        tuple(year, month, day) representing the resulting date
    """
    year, month, day = start_date
    
    while days > 0:
        days_in_current_month = days_in_month(year, month)
        days_remaining_in_month = days_in_current_month - day + 1
        
        if days < days_remaining_in_month:
            day += days
            days = 0
        else:
            days -= days_remaining_in_month
            month += 1
            day = 1
            
            if month > 12:
                year += 1
                month = 1
    
    return (year, month, day)


def date_to_day(start_date:tuple, end_date:tuple) -> int:
    """
    Calculate the number of days between start_date and end_date.
    
    Args:
        start_date: tuple(year, month, day)
        end_date: tuple(year, month, day)
    
    Returns:
        int: number of days between the dates
    """
    start_year, start_month, start_day = start_date
    end_year, end_month, end_day = end_date
    
    # Convert both dates to days since a common reference point
    def date_to_days_since_reference(year, month, day):
        days = day
        
        # Add days for each month in current year
        for m in range(1, month):
            days += days_in_month(year, m)
        
        # Add days for each year before current year
        for y in range(1, year):
            days += 366 if is_leap_year(y) else 365
        
        return days
    
    start_days = date_to_days_since_reference(start_year, start_month, start_day)
    end_days = date_to_days_since_reference(end_year, end_month, end_day)
    
    return end_days - start_days


def main():
    print(day_to_date((1980, 3, 17), 10597))


if __name__ == "__main__":
    main()
    