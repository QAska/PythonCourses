players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])         #1-3 elements
print(players[1:4])         #2-4 elements
print(players[:4])          #1-4 elements
print(players[2:])          #from 3 to last elements
print(players[-3:])         #last 3 elements

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())