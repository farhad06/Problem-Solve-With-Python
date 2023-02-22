'''Set is also an another type of datatype in python which is store mutiple item in a single variable
Set is:-----:
1.Unordered
2.unchangeable
3.Do not allow duplicate
'''
#create anf print
s={1,2,3,4,5}
print(s)
s1=set((3,4,5,67,25,45))
print(s1)

######################### Some Functions ####################################

"""
difference() ====> Returns a set containing the difference between two or more sets.

difference_update() ====> method removes the items that exist in both sets.

"""
print("-----------------------------------------------------------------------------")
"""
intersection() ===> Returns a set, that is the intersection of two other sets. 

intersection_update() ===> method removes the items that is not present in both sets. 

"""
print("-----------------------------------------------------------------------------")
"""
symmetric_difference() ===> Returns a set with the symmetric differences of two sets. 

symmetric_difference_update() ====> method updates the original set by removing items that are present in both sets, and inserting the other items.

"""