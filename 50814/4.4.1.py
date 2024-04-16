import math


def fsin(corner):
    return math.sin(math.radians(corner))


def fcos(corner):
    return math.cos(math.radians(corner))


def ftan(corner):
    return  "inf" if math.tan(math.radians(corner)) > 10**5 else ("-inf" if math.tan(math.radians(corner)) < -10**5 else math.tan(math.radians(corner)))



def get_func(s: str):
    return (fsin, float(s.split('(')[1][:-1])) if s.lower().split('(')[0] == 'sin' else (
        (fcos, float(s.split('(')[1][:-1])) if s.lower().split('(')[0] == 'cos' else (
            (ftan, float(s.split('(')[1][:-1])) if s.lower().split('(')[0] == 'tan' else None))


def main():
    return (lambda x: get_func(x)[0](get_func(x)[1]) if get_func(x) else "Некорректный ввод.")(input())