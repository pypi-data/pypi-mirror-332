# leapyearmodule.py
def tell_leap(year: int) -> bool:
    """
    Determine if a given year is a leap year.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.

    Raises:
        TypeError: If year is not an integer.
        ValueError: If year is outside a reasonable range (e.g., < -10000 or > 10000).
    """
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    if year < -10000 or year > 10000:
        raise ValueError("Year must be between -10000 and 10000")

    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

def ad_or_beforeAD(year: int) -> str:
    """
    Classify a year as AD (Anno Domini) or BC (Before Christ).

    Args:
        year (int): The year to classify.

    Returns:
        str: "AD" for non-negative years, "BC" for negative years.

    Raises:
        TypeError: If year is not an integer.
    """
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    return "BC" if year < 0 else "AD"