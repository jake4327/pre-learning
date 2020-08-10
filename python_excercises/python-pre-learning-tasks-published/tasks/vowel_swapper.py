import re

def vowel_swapper(string):
    # ==============
    # Your code here
    s1 = string
    s1 = re.sub("[Aa]","4",s1)
    s1 = re.sub("[Ee]","3",s1)
    s1 = re.sub("[Ii]","!",s1)
    s1 = re.sub("[o]","ooo", s1)
    s1 = re.sub("[O]", "000", s1)
    s1 = re.sub("[uU]","|_|",s1)
    return s1
    # ==============

print(vowel_swapper("aA eE iI oO uU")) # Should print "44 33 !! ooo000 |_||_|" to the console
print(vowel_swapper("Hello World")) # Should print "H3llooo Wooorld" to the console 
print(vowel_swapper("Everything's Available")) # Should print "3v3ryth!ng's 4v4!l4bl3" to the console
