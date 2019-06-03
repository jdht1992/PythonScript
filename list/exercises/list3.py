# stores the first letter of the days of thw week
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(weekdays)

first = []
for day in weekdays:
    first.append(day[0])

print(first)

# list comprehension
first2 = [day[0] for day in weekdays]
print(first2)

