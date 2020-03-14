#%%
import praw
import pdb
import re
import os
import json


with open('config.json', 'r') as f:
    config = json.loads(f.read())

reddit = praw.Reddit(client_id = config['client_id'],
                    client_secret = config['client_secret'],
                    password = config['password'],
                    user_agent = config['user_agent'],
                    username = config['username'])
subreddit = reddit.subreddit('pythonforengineers')

#%%
if not os.path.isfile('posts_replied_to.txt'):
    posts_replied_to = []
else:
    with open('posts_repliect_to.txt', 'r') as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split('\n')
        posts_replied_to = list(filter(None, posts_replied_to))
# %%
for submission in subreddit.hot(limit=10):
    if submission.id not in posts_replied_to:
        if re.search('i love python', submission.title, re.IGNORECASE):
            submission.reply("Slackbot says: I also love python!")
            print("Bot replying to: {}".format(submission.title))
            posts_replied_to = posts_replied_to.append(submission.id)
# %%
with open('posts_replied_to.txt', 'w') as f:
    for post_id in posts_replied_to:
        f.write(post_id + '\n')