# Debug
import json
import time
print("Schedule Generator (3p) - Andrew Mason")
print("Version 0.2")
print("Please refer to the README if you encounter errors")
for clock in range(1, 10):
    print("-")
    time.sleep(0.05)
#Import Functions
    
print("importing libraries")
from random import randrange
from random import choice
# Variable def

print("db: defining variables")
p1_laun_days = 1
p2_laun_days = 1
p3_laun_days = 1
p1_laun_time = 1
p2_laun_time = 1
p3_laun_time = 1
p1_cfinal = 1
p2_cfinal = 1
p3_cfinal = 1
listall = [1, 2, 3]
list1 = [2, 3]
list2 = [1, 3]
list3 = [2, 3]
# Function def

print("db: defining functions")
#F0: Convert list to int
def convert(a):
    s = [str(i) for i in a]
    res = int("".join(s))
    return(res)
#F0.5: Convert big list to int
#F0.6: Decode big int into list
def decode(a):
    i = 0
    p1_lv_avail = []
    p2_lv_avail = []
    p3_lv_avail = []
    p1_br_avail = []
    p2_br_avail = []
    p3_br_avail = []
    p1_kt_avail = []
    p2_kt_avail = []
    p3_kt_avail = []
    p1_pc_avail = []
    p2_pc_avail = []
    p3_pc_avail = []
    p1_ts_avail = []
    p2_ts_avail = []
    p3_ts_avail = []
    list1 = list(a)
    #print(list1)
    while int(list1[i]) != 8:
        p1_lv_avail.append(list1[i])
        i += 1
        #print(f"i = {i}")
    i += 1
    while int(list1[i]) != 8:
        p2_lv_avail.append(list1[i])
        i += 1
        #print(f"i = {i}")
    i += 1
    while int(list1[i]) != 8:
        p3_lv_avail.append(list1[i])
        i += 1
        #print(f"i = {i}")
    i += 1
    while int(list1[i]) != 8:
        p1_br_avail.append(list1[i])
        i += 1
        #print(f"i = {i}")
    i += 1
    while int(list1[i]) != 8:
        p2_br_avail.append(list1[i])
        i += 1
        #print(f"i = {i}")
    i += 1
    while int(list1[i]) != 8:
        p3_br_avail.append(list1[i])
        i += 1
        #print(f"i = {i}")
    i += 1
    while int(list1[i]) != 8:
        p1_kt_avail.append(list1[i])
        i += 1
        #print(f"i = {i}")
    i += 1
    while int(list1[i]) != 8:
        p2_kt_avail.append(list1[i])
        i += 1
        #print(f"i = {i}")
    i += 1
    while int(list1[i]) != 8:
        p3_kt_avail.append(list1[i])
        i += 1
        #print(f"i = {i}")
    i += 1
    while int(list1[i]) != 8:
        p1_pc_avail.append(list1[i])
        i += 1
        #print(f"i = {i}")
    i += 1
    while int(list1[i]) != 8:
        p2_pc_avail.append(list1[i])
        i += 1
        #print(f"i = {i}")
    i += 1
    while int(list1[i]) != 8:
        p3_pc_avail.append(list1[i])
        i += 1
        #print(f"i = {i}")
    i += 1
    while int(list1[i]) != 8:
        p1_ts_avail.append(list1[i])
        i += 1
        #print(f"i = {i}")
    i += 1
    while int(list1[i]) != 8:
        p2_ts_avail.append(list1[i])
        i += 1
        #print(f"i = {i}")
    i += 1
    while int(list1[i]) != 8:
        p3_ts_avail.append(list1[i])
        i += 1
        #print(f"i = {i}")
    taskassign(p1_lv_avail, p2_lv_avail, p3_lv_avail, p1_br_avail, p2_br_avail, p3_br_avail, p1_kt_avail, p2_kt_avail, p3_kt_avail, p1_pc_avail, p2_pc_avail, p3_pc_avail, p1_ts_avail, p2_ts_avail, p3_ts_avail)
def mastconvert(library):
    s = [str(i) for i in library]
    res = int("8".join(s))
    return(res)
    
#F1: Determine available days
def availability():
    avail = []
    avail.append(input("Please enter one available weekday: "))
    add = input("Are there more available days? y/n: ")
    if add == "y":
        avail.append(input("Please enter next available weekday: "))
    else:
        return avail
    add = input("Are there more available days? y/n: ")
    if add == "y":
        avail.append(input("Please enter next available weekday: "))
    else:
        return avail
    add = input("Are there more available days? y/n: ")
    if add == "y":
        avail.append(input("Please enter next available weekday: "))
    else:
        return avail
    add = input("Are there more available days? y/n: ")
    if add == "y":
        avail.append(input("Please enter next available weekday: "))
    return avail
