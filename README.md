# UnsubNSFW
## Requirements
**System Requirements:**
- Python 3+
- Praw

### Install Praw
`pip install praw`

### Setting Up
1. Navigate to https://www.reddit.com/prefs/apps
2. Click create another app
3. Name it (For simplicity, I used UnsubNSFW)
4. Tick the script option
5. For redirect uri: http://127.0.0.1

In the praw.ini file, edit the following fields to add your information.

https://www.pythonforengineers.com/wp-content/uploads/2014/11/redditbot2.jpg 

client_id would be the red outlined box. (Refer to link above)\
client_secret would be the blue outlined box. (Refer to link above)\
Password would be the password for the reddit account you want to use.\
Username would be the username for the reddit account you want to use.

> [bot1]  
> client_id=  
> client_secret=  
> password=  
> username=  
> user_agent=UnsubNSFW 0.1  

### To Run
1. Open terminal/cmd/shell and navigate to the directory which the script lies in.
2. Run `python unsub.py`
3. The script will then unsubscribe you from all NSFW subreddits while listing the name of each subreddit it unsubscribes from.
4. The total amount of subreddits that you have unsubscribed from will be displayed.

Special thanks to https://www.pythonforengineers.com/build-a-reddit-bot-part-1/ for providing the image and tutorial
