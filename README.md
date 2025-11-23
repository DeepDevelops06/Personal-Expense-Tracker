Personal Expense Tracker

Project Overview

Tired of losing track of your cash? This is a straightforward Personal Expense Tracker built completely in Python. It runs right in your terminal, making it quick and easy to record, categorise and summarise your daily spending.
The project uses only the fundamental Python concepts (like lists, dictionaries, and file handling) we covered in the course, serving as a clean, reliable example of applying those core skills.

Core Features 

The application is structured around three main tasks to manage your finances : 

F1: Log a Transaction
Allows the user to quickly input the details for any new purchase (Date, Amount, Category, and Description).
Demonstrates: Input/Output and List Appending.

F2: Show a Spending Summary
Generates a report that calculates and displays the total amount spent for each category.
Demonstrates: Dictionary Use for efficient aggregation and Reporting.

F3: Save and Load Data
The system automatically loads old records upon startup and saves all current records safely to a local file before exiting.
Demonstrates: File Handling (Read/Write) and Data Persistence.

Technologies & Concepts Used

This project was built entirely using core Python features to fulfill the required non-functional requirements:
Language: Python 3
Data Structures: Lists for storing all records and Dictionaries for fast summary generation - Performance NF.
Error Handling: Implemented try - except blocks to manage invalid inputs, like typing letters for the amount Reliability NF.
Input Validation: Uses basic string checks to ensure the user follows the required format for dates Data Integrity NF.
Architecture: Simple, menu-driven Control Flow provides an easy-to-use interface Usability NF.


How to Run the Tracker

Save the file: Save the project code as tracker.py.
1.Open your terminal or command prompt.
2.Navigate to the directory where you saved tracker.py.
3.Run the program using the command: Bash
4.python tracker.py
5.The program will give you the main menu

Instructions for Testing

Test the functionality by performing the following steps in order:
Test F3 Load: Run the program for the first time. It should print a message saying, Data file not found. Starting a new ledger.
Test F1 Recording: Select option 1 Record a New Expense three times. Enter different categories e.g. Food, Fun, Food.
Crucial Test: When prompted for the amount, deliberately type hello to ensure the Error Handling NF1 prevents a crash.
Test F2 Summary: Select option 3 Show Category Summary. Verify that the amounts for categories like Food are added up correctly.
Test F3 Save : Select option 4 Save and Exit. A new file named expense_ledger.txt should appear in your directory.
Test F3 Load Persistence: Run python tracker.py again. It should now print a message saying, Records loaded successfully. Found 3 entries, proving the data was saved and loaded correctly.

Screenshots

<img width="824" height="837" alt="Screenshot 2025-11-23 at 6 58 23 PM" src="https://github.com/user-attachments/assets/85c8f261-bbf9-4356-b339-4914c2926270" />
<img width="999" height="828" alt="Screenshot 2025-11-23 at 6 58 38 PM" src="https://github.com/user-attachments/assets/cbd7c530-9987-4e5f-9cc2-786d95191c2e" />
<img width="999" height="828" alt="Screenshot 2025-11-23 at 6 58 38 PM" src="https://github.com/user-attachments/assets/04227d5a-b2c9-4f66-adb1-5e27417ca536" />
<img width="688" height="412" alt="Screenshot 2025-11-23 at 7 02 24 PM" src="https://github.com/user-attachments/assets/e4e3a488-65d6-442c-99e0-b8f67e3ce02c" />




