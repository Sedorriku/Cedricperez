# check for loan eligibility
# Get customer details
# Ask for the user's salary and loan request
salary = float(input("What is your monthly salary? "))
loanrequest = float(input("Enter the loan amount you are asking for "))
 # Check if the user is eligible for the loan
# If the salary is too low deny loan
if salary >= 30000:
    if loanrequest <= 10 * salary: 
        print("You are eligible for the loan.")
        # Ask how many months the user wants to take to repay the loan
        # Add 10% interest to the loan
        # Show the final loan amount with interest
        months = int(input("How many months would you like to pay the loan? "))
        interest = 0.10
        totalloaninterest = loanrequest * (1 + interest)
        print(f"Your loan of {loanrequest:.2f} will be increased by 10% interest, with a new total of {totalloaninterest:.2f}")
        print(f"You will repay this amount over {months} months.")
    else: print(f"Loan Request is too high. max loan can be upto {10 * salary}")
else: print("Salary too low. Not eligale for a loan.")