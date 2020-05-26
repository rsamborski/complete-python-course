
friends_list = input("Please give the name of your 3 friends: ").split(',')
people_list = []

with open("people.txt") as people_file:
    people_list = [l.strip() for l in people_file.readlines()]
    people_file.close()

friends_set = set(friends_list)
people_set = set(people_list)

nearby_friends_set = friends_set.intersection(people_set)

with open("nearby_friends.txt", )