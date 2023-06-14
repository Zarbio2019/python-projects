# Author: Zarbio Romulo

import praw
from datetime import datetime, timedelta

reddit = praw.Reddit(user_agent=True, client_id="YOUR REDDIT APP ID", 
  client_secret="YOUR REDDIT APP SECRET", username='YOUR REDDIT USERNAME', password='YOUR REDDIT ACCOUNT PASSWORD')

subreddit = reddit.subreddit("glassblowing")


for post in subreddit.new(): # give us: www.reddit.com/r/glassblowing/new (new button)
  current_time = datetime.utcnow()
  post_time = datetime.utcfromtimestamp(post.created)
  delta_time = current_time - post_time
  if delta_time <= timedelta(hours=48):
    if "christmas" in post.title.lower(): # searh in title of post
      # print(post.title) # get the title of the post
      # post.reply('Hey, Christmas is coming!')
      
      # to add comments to existing comments:
      for comment in post.comments:
        if "is coming" in comment.body.lower():
          comment.reply("Yeah, it's coming") # limitation: wait for 7 minutes
