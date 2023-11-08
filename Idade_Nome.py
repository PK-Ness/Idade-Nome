while True:
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    birth_year = input("Enter your birth year: ")
    age = 2023-int(birth_year)
    if birth_year < "1922" or birth_year > "2023":
        print("Invalid data.")
    else: print("Hello " + first_name + ". You are " + str(age) + " years old")