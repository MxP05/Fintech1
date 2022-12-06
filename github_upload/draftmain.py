loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
future_v = loan.get("future_value")
print(future_v)
months_r=loan.get("remaining_months")
print(months_r)
loan_p=loan.get("loan_price")
print (loan_p)
fair_value= future_v/ (1+.20/12)**months_r

print(fair_value)

if fair_value>=loan_p:
    print("the loan is worth at least the cost to buy it.")
else:
    print("the loan is too expensive and not worth the price")

new_loan = {
"loan_price": 800,
"remaining_months": 12,
"repayment_interval": "bullet",
"future_value": 1000,
}
loan_price=new_loan.get("loan_price")
remaining_months=new_loan.get("remaining_months")
annual_d_rate=new_loan.get("annual_discount_rate", 0.20)
future_value=new_loan.get("future_value")


def calcu_p_value(future_value, remaining_months, annual_d_rate):
 p_value=future_value/(1+(annual_d_rate/12))**remaining_months
 print("fv", p_value)
 return (p_value)

present_value= calcu_p_value (future_value, remaining_months, annual_d_rate)
print(f"The present value of the loan is: {present_value}")