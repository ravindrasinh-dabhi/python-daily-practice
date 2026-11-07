from modules.Choise import type_of_consumer_choise

from modules.energy_charge import (
    residential_rural,
    residential_urban,
    industrial_upto_40kw,
    industrial_above_40kw
)
def main():   
 print("========================================")
 print("  ELECTRICAL ENERGY CHARGE CALCULATOR")
 print("========================================")


 try:

    
    consumer = type_of_consumer_choise()

    
    previous_reading = float(input("\nEnter previous meter reading: "))
    current_reading = float(input("Enter current meter reading: "))

    
    if previous_reading < 0 or current_reading < 0:
        raise ValueError("Meter readings cannot be negative!")

    if current_reading < previous_reading:
        raise ValueError("Current reading cannot be less than previous reading!")

    
    units = current_reading - previous_reading

    
    if consumer == "Residential Rural":

        energy_charge = residential_rural(units)

    elif consumer == "Residential Urban":

        energy_charge = residential_urban(units)

    elif consumer == "Industrial up to 40kW":

        load = float(input("Enter contracted load in kW: "))

        if load <= 0 or load > 40:
            raise ValueError("Load must be above 0 and up to 40 kW!")

        energy_charge = industrial_upto_40kw(units, load)

    elif consumer == "Industrial above 40kW":

        energy_charge = industrial_above_40kw(units)

    
    print("\n========================================")
    print("             BILL DETAILS")
    print("========================================")

    print("Consumer Category :", consumer)
    print("Previous Reading  :", previous_reading)
    print("Current Reading   :", current_reading)
    print("Units Consumed    :", units, "kWh")
    print("Energy Charges    : Rs.", round(energy_charge, 2))

    print("========================================")

 except ValueError as error:

    print("\nInput Error:", error)
    
 print("Do you want to calculate another bill?")
 print("1. Yes")
 print("2. No")
 choise=input("Enter your choice : ").upper()
 if choise=="1" or choise=="YES":
    main()
 else:
    print("Thank you for using the Electricity Energy charge Calculator!")
 print("note : this bill is based on the terrif rates after 30-sep-2026")

main()



