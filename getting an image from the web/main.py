from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv') # load th frontend

class FirstScreen(Screen):
    def get_image_link(self):
        # Get user query from TextInput
        query = self.manager.current_screen.ids.user_query.text
        
        # Get wikipedia page and the first image link
        page = wikipedia.page(query)
        image_link = page.images[0]
        return image_link
        
    def download_image(self):
        # Download the image
        req = requests.get(self.get_image_link())
        imagepath = 'files/image.jpg'
        with open(imagepath, 'wb') as file:
            file.write(req.content)
        return imagepath
        
    def set_image(self):
        # Set the image in the Image widget
        self.manager.current_screen.ids.img.source = self.download_image()
        
class RootWidget(ScreenManager):
    pass
    
class MainApp(App):

    def build(self):
        return RootWidget()
        
MainApp().run()

#################################################

# Test
'''
page = wikipedia.page("beach")
type(page)
dir(page)
page.summary
page.images
len(page.images) # 37: number of images
page.images[0] # first image, get the url

# downloading an image from a url
# install package: requests
import requests
link = page.images[0]
link # get the url
req = requests.get(link)
type(req)
req.content # content in bytes
type(req.content) # bytes
with open("the_beach.jpg", 'wb') as file:
  file.write(req.content)
'''
