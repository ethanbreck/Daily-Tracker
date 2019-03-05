import json
import datetime

print("1. For taking a shower")
print("2. Finished Shower")
print("3. Going to bathroom")
print("4. Left the bathroom")
print("5. Going on Reddit")
print("6. Leaving Reddit")
print("7. Doing Homework")
print("8. Finishing Homework")
print("9. Working on Eagle Project.")
print("10. Stopped working on Eagle Project")
print("11. Going to take the Bus")
print("12. Finished taking the Bus")
print("13. Going to Work")
print("14. Got Home from Work")
print("15. Going to School")
print("16. Going home from school")

task = input("What is the task? ")

def start_shower():
    # localDate.year, month, etc
    localDate = datetime.datetime.now()
    entry={
            "Task": "Started Shower",
            "year":localDate.year,
            "month":localDate.month,
            "day":localDate.day,
            "hour":localDate.hour,
            "minute":localDate.minute,
            "second":localDate.second,
            }
    return entry

def fin_shower():
    # localDate.year, month, etc
    localDate = datetime.datetime.now()
    entry={
            "Task": "Finished Shower",
            "year":localDate.year,
            "month":localDate.month,
            "day":localDate.day,
            "hour":localDate.hour,
            "minute":localDate.minute,
            "second":localDate.second,
            }
    return entry
    
def start_bathroom():
    # localDate.year, month, etc
    localDate = datetime.datetime.now()
    entry={
            "Task": "Went to Bathroom",
            "year":localDate.year,
            "month":localDate.month,
            "day":localDate.day,
            "hour":localDate.hour,
            "minute":localDate.minute,
            "second":localDate.second,
            }
    return entry

def fin_bathroom():
    # localDate.year, month, etc
    localDate = datetime.datetime.now()
    entry={
            "Task": "Left the bathroom",
            "year":localDate.year,
            "month":localDate.month,
            "day":localDate.day,
            "hour":localDate.hour,
            "minute":localDate.minute,
            "second":localDate.second,
            }
    return entry
    
def start_reddit():
    # localDate.year, month, etc
    localDate = datetime.datetime.now()
    entry={
            "Task": "Started going on reddit",
            "year":localDate.year,
            "month":localDate.month,
            "day":localDate.day,
            "hour":localDate.hour,
            "minute":localDate.minute,
            "second":localDate.second,
            }
    return entry

def fin_reddit():
    # localDate.year, month, etc
    localDate = datetime.datetime.now()
    entry={
            "Task": "Left Reddit",
            "year":localDate.year,
            "month":localDate.month,
            "day":localDate.day,
            "hour":localDate.hour,
            "minute":localDate.minute,
            "second":localDate.second,
            }
    return entry

def start_homework():
    # localDate.year, month, etc
    localDate = datetime.datetime.now()
    entry={
            "Task": "Started working on Homework",
            "year":localDate.year,
            "month":localDate.month,
            "day":localDate.day,
            "hour":localDate.hour,
            "minute":localDate.minute,
            "second":localDate.second,
            }
    return entry

def fin_homework():
    # localDate.year, month, etc
    localDate = datetime.datetime.now()
    entry={
            "Task": "Stopped working on Homework",
            "year":localDate.year,
            "month":localDate.month,
            "day":localDate.day,
            "hour":localDate.hour,
            "minute":localDate.minute,
            "second":localDate.second,
            }
    return entry

def start_eagle_work():
    #localDate.year, month, etc
    localDate = datetime.datetime.now()
    entry={
            "Task": "Started Working on Eagle Project",
            "year":localDate.year,
            "month":localDate.month,
            "day":localDate.day,
            "hour":localDate.hour,
            "minute":localDate.minute,
            "second":localDate.second,
            }
    return entry
    
def stop_eagle_work():
    #localDate.year, month, etc
    localDate = datetime.datetime.now()
    entry={
            "Task": "Stopped working on Eagle Project",
            "year":localDate.year,
            "month":localDate.month,
            "day":localDate.day,
            "hour":localDate.hour,
            "minute":localDate.minute,
            "second":localDate.second,
            }
    return entry

def start_work():
    # localDate.year, month, etc
    localDate = datetime.datetime.now()
    entry={
            "Task": "Going to Work",
            "year":localDate.year,
            "month":localDate.month,
            "day":localDate.day,
            "hour":localDate.hour,
            "minute":localDate.minute,
            "second":localDate.second,
            }
    return entry

def fin_work():
    # localDate.year, month, etc
    localDate = datetime.datetime.now()
    entry={
            "Task": "Got Home from work",
            "year":localDate.year,
            "month":localDate.month,
            "day":localDate.day,
            "hour":localDate.hour,
            "minute":localDate.minute,
            "second":localDate.second,
            }
    return entry
