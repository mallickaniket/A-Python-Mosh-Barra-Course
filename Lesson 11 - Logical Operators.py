high_income = True
good_credit = True
criminal_record = False

if high_income and good_credit:
    print("Eligible for loan")

else:
    print("Not eligible for loan")
    
# Here, and is a logical operator that checks if both conditions are True. 
# If both high_income and good_credit are True, the code inside the if block will execute, printing "Eligible for loan". 
# If either condition is False, the else block will execute, printing "Not eligible for loan".

if high_income or good_credit:
    print("Eligible for loan")
    
# Here, or is a logical operator that checks if at least one of the conditions is True. 
# If either high_income or good_credit is True, the code inside the if block will execute.

if good_credit and not criminal_record:
    print("Eligible for loan")

# Here, not is a logical operator that negates the condition.
# If good_credit is True and criminal_record is False (not criminal_record is True), the code inside the if block will execute, printing "Eligible for loan".