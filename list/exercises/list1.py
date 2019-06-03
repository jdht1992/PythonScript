weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# # Check the first letter of the attibutes in the list and if match the storage

day = []
for d in weekdays:
    if d[0] == "T":
        day.append(d)
    else:
        day.append(0)

print(day)

day = [d if d[0] == "T" else 0 for d in weekdays]
print(day)

# In this example we check if the word is in the list
day = []
for d in weekdays:
    if d == "Wednesday":
        day.append(d)
    
print(day)

day = [d for d in weekdays if d == "Wednesday"]

print(day)


