import itertools

doubles = 0
triples = 0
all_lines = [list(x) for x in open("input.txt").read().splitlines()]

for line in all_lines:
    character_dict = dict()
    for character in line:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    if character_dict.values().__contains__(2):
        doubles += 1
    if character_dict.values().__contains__(3):
        triples += 1

print "Part 1 found", doubles, "doubles and", triples, "triples. Result:", doubles * triples

all_combinations = list(itertools.combinations(all_lines, 2))
results = dict()

for combination in all_combinations:
    a = list(combination[0])
    b = list(combination[1])
    in_common = [y for x, y in enumerate(a) if y == b[x]]
    results[len(in_common)] = "".join(in_common)

print "\nPart 2"
for key in results:
    print "Matching:", len(list(results[key])), results[key]
