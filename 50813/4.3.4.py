def final_price_2(*args, discount=1):
    return [round(max(i*(1-discount/100.0),0.0), 2) for i in args]