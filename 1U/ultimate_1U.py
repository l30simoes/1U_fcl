"""
    ULTIMATE SCRIPT

    It uses data written in files:
        * follow_followers.txt
        * follow_following.txt
        * like_hashtags.txt
        * like_users.txt
    and do the job. This bot can be run 24/7.
"""

import os
import sys
import time
from random import shuffle

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

#bot = Bot()

#TXT File Path ///
filePath = os.path.dirname(os.path.abspath(__file__)) + "/"

comments_file_name = filePath + "comments.txt"

bot = Bot(
            # Max
            max_follows_per_day=500,
            max_likes_per_day=500,
            max_unfollows_per_day=300,
            max_comments_per_day=500,

            # Delay
            like_delay=15,
            unfollow_delay=20,
            follow_delay=20,
            comment_delay=25,

            comments_file=comments_file_name

          )
# bot.login()
bot.login(username="1sturban", password="FirstU12#")

# bot.login(username="1nsta_bot001", password="Insta12#")

print ("Comment file: " + comments_file_name)


print("Current script's schedule:")

follow_followers_list = bot.read_list_from_file(filePath + "follow_followers_1U.txt")
print("Going to follow followers of:", follow_followers_list)

follow_following_list = bot.read_list_from_file(filePath + "follow_following_1U.txt")
print("Going to follow following of:", follow_following_list)

like_hashtags_list = bot.read_list_from_file(filePath + "like_hashtags_1U.txt")
print("Going to like hashtags:", like_hashtags_list)

# like_users_list = bot.read_list_from_file(filePath + "like_users_1U.txt")
# print("Going to like users:", like_users_list)


tasks_list = []




for item in follow_followers_list:
    tasks_list.append((bot.follow_followers, {'user_id': item, 'nfollows': None}))

# for item in follow_following_list:
#     tasks_list.append((bot.follow_following, {'user_id': item}))

for item in like_hashtags_list:
    tasks_list.append((bot.like_hashtag, {'hashtag': item, 'amount': None}))

for item in like_hashtags_list:
    tasks_list.append((bot.comment_hashtag, {'hashtag': item, 'amount': None}))



# print ("TASK LIST - " + tasks_list)

# shuffle(tasks_list)

for func, arg in tasks_list:
    func(**arg)
