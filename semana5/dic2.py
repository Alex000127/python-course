# Create an empty dictionary to store the expenses
expenses = {}

# Function to add expenses to the dictionary
def add_expense(category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

# Function to display the summary of expenses
def display_summary():
    print("Expense Summary:")
    for category, amount in expenses.items():
        print(f"{category}: ${amount}")

# Main program loop
while True:
    print("Enter your expense category (or 'quit' to exit):")
    category = input()
    
    if category == "quit":
        break
    
    print("Enter the amount spent:")
    amount = float(input())
    
    add_expense(category, amount)

# Display the summary of expenses
display_summary()