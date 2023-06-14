import re
 
pattern = re.compile(".*Delhi.*[0|+][0-9]{4,50}", re.IGNORECASE)
matches = [match for match in data if pattern.findall(match)]
print(matches)

# Explanation:
'''
.*Delhi.* searches for Delhi anywhere in the line.

[0|+] searches for a 0 or a +

[0-9]{4,50} searches if there is a number with a length from 4 to 50 digits. This assumes phone numbers are not shorter than 4 digits and not longer than 50.
'''