i=0
while not (birth_year == PI[i:i+4]):
    print("It's not {}.".format(i))
    i += 1 
print("Found it! It's {}".format(i))