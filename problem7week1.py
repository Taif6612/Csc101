hours=int(input('Enter the number of hours you will work per week:'))
amount_earned=int(input('Enter the amount you earn per hour: BDT.'))

gross_income_per_month=(amount_earned*(hours*4))
print('Gross income per month before deduction',gross_income_per_month)
deduction_of_20=gross_income_per_month*(20/100)
after_deduction=gross_income_per_month-deduction_of_20
print('Gross income per month after deduction',after_deduction)
Amount_paid_as_tution_fee=2400*12
Yearly_earning=gross_income_per_month*12
print('Yearly earning',Yearly_earning)
print('Amount paid as tuition fees per year:BDT.',Amount_paid_as_tution_fee)