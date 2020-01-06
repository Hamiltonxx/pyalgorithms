line = input()
song = line.split("WUB")
song = [x for x in song if x!='']
print(' '.join(song))