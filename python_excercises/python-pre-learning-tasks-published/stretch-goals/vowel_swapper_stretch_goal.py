def vowel_swapper(string):
    # ==============
    # Your code here
    import re
    def pattern(letter, ignore_case=True):
      return re.compile(letter, re.I)

    def iteration_over_string(pattern, string):
     return pattern.finditer(string)

    def change_array(iterator_object, s1, change, O_o_difference):
     count = 0
     for m in iterator_object:
      if count == 1:
       if O_o_difference == True:
       	if s1[m.start()] == "o":
         s1[m.start()] = str("ooo")
         break
        elif s1[m.start()] == "O":
         s1[m.start()] = str("000")
         break
       else:
       	s1[m.start()] = str(change)
        break
      count += 1
     return s1

    def array_to_string(array):
     string = ''
     for i in array:
      string += str(i)
     return string

    s1 = [x for x in string]
    #(regular expresion, change e.g. a --> 4, if the letter is O)
    patterns = [
     (pattern("a"), 4, False),
     (pattern("e"), 3, False),
     (pattern("i"), "!", False),
     (pattern("o"), ("ooo", "000"), True),
     (pattern("u"), "|_|", False)
    ]
    for pattern in patterns:
     p = iteration_over_string(pattern[0], string)
     s1 = change_array(p, s1, pattern[1], pattern[2])
    return array_to_string(s1)
    # ==============

print(vowel_swapper("aAa eEe iIi oOo uUu")) # Should print "a/\a e3e i!i o000o u\/u" to the console
print(vowel_swapper("Hello World")) # Should print "Hello Wooorld" to the console
print(vowel_swapper("Everything's Available")) # Should print "Ev3rything's Av/\!lable" to the console
