def type_of_consumer_choise():
    print("Please choose the type of consumer:")
    print("1. Residential Rural")
    print("2. Residential Urban")
    print("3. Industrial up to 40kW")
    print("4. Industrial above 40kW")
  
    choice = input("Enter your choice (1-4): ")
   

    if choice == '1':
        return "Residential Rural"
    elif choice == '2':
        return "Residential Urban"
    elif choice == '3':
        return "Industrial up to 40kW"
    elif choice == '4':
        return "Industrial above 40kW"
    else:
        print("Invalid choice. Please try again.")
        return type_of_consumer_choise()
        

