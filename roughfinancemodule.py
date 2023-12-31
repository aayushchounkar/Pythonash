class Finance:
    def _init_(self):
        pass

    def investment(self):
        principal_amount = float(input("Enter the principal amount: "))
        interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
        investment_time = int(input("Enter the number of years the money is invested: "))

        future_value = ((principal_amount * interest_rate * investment_time) / 100) + principal_amount

        print(f"The future value of the investment is: {future_value}")

    def loan_approval(self):
        credit_score = int(input("Enter your credit score: "))
        income = float(input("Enter your annual income: "))
        loan_amount = float(input("Enter the loan amount you are requesting: "))
        time_period=int(input("Enter time period"))

        if self.check_credit_score(credit_score) and self.check_loan_amount(loan_amount, income):
            print("Loan Approved")
            print(f"${loan_amount} has been credited into your bank account..")
            return loan_amount
        else:
            print("Loan Denied")
            return -1

    def check_credit_score(self, credit_score):
        return credit_score >= 600 and credit_score <=900

    def check_loan_amount(self, loan_amount, income):
        return (loan_amount <= (income * 0.4))
    
    def generate_emi(self,time_period,loan_amount,interest_rate):
        interest = (loan_amount*time_period*interest_rate) / 100
        future_value = interest + loan_amount

        emi = future_value / (time_period*12)

        print(f"Monthly EMI: {emi}")
