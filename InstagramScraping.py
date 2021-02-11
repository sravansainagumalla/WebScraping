# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:46:26 2021

@author: nagum
"""

import instaloader

bot = instaloader.Instaloader()


profile = instaloader.Profile.from_username(bot.context, 'dheeraj_saiiii')


print(type(profile))


print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio: ", profile.biography,profile.external_url)