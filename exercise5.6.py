prompt = 'Movie ticket prices are based on age. How old are you guys?\n'
prompt += 'Enter "quit" when you are finished :'

active = True

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print ("You have a free ticket!")
    elif age ==3 and age < 13:
        print ("Your ticket cost 10 pesos!")
    else :
        print ("Your ticket cost 15 pesos!")
else:
    stop
    