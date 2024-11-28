# Question = 10 Write a function to check if a year is a leap year.

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

print(is_leap_year(2024))  
print(is_leap_year(1900))  
print(is_leap_year(2000)) 