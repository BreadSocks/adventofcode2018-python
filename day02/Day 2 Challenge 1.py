doubles = 0
triples = 0

with open("input.txt") as inputFile:
    for line in inputFile:
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

print "Found", doubles, "doubles and", triples, "triples. Result:", doubles * triples
