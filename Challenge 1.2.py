year = int(input("enter the year:"))


def checkYear(year):
  import calendar
  return (calendar.isleap(year))


if (checkYear(year)):
  print("Leap Year")
else:
  print("Not a Leap Year")
