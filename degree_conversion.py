# Get the temperature in C from the user
# and print the equivalent temperature in F.
# According to google, the formula is: (C * (9/5)) + 32

# Set up default values for variables
result = 0.0
temp_C = 0.0
temp_F = 0.0

# prompt for C temp
temp_C = float(input('Temperature in C? '))

# Calculate conversion
temp_F = (temp_C * (9/5)) + 32 # Use formula
result = f'{temp_F} F' # Interpolate our F value.

# print result
print(result)