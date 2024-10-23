def buy_a_beer():
    print("This simple application lets you know if you can buy a beer based on your age!")
    print("------------------------------------------------------------------------------")
    ask = input("Would you like to know if you can buy a beer? (Respond with Yes/No) : ")
    if ask in["Yes", "yes","Y", "y"]:
        age_collector = input("What is your age? : ")
        if age_collector.isdigit():
            age = int(age_collector)
            if age < 0:
                print("That is impossible!")
            elif age > 0 and age < 10:
                print("Still too young!")
            elif age > 10  and age < 18:
                print("Alcohol is not for sale to persons under the age of 18!")
            else:
                print("Drink responsibly! Alcohol is harmful to your health")
        else:
            print("Please provide an integer for your age")
    elif ask in["No", "NO" , "N" ,"n"]:
        print("Have a great day!")
    else:
        print("I cannot process your input! Use Yes or No")
buy_a_beer()