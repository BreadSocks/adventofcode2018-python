import itertools

all_lines = [list(x) for x in open("input.txt").read().splitlines()]
all_combinations = list(itertools.combinations(all_lines, 2))
results = dict()

for combination in all_combinations:
    a = list(combination[0])
    b = list(combination[1])
    in_common = [y for x, y in enumerate(a) if y == b[x]]
    results[len(in_common)] = "".join(in_common)

for key in results:
    print "Matching:", len(list(results[key])), results[key]
