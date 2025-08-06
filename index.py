import praw
import pandas as pd

reddit_read_only = praw.Reddit(site_name="bot1")

subreddit = reddit_read_only.subreddit("IndianStockMarket")

print("Display Name:", subreddit.display_name)
print("Title:", subreddit.title)

posts = subreddit.top(limit = 10,time_filter="day")
posts_dict = {"Title":[], 
              "Post Text":[],
              "ID":[],
              "Score":[],
              "Total Comments":[],
              "Post URL":[]}

for post in posts:
    posts_dict["Title"].append(post.title)
    posts_dict["Post Text"].append(post.selftext)
    posts_dict["ID"].append(post.id)
    posts_dict["Score"].append(post.score)
    posts_dict["Total Comments"].append(post.num_comments)
    posts_dict["Post URL"].append(post.url)

top_posts = pd.DataFrame(posts_dict)
print(top_posts)
top_posts.to_csv("Top Posts.csv", index=True)