#F2: Converting days into numerical values
def numconvert(a):
    if a == "monday":
        a = 1
    if a == "tuesday":
        a = 2
    if a == "wednesday":
        a = 3
    if a == "thursday":
        a = 4
    if a == "friday":
        a = 5
    if a == "saturday":
        a = 6
    if a == "sunday":
        a = 7
    #print(f"conversion result: {a}")
    return a
#F3: Converting numbers BACK into days
def dayconvert(a):
    if a == 1:
        a = "Monday"
    if a == 2:
        a = "Tuesday"
    if a == 3:
        a = "Wednesday"
    if a == 4:
        a = "Thursday"
    if a == 5:
        a = "Friday"
    if a == 6:
        a = "Saturday"
    if a == 7:
        a = "Sunday"
    return a
#F4: Scheduling users via combinations
def scheduler(a, b, c):
    #define variables
    #print("db: define var")
    p1_cfinal = choice(a) if type(a) == list else a
    p2_cfinal = choice(b) if type(b) == list else b
    p3_cfinal = choice(c) if type(c) == list else c
    #print("db: convert to numbers")
    d = numconvert(p1_cfinal)
    e = numconvert(p2_cfinal)
    f = numconvert(p3_cfinal)
    #test for conflicts
    #print("db: testing for conflicts")
    if (d == (e or f)) or (e == (d or f)) or (d == (e or d)):
        return scheduler(a, b, c)
    else:
        return d, e, f
#F5: Assigning tasks based on day selections
def taskassign(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o):
    count = 0
    lv_day = 0
    br_day = 0
    kt_day = 0
    pc_day = 0
    ts_day = 0
    p_pick = 0
    listselect = 0
    print("db: variable def")
    #Living Room
    lv_sched = scheduler(a, b, c)
    p_pick = choice(listall)
    if p_pick == 1:
        lv_name = p1_name
        lv_day = int(lv_sched[0])
        listselect = 1
    if p_pick == 2:
        lv_name = p2_name
        lv_day = int(lv_sched[1])
        listselect = 2
    if p_pick == 3:
        lv_name = p3_name
        lv_day = int(lv_sched[2])
        listselect = 3
    br_day = lv_day
    count = 0
    print("db: LV done")
    while ((br_day == lv_day) and (count < 999)):
        br_sched = scheduler(d, e, f)
        #Bathroom
        count += 1
        if listselect == 1:
            p_pick = choice(list1)
        if listselect == 2:
            p_pick = choice(list2)
        if listselect == 3:
            p_pick = choice(list3)
        if p_pick == 1:
            br_name = p1_name
            br_day = int(br_sched[0])
            if listselect == 2:
                listselect = 12
            if listselect == 3:
                listselect = 13
        if p_pick == 2:
            br_name = p2_name
            br_day = int(br_sched[1])
            if listselect == 1:
                listselect = 12
            if listselect == 3:
                listselect = 23
        if p_pick == 3:
            br_name = p3_name
            br_day = int(br_sched[2])
            if listselect == 1:
                listselect = 13
            if listselect == 2:
                listselect = 23
    kt_day = lv_day
    count = 0
    print("db: BR done")
    while ((kt_day == lv_day or br_day) and (count < 999)):
        kt_sched = scheduler(g, h, i)
        count += 1
        #Kitchen
        if listselect == 23:
            kt_name = p1_name
            kt_day = int(kt_sched[0])
        if listselect == 13:
            kt_name = p2_name
            kt_day = int(kt_sched[1])
        if listselect == 12:
            kt_name = p3_name
            kt_day = int(kt_sched[2])
    pc_day = lv_day
    count = 0
    print("db: KT done")
    while ((pc_day == lv_day or br_day or kt_day) and (count < 999)):
        pc_sched = scheduler(j, k, l)
        count += 1
        #Porch
        p_pick = choice(listall)
        if p_pick == 1:
            pc_name = p1_name
            pc_day = int(pc_sched[0])
            listselect = 1
        if p_pick == 2:
            pc_name = p2_name
            pc_day = int(pc_sched[1])
            listselect = 2
        if p_pick == 3:
            pc_name = p3_name
            pc_day = int(pc_sched[2])
            listselect = 3
    ts_day = lv_day
    count = 0
    print("db: PC done")
    while ((ts_day == lv_day or br_day or kt_day or pc_day) and (count < 999)):
        ts_sched = scheduler(m, n, o)
        count += 1
        #Trash
        if listselect == 1:
            p_pick = choice(list1)
        if listselect == 2:
            p_pick = choice(list2)
        if listselect == 3:
            p_pick = choice(list3)
        if p_pick == 1:
            ts_name = p1_name
            ts_day = int(ts_sched[0])
        if p_pick == 2:
            ts_name = p2_name
            ts_day = int(ts_sched[1])
        if p_pick == 3:
            ts_name = p3_name
            ts_day = int(ts_sched[2])
    print("db: TS done")
    print(f"{lv_name} will clean the LIVING ROOM on {dayconvert(lv_day)}")
    print(f"{br_name} will clean the BATHROOM on {dayconvert(br_day)}")
    print(f"{kt_name} will clean the KITCHEN on {dayconvert(kt_day)}")
    print(f"{pc_name} will clean the PORCH on {dayconvert(pc_day)}")
    print(f"{ts_name} will clean the TRASH on {dayconvert(ts_day)}")
