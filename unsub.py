#!/usr/bin/python
import praw

reddit = praw.Reddit('bot1')
count = 0

for sub in reddit.user.subreddits(limit=None):
    if sub.over18 == True:
        count = count + 1
        sub.unsubscribe()
        print(str(sub) + " unsubscribed.")

print("You have unsubscribed from " + str(count) + " NSFW subreddits.")