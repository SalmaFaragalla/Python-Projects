# Invoice Management System

This repository contains a Python-based Invoice Management System designed to streamline the billing process by automating the calculation of critical dates and statuses for invoices. The system allows users to input:

- Current Date
- Recurring Cycle Day
- Grace period
- Bill issue offset

Then, it calculates and displays the timeline of the invoice including:

- Invoice creation date (Create Invoice)
- Recurring cycle start date (RC Start)
- Grace period start and end dates (Grace Period Start, Grace Period End)
- Invoice expiration date (Expiration)
- Invoice status (Due, Overdue, or Expired)

# Sample Input

```text
Enter current date (DD-MM-YYYY): 01-06-2024
Enter start of the recurring cycle day: Monday
Enter the grace period: 2
Enter the bill issue offset: 2
```

# Sample Output

```text
--------------------- Invoice Timeline ---------------------
Invoice Creation Date:       Saturday   2024-06-01  Due
Recurring Cycle Start Date:  Monday     2024-06-03  Due
Grace Period Start Date:     Tuesday    2024-06-04  Overdue
Grace Period End Date:       Wednesday  2024-06-05  Overdue
Expiration Date:             Thursday   2024-06-06  Expired
-------------------------------------------------------------

Invoice Status:    Due
```
