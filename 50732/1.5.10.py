#Task: Mirror introductory numbers (hours, minutes)
# so that they were mirrored on the dial of wall clocks

# Example:
# input:
# 3
# 20
# output:
# 8 
# 40



hours = int(input(""))
minutes = int(input(""))


mirror_minutes = 60 - minutes   
mirror_hours = 12 - hours if hours != 12 else 0
print(mirror_hours-1, mirror_minutes)
