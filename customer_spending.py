customer_spending = int(input('Enter customer total spending '))

'''
for spending between 1000 and 10000 = 5%
for spending between 10000 and 50000 = 10%
for spending 50000 and above = 5%

'''
if customer_spending >= 1000 and customer_spending <= 10000:
	rate = customer_spending * 0.05

elif customer_spending > 10000 and customer_spending <= 50000:
	rate = customer_spending * 0.1

elif customer_spending > 50000:
	rate = customer_spending * 0.2

customer_total_spending = customer_spending - rate

print(f"The customer_total_spending is {customer_total_spending:,}")
