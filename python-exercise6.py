# A tempature conversion tool

# user input tempature
celsius_temp = int(input(f'Enter a tempature in Celsius: '))

#convert tempature
fahernheit_temp = (celsius_temp * (9/5)) + 32

#output the final tempature
print(f'That\'s {fahernheit_temp} Fahernheit')