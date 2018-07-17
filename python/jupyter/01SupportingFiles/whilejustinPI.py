# look for the birth year in Pi
birth_year='1203'

i = 0

while (i < len(PI) - 3 and
       birth_year != PI[i:i+4] ):
    i += 1

if i == len(PI) - 3: # we have reach the end of Pi!
    print(f"{birth_year} has not been Found in the first {len(PI)-2} digits of Pi.")
else:  # we have found our birth year in Pi!
    print(f"Found it! It's {i}")
