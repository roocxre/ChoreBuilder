# ChoreBuilder
Automatic, RNG-based schedule generator for common household chores, designed for a household of 3.

SCHEDULE GENERATOR 3-PERSON
ANDREW MASON

Thank you for using the schedule generator!
This program is designed to acommodate for up to 3 roommates. If 3 is too many,
simply use a placeholder name and make up availability days.

A PROGRAM THAT CAN RUN PYTHON 3 FILES IS REQUIRED TO USE THE SCHEDULER!

THIS PROGRAM IS NOT OPTIMIZED.

Why is it not optimized? I'M NOT GOOD AT PROGRAMMING!
This program will not work properly if you:
    - Use capital letters for days of the week
    - Misspell days of the week whatsoever

In order to avoid excess typing and headaches, I suggest you use numbers 
instead of typing out days of the week:
1 - Monday
2 - Tuesday
3 - Wednesday
4 - Thursday
5 - Friday
6 - Saturday
7 - Sunday

Additionally, there is NO undo button for the program - if you do something
wrong and press enter, please restart the program and do it all over again!

HOW TO USE:

1. Please fill out roommates availability in the Excel document provided in
the package. If not, please have all roommates present to tell you days they
are available.

2. The program will open and initialize, then ask for roommates names. Please
enter names and press Enter to continue.

3. The program will then ask you if you would like to use "previous availability
entries." if this is your first time using the program, please type "n" and
continue. If you would like to use this feature in the future, please refer to
step 7 below.

4. The program will then ask you to enter availabilities for each roommate in
weekday form. Please type your response in weekdays (including saturday and
sunday) and do NOT include any capital letters, as this will break the program.
Please also only enter one weekday at a time.

5. After entering the first weekday, the program will ask you if there are any
more available weekdays. If there are, please type "y" and enter the next
available weekday as prompted. If not, type "n" and continue. The program
supports up to 5 available weekdays, in any order.

6. Once all available days are entered, the program will calculate days to
clean and display them. Please copy or screenshot these results for use.

7. The program will also give you a key in a series of numbers, which may be
used to SKIP the availabiltiy entry for the next time. Simply copy the key and
type "y" in the prompt in step 3, then paste the key when prompted.

HOW IT WORKS:

This program takes availability entries, then uses recursion to generate random
schedules where cleaning days don't conflict with each other for a task.
For example, if Roommate 1 is available to clean the bathroom on Tuesday, and
Roommate 2 is available to clean the bathroom on Tuesday AND Wednesday, then
the program will assign their bathroom cleaning days to differing days (Tuesday
for Roommate 1, and Wednesday for Roommate 2).

I really hope that makes sense.

ERRORS:

If the program cannot generate a schedule with no conflicting days within
1021 recursions, it will crash. I advise reconsidering availability before
trying again.

WIP/PLANNED UPDATES:
Will expand the “smartness” of the randomizer to attempt to find the 
closest possible iteration of days that represents full day uniqueness, 
even if this uniqueness IS only partial.

UPDATE DOCUMENTATION

0.1 Launch

0.2 Program now attempts to create a schedule with no overlapping days,
attempts are capped at 1000

0.3 Updated complexity of this overlap avoider. It will now individually determine 
uniqueness for each task, attempts capped at 1000 each, effectively giving the
program 5000 attempts to randomize the schedule, as well as preserving
uniqueness per day. 

0.4 Optimized randomization of workdays and therefore improved functionality
of said randomizer. A preliminary workday sorter has been removed, which had
previously given the main day workday randomizer only one day per task per
person to work with. The main randomizer now has every available day to work with,
therefore improving random functionality.
However, added days has made the restart key much longer, which can’t be avoided 
unless I make another decoding dictionary, which would take a while. 

