def greet(s):
    return s.capitalize()


def whisper(s):
    return s.lower()


def shout(s):
    return s.upper()


def volume(v='Greet'):
    d = {'greet': greet, 'whisper': whisper, 'shout': shout}
    return d[v.lower()] if v.lower() in d else None