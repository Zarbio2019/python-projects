import qrcode
 
with open('urls.txt') as file:
  lines = file.readlines()
  count = 1
  for line in lines:
    img = qrcode.make(line)
    img.save(f"{count}.png")
    count += 1