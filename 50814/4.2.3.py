A4 = (165, 255)
A5 = (80, 130)


def calc_tiles(size, form=A4):
    return (form[0] // size[0]) * (form[1] // size[1])