# Get the day number from the user
day = int(input('Day (0-6)? '))

# Make sure it's a number between 0 and 6,
if day < 7 and day >= 0:
    
    # If it's day 0 or day 6...sleep in!
    if day == 0 or day == 6:
        print('Sleep in')
    else:
        print('Go to work')

# Alternatively, you could check for week days with:
# if day >0 and day <6: