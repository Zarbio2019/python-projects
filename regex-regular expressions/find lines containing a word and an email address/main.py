import re
 
pattern = re.compile(".*Delhi.*[^ ]+@[^ ]+\.[a-z]+", re.IGNORECASE)
matches = [match for match in data if pattern.findall(match)]
print(matches)

# Explanation:
'''
.*Delhi.* searches for Delhi anywhere in the line.

[^ ]+ searches for one or more characters other than white space.

@[^ ]+ searches for an @ symbol followed by any number of characters other than space.

\.[a-z]+ searches for a dot followed by any number of letters.
'''