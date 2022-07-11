prompt = "\nTell me five toppings that you would like on your pizza:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    
    
    if message == 'quit':
        active = False
        print("Thank you for stopping by!")   
        break
    if message == 'no':
        break
    if message == " ":
        continue
    else:
        print("\nYour topping " + message + " will be added to your pizza.")
        
