expenses = []
#Ensure the validity of the inputs
while True:
    expense = float(input("Enter an expense (or type 0 to finish): "))
    if expense == 0:
        break
    elif expense < 0:
        print("Expense cannot be negative. Please enter a valid amount.")
        continue
    else:
        expenses.append(expense)

#Set the counters
small_count = 0
moderate_count = 0
large_count = 0

#Determine the size of the expense
for expense in expenses:
    if expense < 25:
        small_count += 1
    elif 25 <= expense <= 100:
        moderate_count += 1
    else:
        large_count += 1

#Find the types of expenses that were asked of me
if len(expenses) == 0:
    print("No expenses were entered.")
else:
    number_of_expenses = len(expenses)
    total_expenses = sum(expenses)
    average_expense = total_expenses / number_of_expenses
    smallest_expense = min(expenses)
    largest_expense = max(expenses)
#Print Results
    print("\nExpense Summary:")
    print(f"Number of expenses: {number_of_expenses}")
    print(f"Total expenses: ${total_expenses:.2f}")
    print(f"Average expense: ${average_expense:.2f}")
    print(f"Smallest expense: ${smallest_expense:.2f}")
    print(f"Largest expense: ${largest_expense:.2f}")

    print(f"\nSmall expenses: {small_count}")
    print(f"Moderate expenses: {moderate_count}")
    print(f"Large expenses: {large_count}")