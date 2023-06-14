import re
 
pattern = re.compile(".*Delhi.*", re.IGNORECASE)
matches = [match for match in data if pattern.findall(match)]
print(matches)

# Explanation:
'''
.*Delhi.* instructs the program that Delhi could be found between any number of characters. The part .* means there could be any number of characters before or after Delhi. The expression .*Delhi.* could also be replaced with just Delhi and still produce the same result, but .*Delhi.* is more explicit and more logical.
'''
