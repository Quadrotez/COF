lambda x: int(str(x)[-1])+int(str(x)[:-1] if len(str(x)) > 1 else 0)