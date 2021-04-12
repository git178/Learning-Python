a = "Well hello there"
b = "General Kenobi"

# You can add strings in different ways:
# Using a + symbol
print(a + b)# = Well hello thereGeneral Kenobi
#  Using a, symbol- this is only for print
print(a,b)# = Well hello there General Kenobi
# Using a + " " symbol
print(a + " " + b)# Well hello there General Kenobi
# You can store the result in a new variable so 
c = a + " " + b
print(c)# Well hello there General Kenobi
# You can also add parts of different variables to get a new result
print(a[:5])# is = Well
print(b[:8])# is= General
d = a[:5] + b[:8]
print(d)# is = Well General
