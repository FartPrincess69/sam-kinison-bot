import praw
import time

reddit = praw.Reddit(  
        user_agent="Sam Kinison Bot" ,
        client_id="ubtXt_FGb831V1t4w3Os5Q",
        client_secret="0Pf4xmkTDX5SvQ-t9b8yhBPQygHTjQ",
        username="SamKinisonBot",
        password="WeRGr00t",)

subreddit = reddit.subreddit("comedy")

sam_reply = ["CAUSE IT'S A JOKE OHH OHHHH OHHHHHHHHH"]

for submission in subreddit.hot(limit=10):
  #  print(submission.title)

    for comment in submission.comments:
        if hasattr(comment,"body"):
           comment_lower = comment.body.lower()
           if " a joke " in comment_lower:
                # print("------")
                 print(comment.body)
                 comment.reply(sam_reply)
                 time.sleep(66)
