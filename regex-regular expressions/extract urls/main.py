# read file
with open('urls.txt', 'r') as file:
    content = file.read()

print(content)

# process
import re

pattern = re.compile("https?://(?:www.)?[^ \n]+\.com")
matches = pattern.findall(content)
matches

#['http://google.com',
# 'https://example.com',
# 'http://www.wikipedia.com',
# 'http://pythonhow.com']
