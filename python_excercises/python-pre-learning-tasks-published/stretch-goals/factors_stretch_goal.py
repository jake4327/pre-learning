def factors(number):
    # ==============
    # Your code here
    factor = []
    for i in range(2, number):
     if number%(i) == 0:
      factor.append(i)
    if len(factor) == 0:
     return '%s is a prime number' % str(number)
    else:
     return factor
    # ==============

print(factors(15)) # Should print [3, 5] to the console
print(factors(12)) # Should print [2, 3, 4, 6] to the console
print(factors(13)) # Should print “13 is a prime number”
