# print a corrisponding day of the week to a provided number 0-5

#create input variable
day = int(input(f'Type a number from 0-5: '))

if day == 0:
    print('Sunday')
elif day == 1:
    print('Monday')
elif day == 2:
    print('Tuesday')
elif day == 3:
    print('Wednesday')
elif day == 4:
    print('Thrusday')
elif day == 5:
    print('Friday')
else:
    print('Saturday')

