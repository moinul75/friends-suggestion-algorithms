"""
Find Friends Algorithms(Suggested Friends)
implement by Moinul75

"""
#find this is the database 
user1_friends = {'Ajoy','Mehedi','Sakib','Nira','Tina'}
user2_friends = {'Ajoy','Naima','Rasel','Sakib','Mehedi','Zisan'}
user3_frinds = {'Moinul','Sadiya','Nayeem','Rana'}

import time


def suggest_friends(*args, find_friends_for):
    suggested_friends = set()
    
    for arg in args:
        frineds_dif = arg.difference(find_friends_for)
        suggested_friends.update(frineds_dif)
    
    return suggested_friends

user3_frinds_suggestion = suggest_friends(user1_friends,user3_frinds,find_friends_for=user3_frinds)
user1_friends_suggestion = suggest_friends(user2_friends,user3_frinds,find_friends_for=user1_friends)
user2_friends_suggestion = suggest_friends(user1_friends,user3_frinds,find_friends_for=user2_friends)


print("Find Friends For user3: ")
for friend in user3_frinds_suggestion:
        print(friend)
print("\n\n")        
print("Find Friends For user1: ")
#for user1 find frinends suggestion 
for friend in user1_friends_suggestion:
    print(friend)

print("\n\n")        
print("Find Friends For user2: ")
#for user1 find frinends suggestion 
for friend in user2_friends_suggestion:
    print(friend)
    

   

