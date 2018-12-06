import collections
import datetime

entries = []
raw_entries = []

with open("input.txt") as inputFile:
    for line in inputFile:
        parts = line.strip("\n").split(" ")
        date_string = parts[0] + " " + parts[1]
        date = datetime.datetime.strptime(date_string, "[%Y-%m-%d %H:%M]")
        unordered_entry = {"date": date, "data": line.strip(date_string)}
        raw_entries.append(unordered_entry)

raw_entries.sort(key=lambda x: x["date"])

last_guard = ""
for raw_entry in raw_entries:
    parts = raw_entry["data"].strip("\n").split(" ")
    action = ""
    if parts[0] == "Guard":
        last_guard = parts[1]
        action = parts[2] + " " + parts[3]
    else:
        action = parts[0] + " " + parts[1]
    entry = {"date": raw_entry["date"], "guard": last_guard, "action": action}
    entries.append(entry)

for entry in entries:
    print entry

guards_sleep = dict()
guard = ""
guard_start = None
guard_falls_asleep = None
guard_wakes_up = None
guard_asleep_minutes_in_hour = []
for entry in entries:
    current_action = entry["action"]
    current_date = entry["date"]
    if current_action == "begins shift":
        #end old shift
        if guard is not None:
            # guards_sleep[guard] += (guard_wakes_up - guard_falls_asleep).minute
            guard_falls_asleep = None
            guard_wakes_up = None
            guard_start = current_date
            guard_asleep_minutes_in_hour = []
            guard = entry["guard"]
        else:
            guard = entry["guard"]
            guard_asleep_minutes_in_hour = []
        continue
    elif current_action == "falls asleep":
        guard_falls_asleep = current_date
    elif current_action == "wakes up":
        guard_wakes_up = current_date
        # guard_wakes_up = current_date - datetime.timedelta(minutes=1)
        minutes_asleep = (guard_wakes_up - guard_falls_asleep).seconds / 60

        guard_asleep_minutes_in_hour = []
        # minutes in the hour they were asleep
        for x in range(guard_falls_asleep.minute, guard_falls_asleep.minute + minutes_asleep):
            guard_asleep_minutes_in_hour.append(x % 60)

        if guard in guards_sleep:
            guards_sleep[guard]["time_asleep_in_minutes"] += minutes_asleep
            guards_sleep[guard]["minutes_in_hour_asleep"] += guard_asleep_minutes_in_hour
        else:
            d = {"time_asleep_in_minutes": minutes_asleep, "minutes_in_hour_asleep": guard_asleep_minutes_in_hour}
            guards_sleep[guard] = d

guards_most_common_minute = dict()
for key, value in guards_sleep.iteritems():
    print "Guard:", key, "Total Minutes:", value["time_asleep_in_minutes"], "Counter:", collections.Counter(value["minutes_in_hour_asleep"])
    # print collections.Counter(value["time_asleep_in_minutes"])
    most_common_minute = collections.Counter(value["minutes_in_hour_asleep"]).most_common(1)[0][0]
    guards_most_common_minute[key] = {"most_common":most_common_minute, "occurrences": collections.Counter(value["minutes_in_hour_asleep"]).most_common(1)[0][1]}

print guards_most_common_minute
for key in guards_most_common_minute:
    print "Guard", key, "Minute", guards_most_common_minute[key]