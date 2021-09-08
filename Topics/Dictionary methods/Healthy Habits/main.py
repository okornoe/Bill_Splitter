# the list "walks" is already defined
# your code here
total = 0
for x in range(len(walks)):
    total += walks[x]["distance"]
print(total // len(walks))