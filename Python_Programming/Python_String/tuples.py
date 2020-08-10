#!/usr/bin/python3

import sys
sys.version_info[0]

lab_excercise = "Tuples"
lab_type = "lab-code"
python_version = ("%s,%s,%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_excercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

#=======================================

#CODE1: Create an empty TUPLE
tup1 = ()
print("CODE1:")
print("tup1 = %s" % str(tup1))
print("data type = %s" % str(type(tup1)))
print("length = %s" % str(len(tup1)))
print()

#CODE2: Create TUPLE with 1 item
tup2 = ("cloudacademy",)
print("CODE2:")
print("tup2 = %s" % str(tup2))
print("data type = %s" % str(type(tup2)))
print("length = %s" % str(len(tup2)))
print()

#CODE3: Create TUPLE with multiple items of the same type
tup3 = (1, 2, 3, 4, 5)
print("CODE3:")
print("tup3 = %s" %  str(tup3))
print("data type = %s" % str(type(tup3)))
print("length = %s" % str(len(tup3)))
print()

#CODE4: Create TUPLE with multiple items of different types
tup4 = ("cloud", "academy", 1, True, False)
print("CODE4:")
print("tup4 = {%s}" % str(tup4))
print("data type = %s" % str(type(tup4)))
print("length = %s" % str(len(tup4)))
print()

#CODE6: Search in TUPLE
print("CODE6:")
print ("cloud" in tup4)
print ("blah" in tup4)
print()

#CODE7: Retrieve item from TUPLE
print("CODE7:")
item0 = tup4[0]
item1 = tup4[1]
print("item0 = {item0}")
print("item1 = {item1}")
print()

#CODE8: Attempt to change immutable TUPLE
print("CODE8:")
try:
  tup4[0] = "not possible!"
except:
  print("Tuples are immutable!!")
print()

