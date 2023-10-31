# Python Interactive Finance Dashboard


"Say goodbye to complicated spreadsheets and hello to simple, automated finances!"

## Overview

The Python Interactive Finance Dashboard is a powerful tool that simplifies financial management by providing an interactive and user-friendly interface to track your monthly transactions, categorize expenses, and visualize your financial data. This project is designed to help users gain insights into their financial activity and make informed decisions about their income and expenses.

## Features

### 1. Transaction Tracking and Summaries

- Track your monthly financial transactions.
- View transaction summaries in box plots for a quick overview of your finances.
- Get detailed transaction summaries in tabular format.

### 2. Categorization of Transactions

- Categorize each transaction based on its type, including:
  - 'Self-Care'
  - 'Fines'
  - 'Groceries'
  - 'Shopping'
  - 'Restaurants'
  - 'Transport'
  - 'Travel'
  - 'Subscriptions'
  - 'Incoming Zelle'
  - 'Outgoing Zelle'
  - 'Withdrawals'
  - 'Deposits'

### 3. Top Banner Summary

- The dashboard features a top banner that provides a summary of your last month's financial activity, including:
  - Income
  - Recurring Expenses
  - Non-recurring Expenses
  - Savings
- These values are automatically calculated when you input your financial data.

### 4. Interactive Dashboard

- The dashboard is interactive, allowing you to explore and analyze your financial data easily.
- Customize and filter data to focus on what matters to you.

### 5. Realistic Data

- The project uses real banking data from January through October 2023  (dont judge how much i love taco bell and chipotle LOL) , making it a realistic and practical tool for personal finance management.

## Technologies Used

- **Python**: The core programming language used for data processing and dashboard creation.
- **SQL**: Used for data storage and retrieval.
- **Libraries**: Key libraries used in the project include:
  - Pandas: Used for data manipulation.
  - Numpy: Used for numerical operations.
  - Panel: Used for building the interactive dashboard.
  - Hvplot: Used for creating visualizations.
  - Holoviews: Used for enhancing the dashboard's interactivity.

## Dashboard Visualization


## Getting Started

To get started with the Python Interactive Finance Dashboard, follow these steps:

1. Clone or download the project repository to your local machine.

2. Install the required dependencies. You can use the following command to install them:
3. run  $ python src/app.py to view dashboard 

```bash
pip install -r requirements.txt
pip install jupyter_bokeh
pip install hvplot