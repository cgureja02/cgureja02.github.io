#!/usr/bin/env python3
import sys
'''
OPS445 Assignment 1 - Summer 2022

Program: assign1.py
Author: "Chakshu Gureja" - "cgureja@myseneca.ca"

Description : The python code in this file (assign1.py) is original work written by
"Chakshu Gureja". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.


Date: 2022-07-05
'''

def usage():
    # This function describes the usage of the script in the format of a string. it returns a string.
    usage = " This script is used to check the date ahead or below the given date with the help of integer value with the date. Suppose there is a valid date and an integervalue. so what this script does is will return a date based on integer value. if the integer value is positive then date will be changed by adding the number of days which represents the integer whereas if there is a date and negative number then it will subtract the number of days from the given date."
    return usage    
    
def days_in_mon(year):
 
  #This function accepts a year and check whether that year is leap year or not with the help of leap_year functionand if the year is leap year then it will return a dictionary which contains each month and maximum number of days in that month. if the year is leap year then it will return a dictionary with 29 days in month of feburary. whereas if the month is not leap year then it will return a dictionary with only 28 days in the month of feburary.

    # return dictionary_months
    pass # TODO: delete this line, replace with valid code.
    if leap_year(year) == False:
        mon_max = { 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    else:
       mon_max = { 1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    return mon_max

def valid_date(date):
 
#This function checks whether the given date is in correct format or not along with whether the day entered is within the range of maximum days in the month or not. If the date and day is correct then it will return true else it will return false.

#return True or False
 
    str_day, str_month, str_year =date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    if len(date) != 10 or day > days_in_mon(year)[month]:
       return False
    else: 
       return True


def leap_year(year):
   #Takes a year in YYYY format, and returns True if it's a leap year, False otherwise.
    lyear = year % 4 
    if lyear == 0:
        feb_max = 29 # this is a leap year
    else:
        feb_max = 28 # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        feb_max = 28 # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        feb_max = 29 # this is a leap year
    if feb_max == 29:
        return True
    else: 
           return False


def after(today):
    
#after function takes a valid date string in DD-MM-YYYY format and returns"
#a date string for the next day in DD-MM-YYYY format.

    if valid_date(today) == False:
        return '00-00-0000'
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

          

        tmp_day = day + 1 # next day

        if tmp_day > days_in_mon(year)[month]:
            to_day = tmp_day % days_in_mon(year)[month] # if tmp_day > this month's max, reset to 1
            tmp_month = month + 1
        else:
            to_day = tmp_day
            tmp_month = month + 0

        if tmp_month > 12:
            to_month = 1
            year = year + 1
        else:
            to_month = tmp_month + 0

        next_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year)
        return next_date

def before(today):

#before function takes a valid date string in DD-MM-YYYY format and returns"
#a date string for the previous day in DD-MM-YYYY format.
    if valid_date(today) == False:
        return '00-00-0000'
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)


        tmp_day = day - 1 # previous day

        if tmp_day == 0 :
            to_month = month - 1
            if to_month == 0: 
              year = year - 1
              to_month = 12
              to_day = 31
            else:
             to_day=days_in_mon(year)[to_month]
        else: 
           to_day = tmp_day + 0
           to_month = month + 0
        next_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year)
        return next_date

def dbda(start_date, num_days):

#This function takes a valid date and an integer from the user and according to an integer it either bring in use of after function or before function. this function also creates a loop and calls the function as many times as the integer value. Based on integer value this function calls the after or before function , and at last it return the exact date based on the integer value.
   
     end_date = 0
    # create a loop
    # call before() or after() as appropriate
    # return end_date
     if num_days >=0:
       for var in range(num_days):
           start_date = after(start_date)
     else: 
       num_days = num_days * -1
       for days in range(num_days):
           start_date = before(start_date)
     end_date = start_date
     return end_date

if __name__ == "__main__":
    # process command line arguments
    # call dbda()
    # output the result

#    this is the main function which checks all the errors and print results accordingly. This mainly calls the dbda function to print the date and here user has to put the 2 command line arguments which is date and an integer value. with the help of try and except this function checks for expected errors with the scripts and print appropriate results.

       try:
        date = sys.argv[1]
        num_days = sys.argv[2]
        str_day, str_month, str_year = date.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        if valid_date(date) == False:
           print("Error: wrong day entered")
        else:   
           print(dbda(date,int(num_days)))
       except KeyError:
         if month > 12:
            print("Error: wrong month entered")
       except ValueError:
           print("Error: wrong date entered")
       except IndexError:
           print("Usage: assign1.py DD-MM-YYYY N")  
