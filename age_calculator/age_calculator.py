print("-----Age Calculator!-----")
while True:
    try:
        print("If you want to quit enter q")
        birth_year_input=input("Enter Your Birth Year: ")
        if birth_year_input.lower() == 'q':
            print("Good Bye!")
            break

        year_input = input("For which year do you want to know your age: ")
        if year_input.lower() == 'q':
            print("Good Bye!")
            break

        birth_year = int(birth_year_input)
        year = int(year_input)



        if year >=birth_year:
            age = (year - birth_year)
            print(f"your Age is {age}")


        else:
            print("Entered year before than birth year!")

    except ValueError:
        print("Invalid Input,Enter valid years.")
