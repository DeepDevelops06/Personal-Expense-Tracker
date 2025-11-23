1. Problem Statement
Lets be real trying to track every rupee I spend using a random notebook or a basic spreadsheet is a mess. Its easy to make mistakes, and figuring out where all the money went at the end of the month is a huge hassle.
The problem is needing a quick, simple digital tool that can automatically organize spending and tell me you spent this much on food this week.

2.Scope
This is a command-line application built in Python.
It handles:Logging a new expense, grouping those expenses by category like Food or Fun, and saving all the data locally to a simple text file so I don't lose it when I close the program.
It doesn't handle:Any fancy graphics no GUI, connecting to the internet, or linking to a bank account. It's kept simple to focus on proving I can handle the core Python concepts.

3.Target Users
Anyone who wants to get a better grip on their money without needing a massive, complicated app. Mostly, its designed for students and individuals who just need a fast, reliable ledger for their daily spending.

4.High Level Features
The project is structured around these three main jobs:
1:Log a Transaction
You can quickly punch in the details for something you just bought the date, the amount, the category, and a quick note.
2:Show a Spending Summary
It runs a quick report that calculates the total amount spent on *each* category. This is the main analysis tool.
3:Save and Load Data
It automatically grabs any old records from the hard drive when the program starts and makes sure everything is saved safely to a text file before it shuts down.
