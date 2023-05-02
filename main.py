# Greet user
print("Welcome to the tip calculator!")

# Set necessary variables through user inputs and type conversion
total_bill = float(input("What was the total bill?\n"))
tip_percent = float(input("What percentage tip would you like to give; 10, 12, or 15?\n")) / 100
total_people = int(input("How many people are splitting the bill?\n"))

# Perform appropriate calculations and format to 2 decimals places
split_bill = total_bill / total_people
split_tip = split_bill * tip_percent
split_total = "{:.2f}".format(split_bill + split_tip)

# Display result in message
message = f"Each person should pay ${split_total}."
print(message)
