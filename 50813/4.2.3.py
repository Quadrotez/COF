def min_max(l, g='min'):
    return len([i for i in l if i == (min(l) if g == 'min' else max(l))])