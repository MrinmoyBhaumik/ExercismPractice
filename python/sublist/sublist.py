"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"
def find_indexes(lst, item):
    return [index for index, value in enumerate(lst) if value == item]

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if not list_one and len(list_two) > 0:
        return SUBLIST
    if len(list_one) < len(list_two):
         indexes = find_indexes(list_two,list_one[0])
         for i in indexes:
              for item in list_one:
                   if item != list_two[i]:
                        break
                   if item == list_one[len(list_one)-1] and item == list_two[i]:
                        return SUBLIST
                   if item == list_two[i]:
                        i+=1
         return UNEQUAL
    if not list_two and len(list_one) > 0:
         return SUPERLIST
    if len(list_two) < len(list_one):
         indexes = find_indexes(list_one,list_two[0])
         for i in indexes:
              for item in list_two:
                   if item != list_one[i]:
                        break
                   if item == list_two[len(list_two)-1] and item == list_one[i]:
                        return SUPERLIST
                   if item == list_one[i]:
                        i+=1
         return UNEQUAL
    return UNEQUAL
