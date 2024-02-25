s = input()
print(''.join(f"\n{char} {count}" if char != sorted(set(s))[0] else f"{char} {count}" for char, count in {char: s.count(char) for char in sorted(set(s))}.items()))
