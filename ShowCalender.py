import calendar

def get_calender():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    cal = calendar.month(year,month)
    print(cal)


get_calender()