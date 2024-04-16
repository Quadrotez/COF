def my_sum(*args):
    return [0, args[0]] + [(sum([args[j] for j in range(i + 1)])) for i in range(1, len(args))]


