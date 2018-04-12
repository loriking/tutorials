i = 0
while  i < len(PI) - 3 and 
    birth_year != PI[i:i+4]):
    print("It's not {}.".format(i))
    i += 1 
if i == len(PI) - 3:
    print("Not Found.")
else:
    print("Found it! It's {}".format(i))