def calculator(a, b, operator):
    # ==============
    # Your code here
    import math
    if operator == "+":
     ans = bin(a + b)
    elif operator == "-":
     ans =  bin(a - b)
    elif operator == "*":
     ans =  bin(a * b)
    elif operator == "/":
      ans = bin(math.floor(a / b))
    return str(ans)[2:]

    # ==============

print(calculator(2, 4, "+")) # Should print 110 to the console
print(calculator(10, 3, "-")) # Should print 111 to the console
print(calculator(4, 7, "*")) # Should output 11100 to the console
print(calculator(100, 2, "/")) # Should print 110010 to the console
