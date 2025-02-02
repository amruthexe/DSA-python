def leap(y):
    return (y%4==0 and y%100!=0) or (y%400==0)

    """year % 4 == 0): This checks if the year is divisible by 4. If it is, it might be a leap year.
and year % 100 != 0: But, if the year is also divisible by 100, it’s not a leap year, unless...
(year % 400 == 0): The year is also divisible by 400, then it is a leap year.
    """
print(leap(2024))

import calendar

print(calendar.isleap(2024))