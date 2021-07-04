import datetime

created = input("Enter the time to check (small hint day-month-year): ")


def convert_numbers_to_date(date):
    created_dt = datetime.datetime.strptime(created, "%d-%m-%Y")
    converted_time = created_dt.strftime("%d-%m-%Y")
    return converted_time


print(convert_numbers_to_date(created))


