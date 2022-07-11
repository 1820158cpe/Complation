try:
    fav_numbers = {
    'John': 21,
    'Trizha': 20,
    'Mhay': 18,
    'Kyla': 18,
    'Queenie': 19,
    }

    num = fav_numbers['John']
    print("John's favorite number is " + str(num))

    num = fav_numbers['Trizha']
    print("Trizha's favorite number is " + str(num))

    num = fav_numbers['Mhay']
    print("Mhay's favorite number is " + str(num))

    num = fav_numbers['Kyla']
    print("Kyla's favorite number is " + str(num))

    num = fav_numbers['Queenie']
    print("Queenie's favorite number is " + str(num))
except:
    print("Error! Person's age not found")