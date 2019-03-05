import json
import datetime

def dataCollection():
    # localDate.year, month, etc
    localDate = datetime.datetime.now()
    entry={
            "year":localDate.year,
            "month":localDate.month,
            "day":localDate.day,
            "hour":localDate.hour,
            "minute":localDate.minute,
            "second":localDate.second,
            "nano":localDate.microsecond
            }
    return entry
   
the_entry = dataCollection()

print(the_entry)

with open('data.json', 'w') as outfile:
    json.dump(the_entry, outfile, indent=4)