def start_school():
    # localDate.year, month, etc
    localDate = datetime.datetime.now()
    entry={
            "Task": "Going to School",
            "year":localDate.year,
            "month":localDate.month,
            "day":localDate.day,
            "hour":localDate.hour,
            "minute":localDate.minute,
            "second":localDate.second,
            }
    return entry

def fin_school():
    # localDate.year, month, etc
    localDate = datetime.datetime.now()
    entry={
            "Task": "Going home from School",
            "year":localDate.year,
            "month":localDate.month,
            "day":localDate.day,
            "hour":localDate.hour,
            "minute":localDate.minute,
            "second":localDate.second,
            }
    return entry

def start_bus():
    # localDate.year, month, etc
    localDate = datetime.datetime.now()
    entry={
            "Task": "Started Bus Ride",
            "year":localDate.year,
            "month":localDate.month,
            "day":localDate.day,
            "hour":localDate.hour,
            "minute":localDate.minute,
            "second":localDate.second,
            }
    return entry

def fin_bus():
    # localDate.year, month, etc
    localDate = datetime.datetime.now()
    entry={
            "Task": "Finished Bus Ride",
            "year":localDate.year,
            "month":localDate.month,
            "day":localDate.day,
            "hour":localDate.hour,
            "minute":localDate.minute,
            "second":localDate.second,
            }
    return entry
    

if task == "1":
    starting_shower = start_shower()
    with open('data/shower.json', 'a') as outfile:
        json.dump(starting_shower, outfile, indent=4)
        print("\n \nTask Logged.")
elif task == "2":
    finishing_shower = fin_shower()
    with open('data/shower.json', 'a') as outfile:
        json.dump(finishing_shower, outfile, indent=4)
        print("\n \nTask Logged.")
elif task == "3":
    goingtobath = start_bathroom()
    with open('data/bathroom.json', 'a') as outfile:
        json.dump(goingtobath, outfile, indent=4)
        print("\n \nTask Logged.")
elif task == "4":
    leavingthebath = fin_bathroom()
    with open('data/bathroom.json', 'a') as outfile:
        json.dump(leavingthebath, outfile, indent=4)
        print("\n \nTask Logged.")
elif task == "5":
    readit_on_reddit = start_reddit()
    with open('data/reddit.json', 'a') as outfile:
        json.dump(readit_on_reddit, outfile, indent=4)
        print("\n \nTask Logged.")
elif task == "6":
    finished_reading_reddit = fin_reddit()
    with open('data/reddit.json', 'a') as outfile:
        json.dump(finished_reading_reddit, outfile, indent=4)
        print("\n \nTask Logged.")
elif task == "7":
    working_from_home = start_homework()
    with open('data/homework.json', 'a') as outfile:
        json.dump(working_from_home, outfile, indent=4)
        print("\n \nTask Logged.")
elif task == "8":
    finished_homework = fin_homework()
    with open("data/homework.json", 'a') as outfile:
        json.dump(finished_homework, outfile, indent=4)
        print("\n \nTask Logged.")
elif task == "9":
    eagling_up = start_eagle_work()
    with open("data/eagle.json", 'a') as outfile:
        json.dump(eagling_up, outfile, indent=4)
        print("\n \nTask Logged.")
elif task == "10":
    eagling_down = stop_eagle_work()
    with open("data/eagle.json", 'a') as outfile:
        json.dump(eagling_down, outfile, indent=4)
        print("\n \nTask Logged.")
        
elif task == "11":
    starting_rides = start_bus()
    with open("data/bus.json", 'a') as outfile:
        json.dump(starting_rides, outfile, indent=4)
        print("\n \nTask Logged.")
        
elif task == "12":
    stopping_rides = fin_bus()
    with open("data/bus.json", 'a') as outfile:
        json.dump(stopping_rides, outfile, indent=4)
        print("\n \nTask Logged.")
        
elif task == "13":
    making_the_Bread = start_work()
    with open("data/work.json", 'a') as outfile:
        json.dump(making_the_Bread, outfile, indent=4)
        print("\n \nTask Logged.")

elif task == "14":
    taking_the_bread_out = fin_work()
    with open("data/work.json", 'a') as outfile:
        json.dump(taking_the_bread_out, outfile, indent=4)
        print("\n \nTask Logged.")

elif task == "15":
    getting_a_schooling = start_school()
    with open("data/school.json", 'a') as outfile:
        json.dump(getting_a_schooling, outfile, indent=4)
        print("\n \nTask Logged.")
elif task == "16":
    stopping_a_schooling = fin_school()
    with open("data/school.json", 'a') as outfile:
        json.dump(stopping_a_schooling, outfile, indent=4)
        print("\n \nTask Logged.")
#with open('data/data.json', 'w') as outfile:
    #json.dump(the_entry, outfile, indent=4)
