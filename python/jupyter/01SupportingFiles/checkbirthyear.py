birth_year = input("What is your birth year?: ")
while not( birth_year.isdigit() and
          len(birth_year) == 4):
    print(f"{birth_year} is not a valid birth year. "
          "Only a postive number with 4 digits is accepted.")
    birth_year = input("What is your birth year?: ")
