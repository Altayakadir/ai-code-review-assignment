# AI Code Review Assignment (Python)

## Candidate
- Name: Abdulkadir Altay
- Approximate time spent: 1 hour and 15 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The code divides the sum of not cancelled orders by the number of all orders whereas, it should divide by the number of the not cancelled orders.


### Edge cases & risks
- When the number of orders are 0, it will try to perform division by zero which is illegal.
- The items on the list must have 'status', 'amount' for sure, if broken data is fed, the code will crash.
- 'amount' is expected to be numerical, if a string is given the code will crash.



### Code quality / design issues
- The code is summing all the orders one by one in a loop. it can be optimized using list comprehensions or generator expressions. This will make it much faster when the list is long.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Add count == zero condition to avoid division by zero.
- Count only the not cancelled orders.
- Use list comprehensions to make the summation efficient.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

Since the most fragile operation is division, I would check division by zero cases. For example: all orders are cancelled, no orders, broken data etc.
I would try to see the limitations of the code by checking how fast it handles very large data.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- "dividing by the number of orders" is mathematically incorrect; it implies dividing by the total count rather than the non-cancelled count.
- it does not mention division by zero edge case.
- it ignores the valid 'status' and 'amount' keys requirement.

### Rewritten explanation
- This function calculates average order value by taking the average of the amounts of the non-cancelled orders. It utilizes list comprehensions for efficient filtering and calculation. It correctly excludes cancelled orders, safely validates data types, and handles empty datasets.

## 4) Final Judgment
- Decision: Request Changes
- Justification: Although the idea is correct, implementation is not safe and fast enough.
- Confidence & unknowns: Division by zero is inevitable if the list is empty, code lacks the checks for invalid data. 

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- if emails is None the code will crash.

### Edge cases & risks
- It is logically unsafe. It will pass every string that contains '@' even if it is not a valid email address syntactically.

### Code quality / design issues
- The current implementation is unsuitable for real life use. It relies on a single character check that does not align with standard email formatting rules.


## 2) Proposed Fixes / Improvements
### Summary of changes
- Use industry standard library to check syntax correctness of emails.
- Use try-except to correctly execute code without errors.
- Add emails is None check to prevent crash.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

I would focus on syntactic correctness: invalid characters like white space or using '@' more than one time without any quotation marks, missing username or domain etc. 
I would check None type emails and None type containing emails.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- "It safely ignores invalid entries" is incorrect since it just makes a simple '@' check and does not care about other syntax rules of emails.

### Rewritten explanation
- This function counts the number of valid email addresses in the input list. It safely ignores invalid entries by employing the industry standard "email_validator" library and handles empty input correctly.

## 4) Final Judgment
- Decision: Reject
- Justification: The logic is fundamentally incorrect. The single check on '@' is insufficient for validation. 
- Confidence & unknowns: While this code is safe for empty string, it is incorrect for any non-trivial input.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- it divides by the total number while it should not include the None items.

### Edge cases & risks
- division by zero when input is empty.
- if the value on the list cannot be converted to float, the code will crash.

### Code quality / design issues
- The logic is incorrect, no exception catches. Insufficient safety for invalid entries.

## 2) Proposed Fixes / Improvements
### Summary of changes
- add count == zero check in order to avoid division by zero.
- add try except for safe type conversion.
- count only the valid numbers for correct logic.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

I would check if the math was correct by inputs like [10, none, 20] to see if the code counts only the valid numbers.
I would check empty, all invalid numbers or None list to see division by zero and undefined behaviour.
I would check using data that contains illegal items like "string" etc. to see if the code crashes while type conversion.
I would check infinity containing data to see if it overflows.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- "averaging the remaining values" is incorrect since the calculation is done by dividing by the total number of items not the valid ones.
- It does not handle mixed input types safely. 
- It does not ensure accurate average since the logic is flawed in the first place.

### Rewritten explanation
- This function calculates the average of valid measurements by ignoring missing values (None) and non-numeric entries (NaN). It correctly handles mixed input types (e.g., strings) by skipping invalid data and robustly handles arithmetic edge cases, returning 0.0 if no valid measurements are found.

## 4) Final Judgment
- Decision: Request Change
- Justification: The original logic produced mathematically incorrect results by using the wrong denominator. It also lacked error handling for mixed types, posing a crash risk during type conversion.
- Confidence & unknowns: Very confident.
