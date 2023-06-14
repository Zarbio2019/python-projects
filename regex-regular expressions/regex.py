import re

filenames = ['nov-12.txt', 'november-14.txt', 'Oct-17.txt', 'Nov-22.txt']

text = 'Hi there you here exa_mple@example.com @blabla some more text here and there another@example.de'

pattern = re.compile("[^ ]+@[^ ]+.[a-z]+")
# [^ ]: allow any caracter except " "
# [a-z]: allow a-z
# + : all characters

matches = pattern.findall(text)
matches # show: ['exa_mple@example.com', 'another@example.de']

#################################################

# Meta Characters

.        Matches any single character
\        Escapes one of the meta characters to treat it as a regular character
[...]    Matches a single character or a range that is contained within brackets
         _- -_ order does not matter but without brackets order does matter
+        Matches the preeceding element one or more times
?        Matches the preeceding pattern element zero or one time
*        Matches the preeceding element zero or more times
{m,n}    Matches the preeceding element at least m and not more than n times
^        Matches the beginning of a line or string
$        Matches the end of a line or string
[^...]   Matches a single character or a range that is not contained within the brackets
?:...|..."Or" operator
()       Matches an optional expression

text = 'Hi there you here exa_mple@example=com @blabla some more text here and there another@example.de'

pattern = re.compile("[^ ]+@[^ ]+.[a-z]+") # return ['exa_mple@example=com', 'another@example.de']
pattern = re.compile("[^ ]+@[^ ]+\.[a-z]+") # return ['another@example.de']

pattern = re.compile("[naother]+@[^ ]+\.[a-z]+") # [] = any order, return ['another@example.de']
pattern = re.compile("aother+@[^ ]+\.[a-z]+") # return empty

pattern = re.compile("[^ ]?+@[^ ]+\.[a-z]+") # return ['r@example.de']

text = 'Hi there you here exa_mple@example.com @blabla some more text here and there another@example.de'
pattern = re.compile("[^ ]?*@[^ ]+\.[a-z]+")
pattern = re.compile("[^ ]?{3}@[^ ]+\.[a-z]+") # return ['ple@example.com', 'her@example.de']

pattern = re.compile("^[^ ]+@[^ ]+\.[a-z]+")
pattern = re.compile("$[^ ]+@[^ ]+\.[a-z]+")

pattern = re.compile("[^ ]+@[^ ]+\.(?:com|de)+")

matches = pattern.findall(text)
matches
