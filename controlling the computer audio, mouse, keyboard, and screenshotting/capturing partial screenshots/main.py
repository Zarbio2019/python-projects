from mss import mss, tools

with mss() as screen:
  part = {'top':257, 'left':900, 'width':500, 'height':400}
  image = screen.grab(part)
  tools.to_png(image.rgb, image.size, output='output.png')
  