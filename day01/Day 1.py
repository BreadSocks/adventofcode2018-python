import itertools

changes = [int(i) for i in open("input.txt").read().splitlines()]

print "Part 1 : ", sum(changes)

frequency = 0
found_frequencies = {0}

for number in itertools.cycle(changes):
    frequency += number
    if frequency in found_frequencies:
        print "Part 2 : ", frequency
        exit()
    else:
        found_frequencies.add(frequency)
