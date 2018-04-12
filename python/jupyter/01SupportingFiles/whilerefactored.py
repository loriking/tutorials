i = 0
while i < len(PI) and birth_year[0] != PI[i] :
    i += 1 # it's a shorter version of i = i + 1
if i == len(PI):
    print("Not Found.")
else:
    print("Found it! It's {}".format(i))