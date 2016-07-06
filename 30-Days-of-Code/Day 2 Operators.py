total = 0
meal = float(input())
tip = float(input())
tax = float(input())

total = int(meal * (1 + ((tip + tax) / 100)))

print('The total meal cost is %s dollars.' % total)
