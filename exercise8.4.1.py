try:
    ball_color = 'green'

    ball_color = input("Enter a color: ")

    if ball_color == 'green':
        print ('You earned 5 points!')
    else:
        print('Incorrect color')
except:
    print('Error! Enter a real color')

    