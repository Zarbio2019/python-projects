# read file
with open('ips.txt', 'r') as file:
    content = file.read()
print(content)

# process
import re

pattern = re.compile("[0-9]{3}\.[0-9]{3}\.12[0-9]{1}\.[0-9]{3}")
matches = pattern.findall(content)
matches

#['912.131.120.111', '912.131.129.129']
