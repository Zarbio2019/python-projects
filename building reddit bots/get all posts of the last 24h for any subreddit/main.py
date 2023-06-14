# Author: Zarbio Romulo

import praw
from datetime import datetime, timedelta

reddit = praw.Reddit(user_agent=True, client_id="YOUR REDDIT APP ID", 
  client_secret="YOUR REDDIT APP SECRET", username='YOUR REDDIT USERNAME', password='YOUR REDDIT ACCOUNT PASSWORD')

# www.reddit.com/r/glassblowing/
subreddit = reddit.subreddit("glassblowing")

posts24h = []

with open('output.txt', 'w') as file: # write in a file
  for post in subreddit.new():
    current_time = datetime.utcnow()
    post_time = datetime.utcfromtimestamp(post.created) # convert to datetime

    delta_time = current_time - post_time
    # print(delta_time)
    if delta_time <= timedelta(hours=24):
      posts24h.append((post.title, post.selftext, post_time))
      file.write(f'{post.title}\n{post.selftext}\n\n')

# print(posts24h)
