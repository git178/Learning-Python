# Variables are like containers
# Except when you "ask" for the "container" you get the value inside the container

x = 1
# The variable x now has a value of 1

x = 37890124
# The variable x got overwritten and is now 37890124

x = 10 + 5
# The variable x got overwritten again and is now 15

y = 41.23
# A new variable y has got a value of 41.23

x = y + 14
# Since y acts as a number, x would be 41.23 + 14, which is 55.23

y = y + x
# The variable y can also be use to overwrite itself
# Since y will now be
# 41.23 + 55.23
# That means y will now be 96.46

# There are three rules for naming variables in python
# Number 1: No special characters except underscores
# Number 2: The variable name can't start with underscore or numbers
# Number 3: It can't be a keyword like print
