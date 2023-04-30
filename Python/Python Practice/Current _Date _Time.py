
"""
3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14

"""


import datetime #import the "datetime" module, gets the current date and time

now = datetime.datetime.now() # create datetime object for current date and time

print ("Current date and time : ", now.strftime("%Y-%m-%d %H:%M:%S")) # uses the strftime() method of the datetime object to format the date and time as a string in the format "YYYY-MM-DD HH:MM:SS" and prints it to the console.

"""
%Y: year with century as a decimal number.
%m: month as a zero-padded decimal number.
%d: day of the month as a zero-padded decimal number.
%H: hour (24-hour clock) as a zero-padded decimal number. 
%M: minute as a zero-padded decimal number.
%S: second as a zero-padded decimal number.

"""
