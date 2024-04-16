def telephone(n):
    print(len(n) == 12 and n[:2] == '+7' and len([i for i in n[2:] if i in '0123456789']) == 10)
