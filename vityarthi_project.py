EXPENSE_RECORDS = [] 
DATA_FILE = "expense_ledger.txt"

def load_records_from_file():
    global EXPENSE_RECORDS
    
    try:
        with open(DATA_FILE, 'r') as file_handle:
            EXPENSE_RECORDS = [line.strip() for line in file_handle if line.strip()]
        print(f"Records loaded successfully. Found {len(EXPENSE_RECORDS)} entries.")
    except FileNotFoundError:
        print("Data file not found. Starting a new ledger.")
    except Exception as e:
        print(f"An error occurred during file loading: {e}")

def save_records_to_file():
    global EXPENSE_RECORDS
    
    try:
        with open(DATA_FILE, 'w') as file_handle:
            for record_string in EXPENSE_RECORDS:
                file_handle.write(record_string + '\n') 
        print(f"All {len(EXPENSE_RECORDS)} records have been saved.")
    except Exception as e:
        print(f"Error: Could not write data to file: {e}")

def record_new_expense():
    print("\n--- Record New Expense ---")
    amount_value = 0.0
    while True:
        try:
            amount_input = input("Enter amount spent (e.g., 50.00): $")
            amount_value = float(amount_input)
            if amount_value <= 0:
                print("Amount must be greater than zero. Please re-enter.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid numerical amount.")
    date_entry = ""
    while True:
        date_entry = input("Enter date (DD-MM-YYYY): ")
        if date_entry.count('-') == 2 and len(date_entry) >= 8: 
            break
        else:
            print("Invalid date format. Please use DD-MM-YYYY.")
    available_categories = ['Food', 'Transport', 'Study', 'Fun', 'Bills', 'Misc']
    print("\nAvailable Categories:")
    for index, category_name in enumerate(available_categories, 1):
        print(f"  {index}. {category_name}")
    
    selected_category = ""
    while True:
        try:
            choice = int(input("Select category number: "))
            if 1 <= choice <= len(available_categories):
                selected_category = available_categories[choice - 1]
                break
            else:
                print("Invalid number. Choose from the list.")
        except ValueError:
            print("Invalid input. Enter a number.")

    description = input("Enter a brief description: ")
    record_string = f"{date_entry}|{amount_value:.2f}|{selected_category}|{description}"
    
    global EXPENSE_RECORDS
    EXPENSE_RECORDS.append(record_string)
    print("\nExpense recorded successfully.")

def display_all_records():
    global EXPENSE_RECORDS
    if not EXPENSE_RECORDS:
        print("\nNo expenses have been recorded yet.")
        return

    print("\n--- All Expense Records ---")
    for number, record_string in enumerate(EXPENSE_RECORDS, 1):
        pieces = record_string.split('|') 
        date, amount, category, description = pieces[0], pieces[1], pieces[2], pieces[3]
        print(f"Record {number}: Date: {date}, Amount: ${amount}, Category: {category}, Note: {description}")


def generate_category_summary():
    global EXPENSE_RECORDS
    if not EXPENSE_RECORDS:
        print("\nNo records available to generate a summary.")
        return
    category_totals = {}
    total_spending_overall = 0.0
    for record_string in EXPENSE_RECORDS:
        pieces = record_string.split('|')
        category_name = pieces[2]
        amount_as_number = float(pieces[1])
        if category_name in category_totals:
            category_totals[category_name] += amount_as_number
        else:
            category_totals[category_name] = amount_as_number
            
        total_spending_overall += amount_as_number

    print("\n--- Category Spending Summary ---")
    for category, total in category_totals.items():
        percentage = (total / total_spending_overall) * 100
        print(f"Category: {category:<15} | Total Spent: ${total:8.2f} | ({percentage:.1f}% of total)")

    print("-" * 45)
    print(f"GRAND TOTAL TRACKED: ${total_spending_overall:8.2f}")

def run_expense_tracker():
    
    load_records_from_file() 
    while True:
        print("\n===== Expense Tracker Main Menu =====")
        print("1. Record a New Expense (F1)")
        print("2. Display All Records")
        print("3. Show Category Summary (F2)")
        print("4. Save and Exit (F3)")

        user_choice = input("Enter your choice (1-4): ")

        if user_choice == '1':
            record_new_expense()
        elif user_choice == '2':
            display_all_records()
        elif user_choice == '3':
            generate_category_summary()
        elif user_choice == '4':
            save_records_to_file()
            print("Application closed. Thank you!")
            break 
        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.")
if __name__ == "__main__":
    run_expense_tracker()