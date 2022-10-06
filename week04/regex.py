# I am not sure if i should include the names in a sentence or a paragraph. I just generate
# a list of names.
# I used https://regexr.com/ to test 
# [A-Z] match a character in the range "A to "Z"
# [a-z] match a character in the range "a to "z"
# [-,. '] matches any of these charcters
# () is to group and + to match all the preceding

import re


def find_date(line):
    pattern = r"[A-Za-z][-,A-Za-z. ']+"
    result = re.findall(pattern,line)
    return result


f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_names(line)
    if (len(result)>0):
        print(result)
