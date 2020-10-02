#-----------------------------------------------------------------------------
# Name:        Problem of the day
# Purpose:     Practice finding errors and fixing code
#
# Author:      Daniel
# Created:     28-Sept-2020
# Updated:     30-Sept-2020
#-----------------------------------------------------------------------------

#warm-up 1 (monkey trouble)
#Note for self: In python use 'and' instead of &&
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif not a_smile and not b_smile:
    return True
  return False

#warm-up 1 sleep_in
def sleep_in(weekday, vacation):
    if not weekday:
        return True
    if vacation:
        return True
    return False

#warm-up 1 near_hundred
def near_hundred(n):
    if n>=90 and n<=110:
        return True
    if n>=190 and n<=210:
        return True
    return False

#lists-1 firstLast6
return nums[0] == 6 or nums [-1] == 6

#lists-1 make_pi
#note to self...don't over think it, sometimes it is that simple...
return [3,1,4]

#lists-1 sum 3
#same note as ^
return sum(nums)

#lists-1 reverse 3
#printing a list backwards
#might want to remember this one...
return [nums[2], nums[1], nums[0]]

#lists-2 count_evens
# note to self, remove the 'pass' at the end of function for the 'return'. Also use (nums) instead of (big_diff)
#big_diff is just the name of the functions
return (max(nums) - min(nums))

