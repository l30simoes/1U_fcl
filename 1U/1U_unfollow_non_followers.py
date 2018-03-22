"""
    instabot example

    Workflow:
        1) unfollows users that don't follow you.
"""

import sys
import os
import argparse

sys.path.append(os.path.join(sys.path[0], '../../'))

from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
args = parser.parse_args()

bot = Bot(max_unfollows_per_day=800)

bot.login(username='1sturban', password='Insta12#',
          proxy=args.proxy)
bot.unfollow_non_followers()
