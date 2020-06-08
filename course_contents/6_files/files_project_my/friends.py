
friends_list = input("Please give the name of your 3 friends: ").split(',')
#people_list = []

with open("people.txt") as people_file:
    people_list = [l.strip() for l in people_file.readlines()]

friends_set = set(friends_list)
people_set = set(people_list)

print(f"Friends: {friends_set}")
print(f"People: {people_set}")

nearby_friends_set = friends_set.intersection(people_set)

print(f"Nearby friends: {nearby_friends_set}")

with open("nearby_friends.txt", "w") as nearby_friends_file:
    nearby_friends_file.write('\n'.join(nearby_friends_set))
    nearby_friends_file.close()
