s = "I Love Python! Python is cool!!!"
c = ''
for i in range(1, len(s)):
    c += s[-i]

c += s[0]

print(c)