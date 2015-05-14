# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:33:33 2015

P22 example 1

@author: Wanqing
"""

users = [
    {"id":0, "name":"hero"},
    {"id":1, "name":"Dunn"},
    {"id":2, "name":"Sue"},
    {"id":3, "name":"Chi"},
    {"id":4, "name":"Thor"},
    {"id":5, "name":"Clive"},
    {"id":6, "name":"Hicks"},
    {"id":7, "name":"Devin"},
    {"id":8, "name":"Kate"},
    {"id":9, "name":"Klein"}
    ]
    
friendships = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),
               (4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

for user in users:
    user["friends"] = []
    
for i,j in friendships:
    users[i]["friends"].append(users[j]["name"])
    users[j]["friends"].append(users[i]["name"])
    
# define a function to calculate number of friends
def number_of_friends(user):
    """how many friends does _user_ have?"""
    return len(user["friends"])

total_connections = sum(number_of_friends(user) for user in users)