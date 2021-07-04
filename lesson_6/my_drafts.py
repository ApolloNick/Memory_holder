import datetime


created = input("Enter the time to check (small hint day, month, year): ")
created_dt = datetime.datetime.strptime(created, "%d-%m-%Y")
print(created_dt + datetime.timedelta(days=365, hours=0))

# dict = {'Name': 'Zabra', 'Age': 7}
# print "Value : %s" %  dict.get('Age')