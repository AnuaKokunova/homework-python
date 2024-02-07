# -*- coding: utf-8 -*-

 
def is_year_leap(year):
    return year % 4 == 0
  
year = 2008    
is_leap = is_year_leap(year)
print("Year " + str(year) + ": " + str(is_leap))