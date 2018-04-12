# look for the birth year in Pi
birth_year='1203'

i = 0

while (i < len(PI) - 3 and 
       birth_year != PI[i:i+4] ):
    i += 1 

if i == len(PI) - 3: # we have reach the end of Pi!
    print("{} has not been Found in the first {} digits of Pi.".format(birth_year,len(PI)-2))
else:  # we have found our birth year in Pi!
    print("Found it! It's {}".format(i))