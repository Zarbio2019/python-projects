# Author: Zarbio Romulo

import praw

reddit = praw.Reddit(user_agent=True, client_id="YOUR REDDIT APP ID", 
  client_secret="YOUR REDDIT APP SECRET", username='YOUR REDDIT USERNAME', password='YOUR REDDIT ACCOUNT PASSWORD')

subreddit = reddit.subreddit("pythonsandlot")
subreddit.validate_on_submit = True

title = 'This is my new Python Bot submission'
content = """
Hey, I am just trying out Python!
This is my first post!
"""

subreddit.submit(title=title, selftext=content)
