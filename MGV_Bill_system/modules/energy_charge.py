def residential_rural(units):
    if units <=50:
        energy_charge = units * 2.65
    elif units <= 100:
        energy_charge = (50 * 2.65) + ((units - 50) * 3.10)
    elif units <= 250:
        energy_charge = (50 * 2.65) + (50 * 3.10) + ((units - 100) * 3.75)
    else:
        energy_charge = (50 * 2.65) + (50 * 3.10) + (150 * 3.75) + ((units - 250) * 4.90)
    return energy_charge

def residential_urban(units):

    if units <= 50:
        amount = units * 3.05

    elif units <= 100:
        amount = (50 * 3.05) + (units - 50) * 3.50

    elif units <= 250:
        amount = (50 * 3.05) + (50 * 3.50) + (units - 100) * 4.15

    else:
        amount = (50 * 3.05) + (50 * 3.50) + (150 * 4.15) + (units - 250) * 5.20

    return amount

def industrial_upto_40kw(units, load):

    if load <= 10:
        amount = units * 4.35

    else:
        amount = units * 4.65

    return amount

def industrial_above_40kw(units):

    amount = units * 4.60

    return amount