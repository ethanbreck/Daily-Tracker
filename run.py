import json
import datetime

task = input("Whats the Task? ")

def start_shower():
    # localDate.year, month, etc
    global Task
    start_task = input("Starting or Stopping? Or coming and going? ")
    print(start_task)
    print(task)
    localDate = datetime.datetime.now()
    entry={
            "Task": task,
            "Start/End": start_task,
            "year":localDate.year,
            "month":localDate.month,
            "day":localDate.day,
            "hour":localDate.hour,
            "minute":localDate.minute,
            "second":localDate.second,
            }
    return entry

if task == "Shower" or "shower":
    starting_shower = start_shower()
    #outfile, and shower_data is appending to the shower specific json file
    with open('data/master_schedule.json') as masterfile:
        main_data = json.load(masterfile)
        main_data.append(starting_shower)
    with open('data/master_schedule.json', mode="w+") as masterfile:
        json.dump(main_data, masterfile, indent=4)
        print("\n \nTask Logged in Masterfile")
else:
    print("Not sure how you got here")
#with open('data/data.json', 'w') as outfile:
    #json.dump(the_entry, outfile, indent=4)