#F7: Gathering individual availability
def masteravail():
    print("Confirm Roommate Availability")
    for clock in range(1, 10):
        print("-")
        time.sleep(0.05)
    #Living Room
    print("LIVING ROOM CLEANING")
    print(f"Please enter the following LIVING ROOM availabiliy for {p1_name}.")
    p1_lv_avail = availability()
    print(f"Please enter the following LIVING ROOM availabiliy for {p2_name}.")
    p2_lv_avail = availability()
    print(f"Please enter the following LIVING ROOM availabiliy for {p3_name}.")
    p3_lv_avail = availability()
    #Bathroom
    print("BATHROOM CLEANING")
    print(f"Please enter the following BATHROOM availabiliy for {p1_name}.")
    p1_br_avail = availability()
    print(f"Please enter the following BATHROOM availabiliy for {p2_name}.")
    p2_br_avail = availability()
    print(f"Please enter the following BATHROOM availabiliy for {p3_name}.")
    p3_br_avail = availability()
    #Kitchen
    print("KITCHEN CLEANING")
    print(f"Please enter the following KITCHEN availabiliy for {p1_name}.")
    p1_kt_avail = availability()
    print(f"Please enter the following KITCHEN availabiliy for {p2_name}.")
    p2_kt_avail = availability()
    print(f"Please enter the following KITCHEN availabiliy for {p3_name}.")
    p3_kt_avail = availability()
    #Porch
    print("PORCH CLEANING")
    print(f"Please enter the following PORCH availabiliy for {p1_name}.")
    p1_pc_avail = availability()
    print(f"Please enter the following PORCH availabiliy for {p2_name}.")
    p2_pc_avail = availability()
    print(f"Please enter the following PORCH availabiliy for {p3_name}.")
    p3_pc_avail = availability()
    #Trash
    print("TRASH CLEANING")
    print(f"Please enter the following TRASH availabiliy for {p1_name}.")
    p1_ts_avail = availability()
    print(f"Please enter the following TRASH availabiliy for {p2_name}.")
    p2_ts_avail = availability()
    print(f"Please enter the following TRASH availabiliy for {p3_name}.")
    p3_ts_avail = availability()
    #Confirm availability
    print("Roommate availability confirmed")
    for clock in range(1, 10):
        print("-")
        time.sleep(0.05)
    taskassign(p1_lv_avail, p2_lv_avail, p3_lv_avail, p1_br_avail, p2_br_avail, p3_br_avail, p1_kt_avail, p2_kt_avail, p3_kt_avail, p1_pc_avail, p2_pc_avail, p3_pc_avail, p1_ts_avail, p2_ts_avail, p3_ts_avail)
    global entry
    entry = f"{mastconvert((convert(p1_lv_avail), convert(p2_lv_avail), convert(p3_lv_avail), convert(p1_br_avail), convert(p2_br_avail), convert(p3_br_avail), convert(p1_kt_avail), convert(p2_kt_avail), convert(p3_kt_avail), convert(p1_pc_avail), convert(p2_pc_avail), convert(p3_pc_avail), convert(p1_ts_avail), convert(p2_ts_avail), convert(p3_ts_avail)))}8"
    #print(entry)
    
#Run Program Here

print("db: Loading Done, Start in 3 seconds")
time.sleep(3)
p1_name = input("Please enter the name of the first roommate: ")
p2_name = input("Please enter the name of the second roommate: ")
p3_name = input("Please enter the name of the third roommate: ")
prev_entry = input("Use previous availability entries? y/n: ")
if prev_entry == "y":
    entry = input("Please paste the list saved from the previous schedule: ")
    #entry1 = list(entry)
    #print(entry1)
    decode(entry)
    
else:
    masteravail()

print("Schedule Generated. Please copy the following list for future schedules.")
print(entry)
for clock in range(1, 10):
        print("-")
        time.sleep(0.05)
print("cleaning up, program finished")

