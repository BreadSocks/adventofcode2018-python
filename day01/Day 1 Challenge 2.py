frequency = 0
found_frequencies = {0}
break_loop = False
loops = 1
changes = []
with open("input.txt") as inputFile:
    for line in inputFile:
        line = line.replace("\n", "")
        number = int(line)
        changes.append(number)

print changes

while not break_loop:
    for number in changes:
        frequency += number
        if frequency in found_frequencies:
            print "Found : ", frequency
            found_frequencies.add(frequency)
            break_loop = True
            break
        else:
            found_frequencies.add(frequency)
    print "Finished Loop: ", loops
    loops += 1
