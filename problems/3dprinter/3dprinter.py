statues = int(input())

# You want to maximize the number of printer you have without 
# going over the max days (number of statues, because when you have 1
# printer then it takes the same amount of days as the number of statues)
# Once you maximize the number of printers, you just need to add another day

days = 0
printers = 1
while printers < statues:
    printers *= 2
    days += 1

# add another day because your printers will always be less than the number of statues
# therefore you will print the number of printer statues once and then you need to print
# statues - printers now which is < printers so we just add one more day for that
print(days + 1)