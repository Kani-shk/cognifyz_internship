# Task 6 – Leap Year Checker

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a Leap Year"
    else:
        return f"{year} is not a Leap Year"

if __name__ == "__main__":
    year = int(input("Enter a year: "))
    print(is_leap_year(year))
