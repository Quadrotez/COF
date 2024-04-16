def final_price(c, discount=1):
    return max(c * (1 - discount / 100.0), 0.0)
