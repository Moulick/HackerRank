total = 0.00
meal = float(input())
tip = float(input())
tax = float(input())

total = float(meal * (1 + ((tip + tax) / 100)))
if total - int(total) > 0.5:
    total = int(total) + 1
else:
    total = int(total)
print('The total meal cost is %s dollars.' % total)
