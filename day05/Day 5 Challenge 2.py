import string
import time

start = time.time()
units = list(open("input.txt").read())
alphabet = string.ascii_lowercase
alphabet = [y for y in alphabet if y in units]
results = dict()

print "1st lap", time.time() - start

for letter in alphabet:

    index = 1
    round_units = units
    round_units = [x for x in round_units if x != letter and x != letter.upper()]
    new_units = [round_units[0]]

    while index < len(round_units):
        unit = round_units[index]
        if len(new_units) == 0:
            new_units.append(unit)
        else:
            previous_unit = new_units[-1]
            if unit.lower() == previous_unit.lower() and unit != previous_unit:
                new_units.pop()
            else:
                new_units.append(unit)
        index += 1

    results[letter] = len(new_units)

print "2nd lap", time.time() - start
print results

lowest = min(results.values())
for key in results:
    if results[key] == lowest:
        print "Letter", key

print "end", time.time() - start
