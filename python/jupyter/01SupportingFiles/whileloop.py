i = 0
while ( i < len(PI) - 3 and
       birth_year[0] != PI[i] and
       birth_year[1] == PI[i+1] and
       birth_year[2] == PI[i+2]and
       birth_year[3] == PI[i+3] ):
    print("It's not {}.".format(i))
    i += 1 # it's a shorter version of i = i + 1
if i == len(PI) - 3:
    print("Not Found.")
else:
    print("Found it! It's {}".format(i))