import os
from datetime import datetime

import flask
import icalendar as ical


def display(cal):
    return cal.to_ical().decode("utf-8").replace("\r\n", "\n").strip()


def time_format(line: str) -> str:
    time = ""
    reversed_line = reversed(line)
    for char in reversed_line:
        if char == "T":
            break
        else:
            time += char

    # take 24 hour time in format 132500
    # and put it in 12 hour time in format 1:25:00 PM
    time = list(reversed(time))
    time.insert(2, ":")
    time.insert(5, ":")
    hour = int(time[0] + time[1]) - 12
    if hour > 0:
        time.append("PM")
        hour = str(hour)

    else:
        hour = hour + 12
        time.append("AM")
        hour = str(hour)

    if int(hour) < 10:
        hour = "0" + hour

    time[0], time[1] = hour[0], hour[1]
    time = "".join(time)

    return time

def date_format(line: str) -> str:
    date = ""
    colon_pos = line.rfind(":")
    line = line[colon_pos + 1 :]
    for char in line:
        if char == "T":
            break
        else:
            date += char
    # date is in form YEARMMDD
    # put year at end and seperate with "/"
    new_date = date[4:6] + "/" + date[6:] + "/" + date[0:4]
    return new_date

now = datetime.now()

# pick semester
semesters = os.listdir("schedules")
semesters = {i: semesters[i] for i in range(len(semesters))}

for semester in semesters:
    print(f"{semester}: {semesters[semester]}")

choice = int(input("Pick a semester: "))
semester = semesters[choice]

# load calender from schedules/semester.ics
with open(f"schedules/{semester}", mode="r", encoding="utf-8") as f:
    cal = ical.Calendar.from_ical(f.read())
    for event in cal.walk("VEVENT"):
        summary = str(event.get("summary")).strip()
        location = str(event.get("location")).strip()
        start = str(event.get("dtstart")).strip()
        end = str(event.get("dtend")).strip()
        info = [summary, location, start, end]
        print(info)

today = now.strftime("%m/%d/%Y")
curr_time = now.strftime("%I:%M:%S %p")