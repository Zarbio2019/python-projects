import re
 
pattern = re.compile(".*Delhi.*([0|+][0-9]{4,50}|[^ ]+@[^ ]+.[a-z]+)", re.IGNORECASE)
matches = [match for match in data if pattern.findall(match)]
print(matches)


# Explanation:
'''
.*Delhi.* searches for Delhi anywhere in the line.

[0|+][0-9]{4,50} searches for a 0 or a + followed a number of 4 to 50 digits.

| makes the preceding and proceeding patterns optional.

[^ ]+@[^ ]+.[a-z]+ searches for email addresses.

( ) are part of the ( | ) "OR" syntax.
'''