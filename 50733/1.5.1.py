humans = int(input())
coast_cheep = int(input())
coast_expens = coast_cheep*2

cash_cheep = (humans*(3/4)*coast_cheep)
cash_expens = (humans*(1/4)*coast_expens)
cash = cash_cheep + cash_expens
print(round(cash))
