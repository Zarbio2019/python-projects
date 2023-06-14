# Author: Zarbio Romulo

with open('merged.csv', 'r') as file:
  content = file.readlines()

content[0] = 'ID,AMOUNT,COST\n' # 0 = first line

with open('merged.csv', 'w') as file:
  file.writelines(content)