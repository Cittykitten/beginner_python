-------f----------

# The f tells Python to “Evaluate any expressions inside {} and insert their values into the string
# Anything inside {} must be a valid Python expression

name = "Tiana"
age = 17

print(f"My name is {name} and I am {age} years old.")
print(f"Next year I will be {age + 1}.")



# Output
# My name is Tiana and I am 17 years old.
# Next year I will be 18👌 

# The output without the f would've been 
# My name is {name} and I am {age} years old.
# Next year I will be {age + 1}.
