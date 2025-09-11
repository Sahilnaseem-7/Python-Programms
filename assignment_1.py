from datetime import date

#Changing format of date
x = date.today()
print("Today's date is : ", x)

#Asking birthday
day = int(input("Enter day:(DD)\n"))
month = int(input("Enter month : (MM)\n"))
year = int(input("Enter year : (YYYY)\n"))
birthday = date(year, month, day)
print("Your birthdate is ", birthday )

#Calculating age
difference = x - birthday
age = difference.days//365
print("Your age is : ", age)

#Calculating Days until your next birthday
next_bday = date(x.year, month, day)
if x>next_bday:
    next_bday = date(x.year+1, month, day)
duedays = next_bday - x
print("\nDays remaining until your next birhtday are : ",  duedays.days)

