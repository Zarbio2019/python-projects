# Author: Zarbio Romulo

import praw

reddit = praw.Reddit(user_agent=True, client_id="YOUR REDDIT APP ID", 
  client_secret="YOUR REDDIT APP SECRET", username='YOUR REDDIT USERNAME', password='YOUR REDDIT ACCOUNT PASSWORD')

url = "https://www.reddit.com/r/cats/comments/qz201u/declawing_hurts_your_cat/"

# get text of post
post = reddit.submission(url=url)
print(post.title)
print(post.selftext)

# get top level comments from post
print(len(post.comments))
for comment in post.comments:
  print(comment.body)