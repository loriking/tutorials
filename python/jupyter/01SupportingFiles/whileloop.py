i = 0

while (birth_year[0] != PI[i] or 
       birth_year[1] != PI[i+1] or
       birth_year[2] != PI[i+2] or
       birth_year[3] != PI[i+3] ):
    i += 1 # it's a shorter version of i = i + 1

print("Found it! It's {}".format(i))